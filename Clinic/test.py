from clinic import Clinic, NoSuchPatient, NoSuchDoctor

# Test create_patient and get_patient
clinic = Clinic()
clinic.addPatient("Alice", "Johnson", "111-22-3333")
clinic.addPatient("Bob", "Williams", "444-55-6666")
patients = clinic.patients
print("Patients:", patients)
print("Patient Alice in patients:", clinic.getPatient("111-22-3333") in patients)
print("Patient Bob in patients:", clinic.getPatient("444-55-6666") in patients)

# Test create_doctor and get_doctor
clinic.addDoctor("John", "Doe", "123-45-6789", 1, "Cardiology")
clinic.addDoctor("Jane", "Smith", "987-65-4321", 2, "Dermatology")
doctors = clinic.doctors
print("Doctors:", doctors)
print("Doctor John in doctors:", clinic.getDoctor(1) in doctors)
print("Doctor Jane in doctors:", clinic.getDoctor(2) in doctors)

# Test assign_patient_to_doctor
clinic.assignPatientToDoctor("111-22-3333", 1)
clinic.assignPatientToDoctor("444-55-6666", 2)

# Test get_assigned_doctor and get_assigned_patients
assigned_doctor_alice = clinic.getPatient("111-22-3333").getDoctor()
assigned_doctor_bob = clinic.getPatient("444-55-6666").getDoctor()
print("Assigned doctor for Alice:", assigned_doctor_alice)
print("Assigned doctor for Bob:", assigned_doctor_bob)
print("Assigned patients for John:", [patient.ssn for patient in clinic.getDoctor(1).getPatients()])
print("Assigned patients for Jane:", [patient.ssn for patient in clinic.getDoctor(2).getPatients()])

# Test statistics
print("Idle Doctors:", [(doctor.surname, doctor.name) for doctor in clinic.idleDoctors()])
print("Busy Doctors:", [(doctor.surname, doctor.name) for doctor in clinic.busyDoctors()])
print("Doctors by Number of Patients:", clinic.doctorsByNumPatients())
print("Patients per Specialization:", clinic.countPatientsPerSpecialization())