from my_functions import estimate_max_hr

from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Henry","Hansen","Boss")
    subject = Subject("Heinz", "Blatt", "male", 42)
    max_hr=estimate_max_hr(42,"m")

    experiment = Experiment("Leistungstest", "2025-04-03", supervisor)
    experiment.add_subject(subject)


    print(experiment)