import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    user=DB_USER,
    password=DB_PASSWORD,
    host="databases.prod.hisao.org",
    port="5432",
    database="multas",
)

cursor = conn.cursor()


def is_plate_found(plate):
    cursor.execute("SELECT found, found_mty FROM plates WHERE plate = %s", (plate,))
    return cursor.fetchall()


def mark_plate_as_candidate(plate):
    cursor.execute("UPDATE plate_queue SET candidate = true WHERE plate = %s", (plate,))
    conn.commit()


def get_plate_queue() -> list:
    """
    Gets the plate queue from the database
    :return: List of plates in the queue
    """
    cursor.execute("SELECT plate FROM plate_queue")
    return cursor.fetchall()


def add_plates_to_db_queue(plates: []) -> None:
    """
    Adds plates to the database queue
    :param plates: List of plates to add
    :return: None
    """
    for plate in plates:
        cursor.execute("SELECT * FROM plate_queue WHERE plate = %s", (plate,))
        if len(cursor.fetchall()) == 0:
            print("Adding plate to queue: " + plate)
            cursor.execute("INSERT INTO plate_queue(plate) VALUES (%s)", (plate,))
            conn.commit()



def get_stored_plates() -> list:
    """
    Gets all stored plates from the database
    :return: List of plates
    """
    cursor.execute("SELECT plate FROM plates")
    return cursor.fetchall()


def mark_as_found_mty(plate):
    cursor.execute("UPDATE plates SET found_mty = true WHERE plate = %s", (plate,))
    conn.commit()


def get_found_mty_plates():
    cursor.execute("SELECT plate FROM plates WHERE found_mty = true")
    return cursor.fetchall()


def add_ticket_mty(plate, tickets):
    for tix in tickets:
        cursor.execute(
            "SELECT * FROM tickets WHERE ticket_number = %s", (tix["boleta"],)
        )
        if len(cursor.fetchall()) == 0:
            cursor.execute(
                "INSERT INTO tickets(municipality, ticket_number, date, ticket_type, crossing, discount, total, plate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    tix["municipio"],
                    tix["boleta"],
                    tix["fecha"],
                    tix["infraccion"],
                    tix["crucero"],
                    tix["descuento"],
                    tix["monto"],
                    plate,
                ),
            )
            conn.commit()


def get_found_plates():
    cursor.execute("SELECT plate FROM plates WHERE found = true")
    return cursor.fetchall()


def add_plate_if_non_existent(plate: str) -> bool:
    """
    Adds a plate to the database if non existent
    :param plate: Plate to add
    :return: None
    """
    cursor.execute("SELECT * FROM plates WHERE plate = %s", (plate,))
    if len(cursor.fetchall()) == 0:
        cursor.execute("INSERT INTO plates(plate) VALUES (%s)", (plate,))
        conn.commit()
        return False
    return True


def mark_plate_as_found(plate: str) -> None:
    """
    Marks a plate as found
    :param plate: Plate to mark
    :return: None
    """
    cursor.execute("UPDATE plates SET found = true WHERE plate = %s", (plate,))
    conn.commit()


def add_new_tickets(plate: str, tickets: list) -> None:
    """
    Adds new tickets to the database
    :param tickets: List of tickets to add
    :return: None
    """
    for multa in tickets:
        cursor.execute(
            "SELECT * FROM tickets WHERE ticket_number = %s", (multa["boleta"],)
        )
        if len(cursor.fetchall()) == 0:
            cursor.execute(
                "INSERT INTO tickets(municipality, ticket_number, date, ticket_type, crossing, value, discount, total, payment_date, reciept2, payed, balance, plate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    multa["municipio"],
                    multa["boleta"],
                    multa["fecha"],
                    multa["infraccion"],
                    multa["crucero"],
                    multa["valor"],
                    multa["descuento"],
                    multa["total"],
                    multa["fecha_pago"],
                    multa["recibo"],
                    multa["pagado"],
                    multa["saldo"],
                    plate,
                ),
            )
            conn.commit()
