# Project_1
Software Engineering

## UC 1.03 (Alarm bei zu hoher Herzfrequenz)
### Name und Identifikationsnummer
UC 1.03(Alarm bei zu hoher Herzfrequenz)

### Beschreibung bei Auslösung
Wenn die Herzfrequenz den einstellbaren Bereich überschreiten sollte, wird über ein seitliches Pop-up Fenster und ein akustisches Warnsignal ein alarm ausgegeben und in den Daten vermerkt

### Beteiligte Akteure
Diagnostiker und Proband:in

## Aufgabe ULM-Diagramm
```mermaid
classDiagram
direction TB
    class Person {
	    +String name
	    +String telephone
	    +String email
    }

    class Address {
	    +String street
	    +String city
	    +String postalCode
	    +String country
	    +confirm()
	    +printLabel()
    }

    class Student {
	    +String studentNumber
	    +float averageGrade
	    +enrollModule()
    }

    class Professor {
	    +String teaches
	    +float salary
    }

    Person <|-- Student
    Person <|-- Professor
    Person "0..1" --> "1..*" Address : lives at
