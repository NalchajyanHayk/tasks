from validations import Validations
class Patient:
    def __init__(self, name, age, medical_history):
        self._name = name
        self._age = age
        self._medical_history = medical_history


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if Validations.is_valid_name(new_name):
            self._name = new_name
        else:
            raise ValueError("Invalid name format")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if Validations.is_valid_age(new_age):
            self._age = new_age
        else:
            raise ValueError("Invalid age format")

    @property
    def medical_history(self):
        return self._medical_history


class Doctor:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if Validations.is_valid_name(new_name):
            self._name = new_name
        else:
            raise ValueError("Invalid name format")

    @property
    def contact_info(self):
        return self._contact_info


class MedicalStaff:
    def __init__(self, name, position, contact_info):
        self._name = name
        self._position = position
        self._contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if Validations.is_valid_name(new_name):
            self._name = new_name
        else:
            raise ValueError("Invalid name format")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    @property
    def contact_info(self):
        return self._contact_info


# Instantiate a Patient
patient1 = Patient("John Doe", 35, "Allergies: Pollen, Medications: None")

# Instantiate a Doctor
doctor1 = Doctor("Dr. Smith", "Contact Info: DrSmith@example.com")

# Instantiate a Medical Staff
medical_staff1 = MedicalStaff("Nurse Johnson", "Registered Nurse", "Contact Info: NurseJohnson@example.com")

# Print patient information
print(f"Patient Name: {patient1.name}")
print(f"Patient Age: {patient1.age}")
print(f"Medical History: {patient1.medical_history}")

# Print doctor information
print(f"Doctor Name: {doctor1.name}")
print(f"Doctor Contact Info: {doctor1.contact_info}")

# Print medical staff information
print(f"Medical Staff Name: {medical_staff1.name}")
print(f"Position: {medical_staff1.position}")
print(f"Contact Info: {medical_staff1.contact_info}")
