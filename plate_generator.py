def generate_r_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("R" + letter + letter2 + str(i).zfill(3) + "A")
    return plates


def generate_s_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(10000):
                plates.append("S" + letter + letter2 + str(i).zfill(4))
    return plates


def generate_truck_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for i in range(1000):
            plates.append("R" + letter + str(i).zfill(5))
            plates.append("P" + letter + str(i).zfill(4) + "A")
    return plates


def generate_t_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("T" + letter + letter2 + str(i).zfill(3) + "B")
    return []


#### NOT ACTUALLY HOW IT WORKS, JUST TO HAVE IT
def generate_green_style_plates():
    plates = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(1000):
                plates.append("G" + letter + letter2 + str(i).zfill(3) + "A")
    return plates


def generate_all_plates():
    # Generate R style plates
    # R XXX NNN A
    r_plates = generate_r_style_plates()
    truck_plates = generate_truck_plates()
    s_plates = generate_s_style_plates()
    t_plates = generate_t_style_plates()
    plates = truck_plates + r_plates + s_plates + t_plates
    return plates
