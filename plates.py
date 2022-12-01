import random


def generate_truck_plates():
    plates = []
    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    """
     for letter in letters:
        for i in range(25000):
            plates.append("R" + letter + str(i).zfill(5))
    """

    for i in range(10000):
        # TODO, then remove S
        plates.append("PS" + str(i).zfill(4) + "A")
    random.shuffle(plates)

    """
        for letter in letters:
            for i in range(100):
                plates.append("P" + letter + str(i).zfill(4) + "A")
    """
    return plates


def generate_s_style_plates():
    """Generate a list of plates.
    First digit is either S, R, or T.
    Last digit is a number when the first is an S, is A when the first is an R, and is a B when the first is a T.
    """
    plates = []
    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    # Four digit modification S**XXXX model
    for letter in letters:
        for letter2 in letters:
            for i in range(10000):
                plates.append("S" + letter + letter2 + str(i).zfill(4))
    random.shuffle(plates)
    return plates


def generate_plates():
    """Generate a list of plates.
    First digit is either S, R, or T.
    Last digit is a number when the first is an S, is A when the first is an R, and is a B when the first is a T.
    """
    initial = "RPG003A"
    plates = []
    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    # Three digit modification R**XXXA model
    if initial[0] == "R":
        for letter in letters:
            for letter2 in letters:
                for i in range(1000):
                    plates.append("R" + letter + letter2 + str(i).zfill(3) + "A")
    random.shuffle(plates)
    return plates
