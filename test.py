from my_functions import estimate_max_hr

from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Walter", "Fürst")
    subject = Subject("Heinz", "Blatt", "male", 42)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2025-04-03", "Walter Fürst")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)