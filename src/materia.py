class materia:
    def __init__(self, name, difficulty, hours_per_day, days_to_exam):
        self.__name = name
        self.__difficulty = difficulty
        self.__hours_per_day = hours_per_day
        self.__days_to_exam = days_to_exam
    
    def get_name(self):
        return self.__name
    
    def get_difficulty(self):
        return self.__difficulty
    
    def get_hours_per_day(self):
        return self.__hours_per_day
    
    def get_days_to_exam(self):
        return self.__days_to_exam