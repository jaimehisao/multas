from database import (
    add_plate_if_non_existent,
    add_new_spgg_tickets,
    mark_plate_as_found,
    mark_as_found_mty,
    update_last_retrieved_to_right_now,
    add_ticket_mty,
    get_found_plates_and_last_query_time,
    remove_candidate,
    mark_candidate_last_checked_date_spgg,
    update_last_retrieved_to_right_now_spgg,
    mark_candidate_last_checked_date_mty,
    update_last_retrieved_to_right_now_mty,
    get_spgg_candidates,
    get_candidates_mty, get_found_spgg_plates, get_found_mty_plates,
)
from scraper import get_san_pedro_tickets_for_plate, get_monterrey_tickets_for_plate
import datetime as dt
import random
from constants import QUERY_COOLDOWN_DAYS

# TODO add a function to update tickets, like payment date


def query_previously_found_plates():
    """
    Query previously found plates and check them against SPGG and MTY databases.
    Plates would be ordered by when they were found, and queried like that.
    :return: None
    """
    current_time = dt.datetime.now()
    found_plates = list(get_found_plates_and_last_query_time())

    for plate in found_plates:
        # Doing San Pedro plates first
        if current_time - plate[1] > dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            san_pedro_tickets = get_san_pedro_tickets_for_plate(plate[0])
            if len(san_pedro_tickets) > 0:
                add_plate_if_non_existent(plate[0])
                add_new_spgg_tickets(plate[0], san_pedro_tickets)
                mark_plate_as_found(plate[0])

            # Doing Monterrey plates
            monterrey_tickets = get_monterrey_tickets_for_plate(plate[0])
            if len(monterrey_tickets) > 0:
                add_plate_if_non_existent(plate[0])
                add_ticket_mty(plate[0], monterrey_tickets)
                mark_as_found_mty(plate[0])

            update_last_retrieved_to_right_now(plate[0])


#####################################
### UPDATING ALREADY FOUND PLATES ###
#####################################

def update_spgg_plates():
    index = 0
    previously_found_plates = list(get_found_spgg_plates())
    len_prev = len(previously_found_plates)

    for plate in previously_found_plates:
        if plate[1] > dt.datetime.now() - dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            index += 1

    for plate in previously_found_plates:
        if dt.datetime.now() - plate[1] > dt.timedelta(days=QUERY_COOLDOWN_DAYS):  ## TODO CHECK IF RIGHT PARAM FROM QUERY
            print("Updating plate:", plate[0])
            san_pedro_tickets = get_san_pedro_tickets_for_plate(plate[0])
            if len(san_pedro_tickets) > 0:  # COULD UPDATE TIX HERE TODO
                add_new_spgg_tickets(plate[0], san_pedro_tickets)
                update_last_retrieved_to_right_now_spgg(plate[0])
        index += 1

    if index % 500 == 0:
        print(
            "Progress: ",
            index,
            "/",
            len_prev,
            "(",
            round(index / len_prev * 100, 2),
            "%)",
        )


def update_mty_plates():
    index = 0
    previously_found_plates = list(get_found_mty_plates())
    len_prev = len(previously_found_plates)

    for plate in previously_found_plates:
        if plate[1] > dt.datetime.now() - dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            index += 1

    for plate in previously_found_plates:
        if dt.datetime.now() - plate[1] > dt.timedelta(days=QUERY_COOLDOWN_DAYS):  ## TODO CHECK IF RIGHT PARAM FROM QUERY
            print("Updating plate:", plate[0])
            mty_tickets = get_monterrey_tickets_for_plate(plate[0])
            if len(mty_tickets) > 0:  # COULD UPDATE TIX HERE TODO
                add_ticket_mty(plate[0], mty_tickets)
                update_last_retrieved_to_right_now_mty(plate[0])
        index += 1

    if index % 500 == 0:
        print(
            "Progress: ",
            index,
            "/",
            len_prev,
            "(",
            round(index / len_prev * 100, 2),
            "%)",
        )

########################
### CANDIDATE PLATES ###
########################


def query_candidate_plates_mty():
    candidate_mty_plates = get_candidates_mty()
    candidate_mty_plates = list(candidate_mty_plates)
    len_candidate_mty_plates = len(candidate_mty_plates)
    index = 0

    random.shuffle(candidate_mty_plates)

    for plate in candidate_mty_plates:
        if plate[1] > dt.datetime.now() - dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            index += 1

    print(
        "Progress: ",
        index,
        "/",
        len_candidate_mty_plates,
        "(",
        round(index / len_candidate_mty_plates * 100, 2),
        "%)",
    )

    for plate in candidate_mty_plates:
        if plate[1] < dt.datetime.now() - dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            print(
                "Checking candidate plate: "
                + plate[0]
                + " ("
                + str(index)
                + "/"
                + str(len_candidate_mty_plates)
                + ")"
            )
            # Doing Monterrey plates
            monterrey_tickets = get_monterrey_tickets_for_plate(plate[0])
            if monterrey_tickets is not None:
                if len(monterrey_tickets) > 0:
                    add_plate_if_non_existent(plate[0])
                    add_ticket_mty(plate[0], monterrey_tickets)
                    mark_as_found_mty(plate[0])
                    remove_candidate(plate[0])

                mark_candidate_last_checked_date_mty(plate[0])
                update_last_retrieved_to_right_now_mty(plate[0])

                index += 1
        if index % 500 == 0:
            print(
                "Progress: ",
                index,
                "/",
                len_candidate_mty_plates,
                "(",
                round(index / len_candidate_mty_plates * 100, 2),
                "%)",
            )


def query_candidate_spgg_plates():
    candidate_spgg_plates = list(get_spgg_candidates())
    random.shuffle(candidate_spgg_plates)
    len_candidate_spgg_plates = len(candidate_spgg_plates)
    index = 0

    for plate in candidate_spgg_plates:
        if plate[1] > dt.datetime.now() - dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            index += 1

    print(
        "Progress: ",
        index,
        "/",
        len_candidate_spgg_plates,
        "(",
        round(index / len_candidate_spgg_plates * 100, 2),
        "%)",
    )

    # random.shuffle(candidate_spgg_plates)

    for plate in candidate_spgg_plates:
        if plate[1] < dt.datetime.now() - dt.timedelta(days=QUERY_COOLDOWN_DAYS):
            print(
                "Checking candidate plate: "
                + plate[0]
                + " ("
                + str(index)
                + "/"
                + str(len_candidate_spgg_plates)
                + ")"
            )
            # Doing San Pedro plates first
            san_pedro_tickets = get_san_pedro_tickets_for_plate(plate[0])
            if len(san_pedro_tickets) > 0:
                add_plate_if_non_existent(plate[0])
                add_new_spgg_tickets(plate[0], san_pedro_tickets)
                mark_plate_as_found(plate[0])
                remove_candidate(plate[0])

            mark_candidate_last_checked_date_spgg(plate[0])
            update_last_retrieved_to_right_now_spgg(plate[0])

            index += 1
        if index % 500 == 0:
            print(
                "Progress: ",
                index,
                "/",
                len_candidate_spgg_plates,
                "(",
                round(index / len_candidate_spgg_plates * 100, 2),
                "%)",
            )
