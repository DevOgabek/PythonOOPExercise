from person import Person

class Doctor(Person):
    def __init__(self, name, surname, ssn, doctor_id, specialization):
        super().__init__(name, surname, ssn)
        self.id = doctor_id
        self.specialization = specialization
        self.patients = []

    def getPatients(self):
        return self.patients