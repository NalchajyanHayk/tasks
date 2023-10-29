from abc import ABC, abstractmethod
from validations import Validations

class HealthCareOperations(ABC):
    @abstractmethod
    def schedule_appointment(self, patient, appointment_time):
        pass

    @abstractmethod
    def view_medical_history(self, patient):
        pass

class Person(HealthCareOperations):
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self.name = name
        self.contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("Invalid name format.")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self._contact_info = value
        else:
            print("Invalid email format.")

    def schedule_appointment(self, patient, appointment_time):
        pass

    def view_medical_history(self, patient):
        pass

class Patient(Person):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)

    def schedule_appointment(self, doctor, appointment_time):
        appointment = InPersonAppointment(self, doctor, appointment_time)
        doctor.add_appointment(appointment)
        print(f"{self.name} has scheduled an appointment with Dr. {doctor.name} at {appointment_time}")

    def view_medical_history(self):
        print(f"Medical history for patient {self.name} is displayed here.")

class Doctor(Person):
    def __init__(self, name, contact_info, specialty):
        super().__init__(name, contact_info)
        self._specialty = None
        self.specialty = specialty
        self.appointments = []

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, value):
        if Validations.is_valid_name(value):
            self._specialty = value
        else:
            print("Invalid specialty format.")

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def schedule_appointment(self, patient, appointment_time):
        appointment = VirtualAppointment(self, patient, appointment_time)
        patient.schedule_appointment(self, appointment_time)
        self.add_appointment(appointment)
        print(f"Dr. {self.name} has scheduled a virtual appointment with {patient.name} at {appointment_time}")

    def view_medical_history(self, patient):
        patient.view_medical_history()

class Appointment(HealthCareOperations):
    def __init__(self, doctor, patient, appointment_time):
        self._doctor = doctor
        self._patient = patient
        self._appointment_time = appointment_time

    @property
    def doctor(self):
        return self._doctor

    @property
    def patient(self):
        return self._patient

    @property
    def appointment_time(self):
        return self._appointment_time

    def view_medical_history(self, patient):
        self.doctor.view_medical_history(patient)

class InPersonAppointment(Appointment):
    def schedule_appointment(self, patient, appointment_time):
        patient.schedule_appointment(self.doctor, appointment_time)

class VirtualAppointment(Appointment):
    def schedule_appointment(self, patient, appointment_time):
        patient.schedule_appointment(self.doctor, appointment_time)

# Example usage of the healthcare system:

# Create patients
patient1 = Patient("Alice", "ali@example.com")
patient2 = Patient("Bob", "bob@example.com")

# Create doctors
doctor1 = Doctor("Dr. Smith", "smith@example.com", "Cardiologist")
doctor2 = Doctor("Dr. Johnson", "johnson@example.com", "Dermatologist")

# Patients schedule appointments
patient1.schedule_appointment(doctor1, "2023-11-01 10:00 AM")
patient2.schedule_appointment(doctor2, "2023-11-02 2:00 PM")

# Doctors view patient medical history
doctor1.view_medical_history(patient1)
doctor2.view_medical_history(patient2)

