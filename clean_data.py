from database import (
    clean_parking_meter_tickets,
    clean_prohibited_parking_space_tickets,
    other_cleanups,
)


# Could probably clean up into one single command and/or abstract from DB class.
clean_parking_meter_tickets()
clean_prohibited_parking_space_tickets()
other_cleanups()
print("Data cleaned!")
