import my_functions

def main():
    # Test: Personendaten erstellen
    person = my_functions.build_person("Simon", "Krainer", "male", 23)
    print("Personendaten:", person)

    # Test: Experiment erstellen
    experiment = my_functions.build_experiment("Herzfrequenz-Test", "2025-03-18", "Dr. Who", "Simon Krainer")
    print("Experiment:", experiment)

if __name__ == "__main__":
    main()

    from my_functions import estimate_max_hr, build_person, build_experiment, ask_name, ask_number, ask_sex

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    print("Leistungstest wird erstellt")
    print("Bitte geben Sie die Diagnostikerdaten ein:")

    print(" Geben Sie den Vornamen des Diagnostikers ein:")
    first_name = ask_name()
    print(" Geben Sie den Nachnamen des Diagnostikers ein:")    
    last_name = ask_name()

    supervisor = build_person(first_name, last_name, None, None)

    print("Bitte geben Sie die Probandendaten ein:")
    print(" Geben Sie den Vornamen des Probanden ein:")
    first_name = ask_name()
    print(" Geben Sie den Nachnamen des Probanden ein:")
    last_name = ask_name()
    print(" Geben Sie das Alter des Probanden ein:")
    age = ask_number()
    sex = ask_sex()
    # Erstellen einer Person
    subject = build_person(first_name, last_name, sex, age)

    # Erstellen eines Experiments
    experiment = build_experiment("Leistungstest", "2021-01-01", supervisor, subject)

    print("Das Experiment wurde erstellt:")
    print(experiment)
