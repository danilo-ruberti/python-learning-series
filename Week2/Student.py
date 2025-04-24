class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # list of numbers

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def is_passing(self):
        return self.average() >= 60

    def __str__(self):
        status = "Passing" if self.is_passing() else "Failing"
        return f"{self.name}: Avg = {self.average():.2f}, {status}"