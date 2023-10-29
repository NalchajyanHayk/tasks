import re

class Validations:
    @staticmethod
    def is_valid_name(name):
        pattern = r"^[A-Za-z -']+$"
        return bool(re.match(pattern, name))

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def is_valid_phone_number(phone_number):
        pattern = r"[0-9]\d{1,14}$"
        return bool(re.match(pattern, phone_number))

    @staticmethod
    def is_valid_address(address):
        pattern = r"^[A-Za-z0-9.,# -]+$"
        return bool(re.match(pattern, address))

    @staticmethod
    def count_digits_and_check(string, expected_count):
        digit_pattern = r'\d'
        digits = re.findall(digit_pattern, string)
        return len(digits) == expected_count

    @staticmethod
    def checking_account(account):
        types = ["savings", "checking"]
        if account.lower() not in types:
            return False
        else:
            return True

    @staticmethod
    def type_checking(obj, given_type):
        return type(obj) == given_type

    @staticmethod
    def transaction_checking(trans):
        types = ["internal", "external", "cash", "non-cash"]
        if trans.lower() in types:
            return True
        else:
            return False

    @staticmethod
    def car_make_valid(make):
        makes = ["BMW", "Porsche", "Opel"]
        return make.lower() in makes

    @staticmethod
    def model_valid(make):
        makes = ["truck", "sedan", "crossover"]
        return make in makes

    @staticmethod
    def is_positive_number(value):
        return isinstance(value, (int, float)) and value > 0

    @staticmethod
    def is_valid_age(age):
        return 0 < age < 150

    @staticmethod
    def game_genres(genre):
        genres = ["action", "strategy"]
        return genre in genres

    @staticmethod
    def is_valid_date(date):
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        return bool(re.match(date_pattern, date))

    @staticmethod
    def has_more_than_10_words(text):
        word_pattern = r'\b\w+\b'
        words = re.findall(word_pattern, text)
        return len(words) > 2