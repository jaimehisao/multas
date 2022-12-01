from scraper import get_tickets_for_plate
from database import add_plate_if_non_existent, add_new_tickets, mark_plate_as_found
from plates import generate_plates, generate_s_style_plates, generate_truck_plates


""" 
s_plates = generate_s_style_plates()
r_plates = generate_plates()
plates = s_plates + r_plates
plates_ = ["RPG003A"]
"""


plates_truck = generate_truck_plates()

for plate in plates_truck:
    print("Getting tickets for plate: " + plate)
    exists = add_plate_if_non_existent(plate)
    if not exists:
        tickets = get_tickets_for_plate(plate)
        if len(tickets) > 0:
            add_new_tickets(plate, tickets)
            mark_plate_as_found(plate)
            print("Added", len(tickets), "tickets for plate: " + plate)
        else:
            print("No new tickets for plate: " + plate)
    else:
        print("Plate already exists (skipping for now): " + plate)
    print("--------------------------------------------------")
