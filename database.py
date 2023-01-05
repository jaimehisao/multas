import psycopg2
from dotenv import load_dotenv
import os
import datetime as dt
import logging

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

###################################
############ CLEANING ############
###################################
def clean_parking_meter_tickets():

    # Parking Meter
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'MULTA DE PARQUIMETROS' "
        "WHERE ticket_type = 'NO PAGAR CUOTA PARQUIMETRO'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'MULTA DE PARQUIMETROS' "
        "WHERE ticket_type = 'No paga cuota parquimetro'"
    )
    conn.commit()


"""
There is prpobably a way to make the cleanups look more elegant and it would involve splitting this into two files, 
then have one with only the before and after queries and then just have a single cursor and commit that iterate over
all the options doing execute and then only commit once at the end. Efficiency wise, it is not hurtful to commit 
often with this changes, as they happen every two minutes the impact of commiting after each statement is minimal 
but we will still try to optimize any run by our program.
"""


def clean_prohibited_parking_space_tickets():
    # Prohibited Parking Spaces
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO   , ART. 72 FRACC. III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XV, XVI, XVII, XX, X'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'ESTAC EN LUGAR PROHIBIDO'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'Est. En lugar Prohibido'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'ESTAC. LUGAR PROHIBIDO'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO   , ART. 72'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'ESTACIONARSE EN LUGAR PROHIBIDO   , ART. 72'"
    )
    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'CAMBIAR CARRIL SIN PRECAUCION' "
        "WHERE ticket_type = 'cambiar carr s/ prec'"
    )

    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'REBASAR EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'REBASAR EN LUGAR PROHIBID'"
    )

    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'SER RESPONSABLE EN HECHO DE TRÁNSITO' "
        "WHERE ticket_type = 'SER RESPONSABLE EN HECHO DE TRÁNSITO , ART. 137'"
    )

    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'CIRCULAR SIN LICENCIA O VENCIDA' "
        "WHERE ticket_type = 'circ. sin licencia o vencida'"
    )

    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'VOLTEAR A LA IZQUIERDA EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'VOLTEAR A LA IZQ EN LUGAR PROH'"
    )

    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'TRANSPORTAR PERSONAS EN LUGAR PROHIBIDO' "
        "WHERE ticket_type = 'TRANS.PERS.EN LUGAR PROH.'"
    )

    cursor.execute(
        "UPDATE tickets "
        "SET ticket_type = 'SUJETAR APARATOS DE COMUNICACION' "
        "WHERE ticket_type = 'SUJETAR APARATOS DE COMUNICACIÓN O APARATOS ELECTRÓNICOS , ART. 51, FRACC. II'"
    )

    conn.commit()


def other_cleanups():
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'MANEJAR CON LICENCIA VENCIDA' "
        "WHERE ticket_type = 'MANEJAR C/LIC.VENCIDA'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'CIRCULAR ZIGZAGUEANDO' "
        "WHERE ticket_type = 'CIRC. ZIGZAGUEANDO'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'INICIAR MARCHA SIN PRECAUCIÓN' "
        "WHERE ticket_type = 'INICIAR MARCHA SIN PRECAUCIÓN , ART. 49, FRACC. XV'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'MANEJAR LICENCIA NO ACORDE AL VEHICULO' "
        "WHERE ticket_type = 'MANEJAR LICEN.NO ACORDE AL VEH'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'NO CONTAR CON CINTURON DE SEGURIDAD' "
        "WHERE ticket_type = 'NO CONTAR CON CINTURON DE SEG.'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'INTERVENIR EN ASUNTOS DE TRANSITO' "
        "WHERE ticket_type = 'INTERVENIR EN ASUNTOS DE TRANS'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'ESTACIONARSE EN LUGAR EXCLUSIVO PARA DISCAPACITADOS' "
        "WHERE ticket_type = 'ESTACIONARSE EN LUGAR EXCLUSIVO PARA DISCAPACITADOS , ART. 72, FRACC. XVIII'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'EXCESO DE VELOCIDAD EN ZONA ESCOLAR' "
        "WHERE ticket_type = 'EXCESO DE VELOCIDAD EN ZONA ESCOLAR , ART. 52, FRACC. I'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'EXCESO DE VELOCIDAD' "
        "WHERE ticket_type = 'exceso de velocidad'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'TRASLADO DE LESIONADO CRUZ ROJA' "
        "WHERE ticket_type = 'TRASLADO DE LESIONADO C. ROJA'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'EXCESO DE VELOCIDAD EN ZONA URBANA' "
        "WHERE ticket_type = 'EXCESO DE VELOCIDAD Z. URBANA'"
    )
    cursor.execute(
        "UPDATE tickets SET ticket_type = 'EXCESO DE VELOCIDAD EN ZONA ESCOLAR' "
        "WHERE ticket_type = 'Exceso vel. Zona Escolar'"
    )
    conn.commit()


