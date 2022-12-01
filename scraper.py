import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime


def get_tickets_for_plate(plate: str):
    url = 'https://aplicativos.sanpedro.gob.mx/esanpedro/multas/estado_cuenta.asp'
    d = {'placa': plate, 'submit': 'Consultar'}

    x = requests.post(url, data=d)

    soup = BeautifulSoup(x.text, 'html.parser')

    resultsA = soup.find_all('tr')[3].find_all('tr')

    # TODO case of no results

    multas = []
    curr = 0
    for results in resultsA:
        if curr == 0:
            curr += 1
            continue
        multa = {}
        next_td = results.find_next('td')
        multa['municipio'] = next_td.text.strip()
        next_td = next_td.find_next('td')
        multa['boleta'] = next_td.text.strip()
        next_td = next_td.find_next('td')
        multa['fecha'] = next_td.text.strip()
        next_td = next_td.find_next('td')
        multa['infraccion'] = next_td.text.strip()
        next_td = next_td.find_next('td')
        multa['crucero'] = next_td.text.strip()
        next_td = next_td.find_next('td')
        multa['valor'] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next('td')
        multa['descuento'] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next('td')
        multa['total'] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next('td')
        multa['fecha_pago'] = next_td.text.strip()
        next_td = next_td.find_next('td')
        multa['recibo'] = next_td.text.strip()
        if multa['recibo'] == '':
            multa['recibo'] = 0
        next_td = next_td.find_next('td')
        multa['pagado'] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next('td')
        multa['saldo'] = next_td.text.strip().replace(",", "")
        if multa['municipio'] == 'SPGG':  # Cheap validation but works
            try:
                multa['fecha'] = datetime.strptime(multa['fecha'], '%Y%m%d')
            except ValueError:
                multa['fecha'] = datetime.strptime('1/1/1980', '%d/%m/%Y')

            try:
                multa['fecha_pago'] = datetime.strptime(multa['fecha_pago'], '%Y%m%d')
            except ValueError:
                multa['fecha_pago'] = datetime.strptime('1/1/1980', '%d/%m/%Y')

            multas.append(multa)
    return multas


"""
MUN 
Boleta
Fecha
Infraccion
Crucero
Valor
Bonificacion/Descuento
Total
Fecha de Pago
Recibo
Pagado
Saldo
"""

"""
for strong_tag in soup.find_all('tr'):
    print(strong_tag.text, strong_tag.next_sibling)
"""
