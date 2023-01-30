import time

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import js2py

from constants import SAN_PEDRO_ASP_ENDPOINT, MONTERREY_ASP_ENDPOINT


def get_san_pedro_tickets_for_plate(plate: str):
    """
    Retrieves and scrapes tickets from San Pedro Garza García.
    :param plate: string plate to search for.
    :return: a ticket dictionary with the details.
    """
    d = {"placa": plate, "submit": "Consultar"}

    x = requests.post(SAN_PEDRO_ASP_ENDPOINT, data=d)

    soup = BeautifulSoup(x.text, "html.parser")

    resultsA = soup.find_all("tr")[3].find_all("tr")

    multas = []
    curr = 0
    for results in resultsA:
        if curr == 0:
            curr += 1
            continue
        multa = {}
        next_td = results.find_next("td")
        multa["municipio"] = next_td.text.strip()
        next_td = next_td.find_next("td")
        multa["boleta"] = next_td.text.strip()
        next_td = next_td.find_next("td")
        multa["fecha"] = next_td.text.strip()
        next_td = next_td.find_next("td")
        multa["infraccion"] = next_td.text.strip()
        next_td = next_td.find_next("td")
        multa["crucero"] = next_td.text.strip()
        next_td = next_td.find_next("td")
        multa["valor"] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next("td")
        multa["descuento"] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next("td")
        multa["total"] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next("td")
        multa["fecha_pago"] = next_td.text.strip()
        next_td = next_td.find_next("td")
        multa["recibo"] = next_td.text.strip()
        if multa["recibo"] == "":
            multa["recibo"] = 0
        next_td = next_td.find_next("td")
        multa["pagado"] = next_td.text.strip().replace(",", "")
        next_td = next_td.find_next("td")
        multa["saldo"] = next_td.text.strip().replace(",", "")
        if multa["municipio"] == "SPGG":  # Cheap validation but works
            try:
                multa["fecha"] = datetime.strptime(multa["fecha"], "%Y%m%d")
            except ValueError:
                multa["fecha"] = datetime.strptime("1/1/1980", "%d/%m/%Y")

            try:
                multa["fecha_pago"] = datetime.strptime(multa["fecha_pago"], "%Y%m%d")
            except ValueError:
                multa["fecha_pago"] = datetime.strptime("1/1/1980", "%d/%m/%Y")

            multas.append(multa)
    return multas


def get_monterrey_tickets_for_plate(plate: str):
    """
    Retrieves and scrapes tickets from Monterrey.
    :param plate: plate to search for.
    :return: a ticket dictionary with the details.
    """
    x = None
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "upgrade-insecure-requests": "1",
        "cache-control": "max-age=0",
    }
    token = ""
    while x is None:
        # bypass = bypass2(page=url, header=headers, logging=False)
        # bypass = sucuri_bypass(url)
        # x = requests.get(url, cookies=bypass)

        try:
            x = requests.get(MONTERREY_ASP_ENDPOINT)
        except requests.exceptions.ConnectionError:
            time.sleep(1)

        try:
            try:
                token = BeautifulSoup(x.text, "html.parser").find(
                "input", {"name": "__RequestVerificationToken"}
                )["value"]
            except AttributeError:
                print("Error when getting token!")
                return None
        except TypeError:
            print("Type Error In Verification Token!")
            x = None
    x_cookies = x.cookies

    d = {"__RequestVerificationToken": token, "placa": plate}

    x = requests.post(
        MONTERREY_ASP_ENDPOINT, headers=headers, cookies=x_cookies, data=d
    )

    soup = BeautifulSoup(x.text, "html.parser")

    verify_if_contains_form = soup.find_all("form")

    if len(verify_if_contains_form) > 0:
        resultsA = (
            verify_if_contains_form[0]
            .find_all("table")[1]
            .find_all("tbody")[0]
            .find_all("tr")
        )

        multas = []
        for tx in resultsA:
            multa = {"municipio": "MTY"}

            next_td = tx.find_next("td")
            multa["boleta"] = next_td.text.strip()

            next_td = next_td.find_next("td")
            multa["placa"] = next_td.text.strip()

            next_td = next_td.find_next("td")
            multa["fecha"] = next_td.text.strip()

            next_td = next_td.find_next("td")
            multa["infraccion"] = next_td.text.strip()

            next_td = next_td.find_next("td")
            multa["crucero"] = next_td.text.strip()

            next_td = next_td.find_next("td")
            multa["descuento"] = next_td.text.strip()

            next_td = next_td.find_next("td")
            multa["monto"] = next_td.text.strip()

            # Replacement + data cleaning for the ticket elements.
            multa["monto"] = multa["monto"].replace("$", "")
            multa["monto"] = multa["monto"].replace(",", "")
            multa["descuento"] = multa["descuento"].replace(",", "")
            multa["descuento"] = multa["descuento"].replace("$", "")

            try:
                multa["fecha"] = datetime.strptime(multa["fecha"], "%d/%m/%Y")
            except ValueError:
                multa["fecha"] = datetime.strptime("1/1/1980", "%d/%m/%Y")

            multas.append(multa)
        return multas
    return None


def get_san_nicolas_tickets_for_plate(plate: str):
    pass


def get_guadalupe_tickets_for_plate(plate: str):
    pass


################################################
###############  CODE GRAVEYARD  ###############
################################################

# Helpers

"""
def sucuri_bypass(url):
    res = requests.get(
        url, headers={"user-agent": "Mozilla/5.0 Chrome/96.0.4664.45 Safari/537.36"}
    )
    scr = re.findall("<script>([\s\S]*?)<\/script>", res.text, re.MULTILINE)[0]
    a = scr.split("(r)")[0][:-1] + "r=r.replace('document.cookie','var cookie');"

    b = js2py.eval_js(a)

    sucuri_cloudproxy_cookie = js2py.eval_js(
        b.replace("location.", "").replace("reload();", "")
    )
    cookies = {
        sucuri_cloudproxy_cookie.split("=")[0]: sucuri_cloudproxy_cookie.split("=")[
            1
        ].replace(";path", "")
    }

    return cookies


def bypass2(page, header, logging):
    if logging:
        print("Requesting Home Page without cookies")
    req = requests.get(page, headers=header)
    if logging:
        print("Parsing Sucuri Script...")
    soup = BeautifulSoup(req.text, "html.parser")
    script = soup.find("script")
    scr = script.text
    a = scr.split("(r)")[0][:-1] + "r=r.replace('document.cookie','var cookie');"
    if logging:
        print("Extracted internal script")
    b = js2py.eval_js(a)
    if logging:
        print("Getting cookies")
    sucuri_cloudproxy_cookie = js2py.eval_js(
        b.replace("location.", "").replace("reload();", "")
    )
    cookies = {
        sucuri_cloudproxy_cookie.split("=")[0]: sucuri_cloudproxy_cookie.split("=")[
            1
        ].replace(";path", "")
    }
    return cookies

"""
