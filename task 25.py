from validations import Validations
from abc import ABC, abstractmethod

class FitnessTrackingOperations(ABC):
    @abstractmethod
    def track_exercise(self, user, exercise, duration):
        pass

    @abstractmethod
    def create_workout_plan(self, user, exercises, plan_duration):
        pass

    @abstractmethod
    def follow_workout_plan(self, user, plan):
        pass

class Exercise:
    def __init__(self, name, muscle_group):
        self._name = None
        self._muscle_group = None
        self.name = name
        self.muscle_group = muscle_group

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
    def muscle_group(self):
        return self._muscle_group

    @muscle_group.setter
    def muscle_group(self, value):
        if Validations.is_valid_name(value):
            self._muscle_group = value
        else:
            print("Invalid muscle group format.")

class CardioExercise(Exercise):
    def __init__(self, name, duration, muscle_group):
        super().__init__(name, muscle_group)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if Validations.is_positive_number(value):
            self._duration = value
        else:
            print("Invalid duration format.")

class StrengthExercise(Exercise):
    def __init__(self, name, sets, reps, muscle_group):
        super().__init__(name, muscle_group)
        self._sets = None
        self._reps = None
        self.sets = sets
        self.reps = reps

    @property
    def sets(self):
        return self._sets

    @sets.setter
    def sets(self, value):
        if Validations.is_positive_number(value):
            self._sets = value
        else:
            print("Invalid sets format.")

    @property
    def reps(self):
        return self._reps

    @reps.setter
    def reps(self, value):
        if Validations.is_positive_number(value):
            self._reps = value
        else:
            print("Invalid reps format.")

class User:
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._favorite_exercises = []

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

    @property
    def favorite_exercises(self):
        return self._favorite_exercises

    def add_favorite_exercise(self, exercise):
        self._favorite_exercises.append(exercise)

class WorkoutPlan:
    def __init__(self, user, exercises, plan_duration):
        self._user = None
        self._exercises = None
        self._plan_duration = None
        self.user = user
        self.exercises = exercises
        self.plan_duration = plan_duration

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def exercises(self):
        return self._exercises

    @exercises.setter
    def exercises(self, value):
        self._exercises = value

    @property
    def plan_duration(self):
        return self._plan_duration

    @plan_duration.setter
    def plan_duration(self, value):
        if Validations.is_positive_number(value):
            self._plan_duration = value
        else:
            print("Invalid plan duration format.")

# Example usage:

cardio_exercise = CardioExercise("Running", 30, "Legs")
strength_exercise = StrengthExercise("Push-ups", 3, 15, "Chest")

user = User("John", "john@example.com")
user.add_favorite_exercise(cardio_exercise)
user.add_favorite_exercise(strength_exercise)

workout_plan = WorkoutPlan(user, [cardio_exercise, strength_exercise], 30)

print(f"{user.name}'s favorite exercises:")
for exercise in user.favorite_exercises:
    if isinstance(exercise, CardioExercise):
        print(f"Cardio: {exercise.name} ({exercise.duration} minutes)")
    elif isinstance(exercise, StrengthExercise):
        print(f"Strength: {exercise.name} ({exercise.sets} sets x {exercise.reps} reps)")

print(f"{user.name}'s workout plan:")
for exercise in workout_plan.exercises:
    if isinstance(exercise, CardioExercise):
        print(f"Cardio: {exercise.name} ({exercise.duration} minutes)")
    elif isinstance(exercise, StrengthExercise):
        print(f"Strength: {exercise.name} ({exercise.sets} sets x {exercise.reps} reps)")
print(f"Plan Duration: {workout_plan.plan_duration} days")
