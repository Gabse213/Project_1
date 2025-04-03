from my_functions import estimate_max_hr
class Subject():

    def __init__(self, first_name, last, sex, age):
        self.first_name = first_name
        self.last = last
        self.sex = sex
        self.age = age
    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      pass

class Supervisor():
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last = last_name

class Experiment():
    def __init__(self,title, date, supervisor):
      self.title = title
      self.date = date
      self.supervisor = supervisor

    def add_subject(self, subject):
      self.add_subject = subject

    def add_supervisor(self, supervisor):
      self.add_supervisor= supervisor

    def __str__(self):
        return f"Experiment: {self.title}, Date: {self.date}, Supervisor: {self.supervisor}"