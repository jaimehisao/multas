import requests
from bs4 import BeautifulSoup


############################################################################
#### THIS IS PAUSED FOR THE MOMENT AS THERE IS NO CURRENT USE FOR THIS ####
############################################################################

def get_plate_account_statement(plate: str):
    url = "https://www.icvnl.gob.mx:1034/ICV_EDOCUENTA_SIRE/ConsultaEstadocuenta.aspx"

    d = {"placa": plate, "submit": "btnConsultar"}

    x = requests.post(url, data=d)

    print(x.text)


get_plate_account_statement("RPG003A")


