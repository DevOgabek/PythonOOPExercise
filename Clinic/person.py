class Person:
    def __init__(self, name, surname, ssn):
        self.name = name
        self.surname = surname
        self.ssn = ssn
        self.doctor = None

    def getDoctor(self):
        return self.doctor