
class scheduler:
    def __init__(self, name,materia_list):
        self.__name = name
        self.__materia_list = materia_list
    def _comput_DifficultySum(self):
        sum_difficulty = 0
        for materia in self.__materia_list:
            difficulty = materia["difficulty"] * materia["difficulty"]
            sum_difficulty += difficulty
        return sum_difficulty
    def Create_schedule(self):
        schedule = []
        sum_difficulty = self._comput_DifficultySum()
        for materia in self.__materia_list:
            time_per_materia = (materia["hours_per_day"] * materia["days_to_exam"]) * ((materia["difficulty"] * materia["difficulty"] )/sum_difficulty )
            schedule.append({"name": materia["name"], "time_per_materia": round(time_per_materia)})
        return schedule