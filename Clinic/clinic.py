from doctor import Doctor
from person import Person

class NoSuchPatient(Exception):
    pass

class NoSuchDoctor(Exception):
    pass

class Clinic:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def addPatient(self, name, surname, ssn):
        patient = Person(name, surname, ssn)
        self.patients.append(patient)

    def getPatient(self, ssn):
        for patient in self.patients:
            if patient.ssn == ssn:
                return patient
        raise NoSuchPatient("Patient not found.")

    def addDoctor(self, name, surname, ssn, doctor_id, specialization):
        doctor = Doctor(name, surname, ssn, doctor_id, specialization)
        self.doctors.append(doctor)

    def getDoctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise NoSuchDoctor("Doctor not found.")

    def assignPatientToDoctor(self, patient_ssn, doctor_id):
        try:
            patient = self.getPatient(patient_ssn)
            doctor = self.getDoctor(doctor_id)
            patient.doctor = doctor
            doctor.patients.append(patient)
        except NoSuchPatient as e:
            print(f"Error: {e}")
        except NoSuchDoctor as e:
            print(f"Error: {e}")

    def idleDoctors(self):
        return sorted([doctor for doctor in self.doctors if not doctor.getPatients()], key=lambda x: (x.surname, x.name))

    def busyDoctors(self):
        return sorted([doctor for doctor in self.doctors if doctor.getPatients()], key=lambda x: (x.surname, x.name))

    def doctorsByNumPatients(self):
        doctors_with_patients = sorted(self.doctors, key=lambda x: (len(x.getPatients()), x.surname, x.name), reverse=True)
        result = [f"{len(doctor.getPatients())}: {doctor.id} {doctor.surname} {doctor.name}" for doctor in doctors_with_patients]
        return result

    def countPatientsPerSpecialization(self):
        specialization_counts = {}
        for doctor in self.doctors:
            specialization = doctor.specialization
            if specialization in specialization_counts:
                specialization_counts[specialization] += len(doctor.getPatients())
            else:
                specialization_counts[specialization] = len(doctor.getPatients())

        result = [f"{count} - {specialization}" for specialization, count in sorted(specialization_counts.items())]
        return result