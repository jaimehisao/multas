"""
Predicting the validity of a plate number based on the neighbor plaes. If a neighbor plate
has a ticket (-7/+7), then the plate is considered valid but with no tickets, so it's status
is updated as to give it preference when checking the plates periodically.
"""
import logging
from database import is_plate_found, mark_plate_as_candidate, get_plate_queue
from constants import CANDIDATE_PLATES_AFTER_POSITIVE_MATCH as CANDIDATE_NUMBER


def next_plate_validity(plates: []) -> None:
    """
    Checks the validity of the neighbor plates of the plates in the database.
    If the plate has a ticket, then the next plates are presumed valid and thus
    marked as candidates.
    :param plates: List of plates to check their validity
    :return: None
    """
    index = 0
    non_tuple_plates = [item[0] for item in plates]
    for plate in non_tuple_plates:
        is_found = is_plate_found(plate)
        if len(is_found) > 0:
            if bool(is_found[0][0]) or bool(is_found[0][1]):
                next_twenty = non_tuple_plates[index + 1: index + CANDIDATE_NUMBER]
                logging.info("New candidate plates", str(next_twenty), "originally", plate)
                for plate_tw in next_twenty:
                    mark_plate_as_candidate(plate_tw)
        index += 1

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


def retrieve_plate_queue_and_check_validity_of_neighbhors():
    """
    Checks the validity of the neighbor plates of the plates in the database
    Storing all plates in memory, as to operate faster. Top of 7.5M records.
    Will live generate plates in order.
    :return: None
    """
    plates = get_plate_queue()
    next_plate_validity(plates)
