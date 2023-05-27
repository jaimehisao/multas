package main

import (
	"fmt"
	"log"
	"net/http"
	"net/url"
	"strings"
	"time"

	"github.com/PuerkitoBio/goquery"
)

const (
	SAN_PEDRO_ASP_ENDPOINT = "https://example.com/san-pedro" // Replace with the actual endpoint URL
	MONTERREY_ASP_ENDPOINT = "https://example.com/monterrey" // Replace with the actual endpoint URL
)

type Ticket struct {
	Municipio  string
	Boleta     string
	Fecha      string
	Infraccion string
	Crucero    string
	Valor      string
	Descuento  string
	Total      string
	FechaPago  string
	Recibo     string
	Pagado     string
	Saldo      string
}

func getSanPedroTicketsForPlate(plate string) ([]Ticket, error) {
	d := url.Values{
		"placa":  {plate},
		"submit": {"Consultar"},
	}

	resp, err := http.PostForm(SAN_PEDRO_ASP_ENDPOINT, d)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		return nil, err
	}

	resultsA := doc.Find("tr").Eq(3).Find("tr")

	var multas []Ticket
	curr := 0
	resultsA.Each(func(i int, s *goquery.Selection) {
		if curr == 0 {
			curr++
			return
		}
		multa := Ticket{}
		nextTd := s.Find("td").First()
		multa.Municipio = nextTd.Text()

		nextTd = nextTd.Next()
		multa.Boleta = nextTd.Text()

		nextTd = nextTd.Next()
		multa.Fecha = nextTd.Text()

		nextTd = nextTd.Next()
		multa.Infraccion = nextTd.Text()

		nextTd = nextTd.Next()
		multa.Crucero = nextTd.Text()

		nextTd = nextTd.Next()
		multa.Valor = strings.ReplaceAll(nextTd.Text(), ",", "")

		nextTd = nextTd.Next()
		multa.Descuento = strings.ReplaceAll(nextTd.Text(), ",", "")

		nextTd = nextTd.Next()
		multa.Total = strings.ReplaceAll(nextTd.Text(), ",", "")

		nextTd = nextTd.Next()
		multa.FechaPago = nextTd.Text()

		nextTd = nextTd.Next()
		multa.Recibo = nextTd.Text()
		if multa.Recibo == "" {
			multa.Recibo = "0"
		}

		nextTd = nextTd.Next()
		multa.Pagado = strings.ReplaceAll(nextTd.Text(), ",", "")

		nextTd = nextTd.Next()
		multa.Saldo = strings.ReplaceAll(nextTd.Text(), ",", "")

		if multa.Municipio == "SPGG" {
			var parseErr error
			multa.Fecha, parseErr = time.Parse("20060102", multa.Fecha)
			if parseErr != nil {
				multa.Fecha, _ = time.Parse("02/01/2006", "1/1/1980")
			}

			multa.FechaPago, parseErr = time.Parse("20060102", multa.FechaPago)
			if parseErr != nil {
				multa.FechaPago, _ = time.Parse("02/01/2006", "1/1/1980")
			}

			multas = append(multas, multa)
		}
	})

	return multas, nil
}

func getMonterreyTicketsForPlate(plate string) ([]Ticket, error) {
	client := http.DefaultClient

	req, err := http.NewRequest("GET", MONTERREY_ASP_ENDPOINT, nil)
	if err != nil {
		return nil, err
	}

	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		return nil, err
	}

	verifyForm := doc.Find("form")

	if verifyForm.Length() > 0 {
		resultsA := verifyForm.Find("table").Eq(1).Find("tbody").Eq(0).Find("tr")

		var multas []Ticket
		resultsA.Each(func(i int, s *goquery.Selection) {
			multa := Ticket{
				Municipio: "MTY",
			}

			nextTd := s.Find("td").First()
			multa.Boleta = nextTd.Text()

			nextTd = nextTd.Next()
			multa.Placa = nextTd.Text()

			nextTd = nextTd.Next()
			multa.Fecha = nextTd.Text()

			nextTd = nextTd.Next()
			multa.Infraccion = nextTd.Text()

			nextTd = nextTd.Next()
			multa.Crucero = nextTd.Text()

			nextTd = nextTd.Next()
			multa.Descuento = nextTd.Text()

			nextTd = nextTd.Next()
			multa.Monto = strings.ReplaceAll(nextTd.Text(), "$", "")
			multa.Monto = strings.ReplaceAll(multa.Monto, ",", "")

			var parseErr error
			multa.Fecha, parseErr = time.Parse("02/01/2006", multa.Fecha)
			if parseErr != nil {
				multa.Fecha, _ = time.Parse("02/01/2006", "1/1/1980")
			}

			multas = append(multas, multa)
		})

		return multas, nil
	}

	return nil, nil
}

func main() {
	plate := "ABC123" // Replace with the desired license plate

	sanPedroTickets, err := getSanPedroTicketsForPlate(plate)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("San Pedro Tickets:")
	for _, ticket := range sanPedroTickets {
		fmt.Printf("%+v\n", ticket)
	}

	monterreyTickets, err := getMonterreyTicketsForPlate(plate)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Monterrey Tickets:")
	for _, ticket := range monterreyTickets {
		fmt.Printf("%+v\n", ticket)
	}
}
