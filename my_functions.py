def estimate_max_hr(age_years : int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
  """
  if sex == "male":
    max_hr =  223 - 0.9 * age_years
  elif sex == "female":
    max_hr = 226 - 1.0 *  age_years
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr  = input("Enter maximum heart rate:")
  return int(max_hr)

def build_person(first_name, last_name, sex, age,max_hr) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    person_dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "sex" : sex,
             "max_hr" : max_hr
             }
    return person_dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    experiment_dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return experiment_dict

def ask_name() -> str:
    """Asks the user for their name."""
    try :
        name = input("What is your name? ")
        return name
    except Exception as e:
        print("Please enter a valid name")
        ask_name()

def ask_number() -> int:
    """Asks the user for a number."""
    try:
        number = int(input("Enter a number: "))
        return number
    except Exception as e:
        print("Please enter a valid number")
        ask_number()

def ask_sex() -> str:
    """Ask the user for the sex"""
    sex_string = input("Enter sex (w/m): ")
    if sex_string == "w":
        return "female"
    elif sex_string == "m":
        return "male"
    else:
        print("Please enter 'w' or 'm'")
        ask_sex()

def ask_date() -> str:
    while True:
        date_input = input("Geben Sie das Datum im Format TT.MM.JJJJ ein: ")
        try:
            datetime.strptime(date_input, "%d.%m.%Y")
            return date_input
        except ValueError:
            print("Ungültiges Datum. Bitte versuchen Sie es erneut.")

from datetime import datetime
def birthday(birthdate):
    birth_date = datetime.strptime(birthdate, "%d.%m.%Y")
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# Beispielnutzung
#Geburtstag = "09.04.1990"
# age = birthday(Geburtstag)
#print(f"Alter: {age} Jahre")