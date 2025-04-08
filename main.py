from my_functions import estimate_max_hr, build_person, build_experiment, ask_name, ask_number, ask_sex ,birthday, ask_date

# Erstellen eines Leistungstests
print("Leistungstest wird erstellt")
print(" Geben Sie den Vornamen des Diagnostikers ein:")
first_name = ask_name()
print(" Geben Sie den Nachnamen des Diagnostikers ein:")    
last_name = ask_name()

supervisor = build_person(first_name, last_name, None, None, None )
print(" Geben Sie den Vornamen des Probanden ein:")
first_name = ask_name()
print(" Geben Sie den Nachnamen des Probanden ein:")
last_name = ask_name()
print(" Geben Sie den Geburtstag des Probanden ein:(TT.MM:JJJJ)")
birthdate=ask_date()
age = birthday(birthdate)
print(" Geben Sie das Geschlecht des Probanden ein:")
sex = ask_sex()
#print(sex)
#print(age)
#print(estimate_max_hr(30,"male"))
max_hr = estimate_max_hr(age,sex)
# Erstellen einer Person
subject = build_person(first_name, last_name, sex, age, max_hr)

# Erstellen eines Experiments
experiment = build_experiment("Leistungstest", "2025-04-08", supervisor, subject)

print("Das Experiment wurde erstellt:")
print(experiment)