####### END OF CLEANING SECTION #######


############ UPDATES ############
def update_last_retrieved_to_right_now(plate: str) -> None:
    """
    Updates the last retrieved date
    :param plate: Plate to update
    :param date: Date to update to
    :return: None
    """
    ts = dt.datetime.now()
    cursor.execute(
        "UPDATE plates SET last_retrieved = %s WHERE plate = %s",
        (
            ts,
            plate,
        ),
    )
    conn.commit()


def update_last_retrieved_to_right_now_mty(plate: str) -> None:
    """
    Updates the last retrieved date
    :param plate: Plate to update
    :param date: Date to update to
    :return: None
    """
    ts = dt.datetime.now()
    cursor.execute(
        "UPDATE plates SET last_retrieved_mty = %s WHERE plate = %s",
        (
            ts,
            plate,
        ),
    )
    conn.commit()


def update_last_retrieved_to_right_now_spgg(plate: str) -> None:
    """
    Updates the last retrieved date
    :param plate: Plate to update
    :param date: Date to update to
    :return: None
    """
    current_timestamp = dt.datetime.now()
    cursor.execute(
        "UPDATE plates SET last_retrieved_spgg = %s WHERE plate = %s",
        (
            current_timestamp,
            plate,
        ),
    )
    conn.commit()


############ PLATE QUEUE & CANDIDATES ############
def get_plate_queue() -> list:
    """
    Gets the plate queue from the database
    :return: List of plates in the queue
    """
    cursor.execute("SELECT plate FROM plate_queue ORDER BY plate")
    return cursor.fetchall()


def remove_candidate(plate):
    cursor.execute("DELETE FROM plate_queue WHERE plate = %s", (plate,))
    conn.commit()


def mark_plate_as_candidate(plate):
    cursor.execute("SELECT found FROM plates WHERE plate = %s", (plate,))
    has_been_found = cursor.fetchall()
    if len(has_been_found) > 0:
        # If a plate has been found (len!=0), it is not a candidate, because it has already been searched.
        logging.info(
            "Plate has already been found, not marking as candidate and deleting from queue."
        )
        cursor.execute(
            "DELETE FROM plate_queue WHERE plate = %s", (plate,)
        )  # might break code if i run the script twice
        conn.commit()
    else:
        cursor.execute(
            "UPDATE plate_queue SET candidate = true WHERE plate = %s", (plate,)
        )
        cursor.execute(
            "UPDATE plate_queue SET last_checked_mty = %s WHERE plate = %s",
            (dt.datetime.strptime("2020/01/01", "%Y/%m/%d"), plate),
        )
        cursor.execute(
            "UPDATE plate_queue SET last_checked_spgg = %s WHERE plate = %s",
            (dt.datetime.strptime("2020/01/01", "%Y/%m/%d"), plate),
        )
        conn.commit()


def mark_plates_as_candidates(plate):
    for plate in plate:
        cursor.execute("UPDATE plates SET candidate = true WHERE plate = %s", (plate,))
    conn.commit()


def get_found_plates_in_order():
    cursor.execute(
        "SELECT plate FROM plates WHERE found = true or found_mty = true ORDER BY plate"
    )
    return cursor.fetchall()


