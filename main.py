from scraper import get_tickets_for_plate
from database import add_plate_if_non_existent, add_new_tickets, mark_plate_as_found, get_stored_plates
from plates import generate_plates, generate_s_style_plates, generate_truck_plates, r_plates_2, plates_and_query, look_for_spgg_plates_in_mty
import random
""" 
plates_ = ["RPG003A"]
"""


def main():
    look_for_spgg_plates_in_mty()
    plates_and_query()

    """
    s_plates = generate_s_style_plates()
    r_plates = generate_plates()
    plates_truck = generate_truck_plates()
    plates = s_plates + r_plates + plates_truck

    print("Generated plates", len(plates))

    #plates = r_plates_2()
    random.shuffle(plates)

    for plate in plates:
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
    """

    """
        while plates:
        plate = plates.pop()
        print("Getting tickets for plate: " + plate)
        if not add_plate_if_non_existent(plate):
            tickets = get_tickets_for_plate(plate)
            if len(tickets) > 0:
                add_new_tickets(plate, tickets)
                mark_plate_as_found(plate)
                print("Added", len(tickets), "tickets for plate: " + plate)
            else:
                print("No new tickets for plate: " + plate)
        else:
            print("Plate already in database: " + plate)
        print("Remaining plates: " + str(len(plates)))
        print("--------------------------------------------------")
    """


if __name__ == '__main__':
    main()
