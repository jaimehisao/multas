"""
Predicting the validity of a plate number based on the neighbor plaes. If a neighbor plate
has a ticket (-20/+20), then the plate is considered valid but with no tickets, so it's status
is updated as to give it preference when checking the plates periodically.
"""

from database import get_plate_queue, is_plate_found, mark_plate_as_candidate
from plates import generate_plates, generate_truck_plates, generate_s_style_plates

CANDIDATE_NUMBER = 10 + 1


def next_plate_validity(plates):
    index = 0
    for plate in plates:
        is_found = is_plate_found(plate)
        if len(is_found) > 0:
            if bool(is_found[0][0]) or bool(is_found[0][1]):
                next_twenty = plates[index + 1: index + CANDIDATE_NUMBER]
                print("New candidate plates", str(next_twenty))
                for plate_tw in next_twenty:
                    mark_plate_as_candidate(plate_tw)
            index += 1


def see_if_neighbors_are_valid():
    """
    Checks the validity of the neighbor plates of the plates in the database
    Storing all plates in memory, as to operate faster. Top of 7.5M records.
    Will live generate plates in order.
    :return: None
    """
    # plates = get_plate_queue()

    s_plates = generate_s_style_plates()
    next_plate_validity(s_plates)
    r_plates = generate_plates()
    next_plate_validity(r_plates)
    plates_truck = generate_truck_plates()
    next_plate_validity(plates_truck)


see_if_neighbors_are_valid()

