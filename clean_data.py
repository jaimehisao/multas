from database import cursor, conn


def clean_parking_meter_tickets():
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




### Switching to using a direct update statement instead of SELECT then UPDATE
"""
def clean_ticket_names():
    # Change ticket names to be more readable and consistent
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    for ticket in tickets:
        if ticket[4] == "No paga cuota parquimetro":
            cursor.execute(
                "UPDATE tickets SET ticket_type = %s WHERE ticket_number = %s", ## altough this might dupe it in some mty tickets, probs should check type first
                ("MULTA DE PARQUIMETROS", ticket[1]),
            )
            conn.commit()
"""
