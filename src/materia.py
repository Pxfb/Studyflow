class materia:
    def __init__(self, name, dificulty, time_to_exam, priority):
        self.__name = name
        self.__dificulty = dificulty
        self.__time_to_exam = time_to_exam
        self.__priority = priority
    
    def get_name(self):
        return self.__name
    
    def get_dificulty(self):
        return self.__dificulty
    
    def get_time_to_exam(self):
        return self.__time_to_exam
    
    def get_priority(self):
        return self.__priority