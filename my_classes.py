from my_functions import estimate_max_hr

class Person: 
  def __init__(self,first_name, last_name,):
      self.first_name = first_name
      self.last_name = last_name 

class Subject(Person):
  def __init__(self,first_name,last_name, sex, age):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.age = age
        self.estimate_max_hr =  estimate_max_hr(age, sex)
  def __str__(self):
    return f"Subject: {self.first_name} {self.last_name}, Sex: {self.sex}, Age: {self.age}, Max HR: {self.estimate_max_hr}"       

class Supervisor(Person):
  def __init__(self,first_name,last_name, rank):
      super().__init__(first_name, last_name)  
      self.rank=rank
  def __str__(self):
      return f"Supervisor: {self.first_name} {self.last_name}, Rank: {self.rank}"

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