######### temporary #########
def get_candidates_mty():
    cursor.execute(
        "SELECT plate, last_checked_mty "
        "FROM plate_queue "
        "WHERE candidate = true "
        "ORDER BY last_checked_mty"
    )
    return cursor.fetchall()


def get_spgg_candidates():
    cursor.execute(
        "SELECT plate, last_checked_spgg "
        "FROM plate_queue "
        "WHERE candidate = true "
        "ORDER BY last_checked_spgg"
    )
    return cursor.fetchall()


######### end temporary #########


def mark_candidate_last_checked_date_mty(plate):
    cursor.execute(
        "UPDATE plate_queue SET last_checked_mty = %s WHERE plate = %s",
        (dt.datetime.now(), plate),
    )
    conn.commit()


def mark_candidate_last_checked_date_spgg(plate):
    cursor.execute(
        "UPDATE plate_queue SET last_checked_spgg = %s WHERE plate = %s",
        (dt.datetime.now(), plate),
    )
    conn.commit()


def is_plate_found(plate):
    cursor.execute("SELECT found, found_mty FROM plates WHERE plate = %s", (plate,))
    return cursor.fetchall()


def add_plates_to_queue(plates: []) -> None:
    """
    Adds plates to the database queue.
    :param plates: List of plates to add
    :return: None
    """
    index = 0
    for plate in plates:
        # cursor.execute("SELECT * FROM plate_queue WHERE plate = %s", (plate,))
        if index % 1000 == 0:
            logging.info(
                "Current progress: "
                + str(index)
                + "/"
                + str(len(plates))
                + " plates ("
                + str(round(index / len(plates) * 100, 2))
                + "%)"
            )
            # conn.commit()
        # if len(cursor.fetchall()) == 0:
        cursor.execute(
            "INSERT INTO plate_queue(plate) VALUES (%s) ON CONFLICT DO NOTHING",
            (plate,),
        )
        index += 1
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
    for ticket in tickets:
        cursor.execute(
            "SELECT * FROM tickets WHERE ticket_number = %s and ticket_type = %s",
            (
                ticket["boleta"],
                ticket["infraccion"],
            ),
        )
        if len(cursor.fetchall()) == 0:
            cursor.execute(
                "INSERT INTO tickets(municipality, ticket_number, date, ticket_type, crossing, discount, total, plate) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    ticket["municipio"],
                    ticket["boleta"],
                    ticket["fecha"],
                    ticket["infraccion"],
                    ticket["crucero"],
                    ticket["descuento"],
                    ticket["monto"],
                    plate,
                ),
            )
            conn.commit()


def get_found_plates():
    cursor.execute("SELECT plate FROM plates WHERE found = true or found_mty = true")
    return cursor.fetchall()


def get_found_plates_and_last_query_time():
    cursor.execute(
        "SELECT plate, last_retrieved "
        "FROM plates "
        "WHERE found = true or found_mty = true"
    )
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


def add_new_spgg_tickets(plate: str, tickets: list) -> None:
    """
    Adds new tickets to the database
    :param tickets: List of tickets to add
    :return: None
    """
    # should check municipality
    for ticket in tickets:
        cursor.execute(
            "SELECT * FROM tickets WHERE ticket_number = %s", (ticket["boleta"],)
        )
        if len(cursor.fetchall()) == 0:
            cursor.execute(
                "INSERT INTO tickets(municipality, ticket_number, date, ticket_type, crossing, value, discount, total, "
                "payment_date, reciept2, payed, balance, plate) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    ticket["municipio"],
                    ticket["boleta"],
                    ticket["fecha"],
                    ticket["infraccion"],
                    ticket["crucero"],
                    ticket["valor"],
                    ticket["descuento"],
                    ticket["total"],
                    ticket["fecha_pago"],
                    ticket["recibo"],
                    ticket["pagado"],
                    ticket["saldo"],
                    plate,
                ),
            )
            conn.commit()
