# Our main function.
def main():
    k1, k2, k3 = fill()


# Creates the directories with the information provided in the text book.
# RECIVES: Nothing.
# RETURNES: Three directories.
# REQUIRES: Nothing.
def fill():
    k1 = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
    k2 = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    k3 = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.',
          'CM241': '1:00 p.m.'}
    return k1, k2, k3
