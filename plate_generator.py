from database import add_plates_to_db_queue
import random


def generate_r_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("R" + letter + letter2 + str(i).zfill(3) + "A")
    return plates


def generate_s_style_plates():
    plates = []

    # SNN ## ## style plates
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(10000):
                plates.append("S" + letter + letter2 + str(i).zfill(4))

    # SNN ### A style plates
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("S" + letter + letter2 + str(i).zfill(3) + "A")
    return plates


def generate_truck_plates():
    plates_r = []
    plates_p = []
    plates_p_a = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for i in range(1000):
            plates_r.append("R" + letter + str(i).zfill(5))
            plates_p.append("P" + letter + str(i).zfill(5))
            plates_p_a.append("P" + letter + str(i).zfill(4) + "A")
    return plates_r + plates_p + plates_p_a


def generate_t_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("T" + letter + letter2 + str(i).zfill(3) + "B")
    return plates


#### NOT ACTUALLY HOW IT WORKS, JUST TO HAVE IT
def generate_green_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("G" + letter + letter2 + str(i).zfill(3) + "A")
    return plates


# Generate handicap plates


def generate_all_plates():
    # Generate all plates from different styles
    # r_plates = generate_r_style_plates()
    # truck_plates = generate_truck_plates()
    # s_plates = generate_s_style_plates()
    plates = t_plates = generate_t_style_plates()
    # plates = s_plates + truck_plates + r_plates + t_plates
    print("Generated " + str(len(plates)) + " plates")
    random.shuffle(plates)
    print("Shuffled plates")
    add_plates_to_db_queue(plates)
    print("Added plates to database")
