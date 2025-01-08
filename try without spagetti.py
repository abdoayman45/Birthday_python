import datetime
from os import name, system
from time import sleep

def cls():
    system('cls' if name == 'nt' else 'clear')

def pause(message="Click 'Enter' to continue..."):
    input(message)

def print_error(message):
    print(f"\nError: {message}\n")
    sleep(2)

class Person:
    def __init__(self, name, birthdate):
        self.name = name.capitalize()
        self.birthdate = birthdate
        self.age = self.calculate_age()
        self.birth_day = self.get_birth_day()

    def calculate_age(self):
        today = datetime.datetime.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def get_birth_day(self):
        return self.birthdate.strftime('%A')

    def was_born_on_sunday(self):
        return self.birth_day.lower() == 'sunday'

class BirthdayManager:
    def __init__(self):
        self.persons = []

    def add_person(self):
        while True:
            cls()
            print("Add a New Person:")
            user_input = input("Enter name and date (Name, dd-mm-yyyy): ").strip()
            try:
                name, date_str = map(str.strip, user_input.split(','))
                birthdate = datetime.datetime.strptime(date_str, '%d-%m-%Y')

                if birthdate > datetime.datetime.today():
                    print_error("The birthdate cannot be in the future.")
                    continue

                new_person = Person(name, birthdate)
                self.persons.append(new_person)
                print("\nPerson added successfully!\n")

                if input("Add another? (Y/N): ").strip().lower() == 'n':
                    break
            except ValueError:
                print_error("Invalid input. Please enter in the format: Name, dd-mm-yyyy")

    def delete_person(self):
        while True:
            cls()
            if not self.persons:
                print("No persons to delete.")
                pause()
                return

            print("Delete a Person:")
            search_name = input("Enter the name to delete: ").strip().capitalize()

            matches = [p for p in self.persons if search_name in p.name]
            if not matches:
                print_error("No matching persons found.")
                continue

            for idx, person in enumerate(matches, start=1):
                print(f"{idx}) {person.name}, born on {person.birthdate.strftime('%d-%m-%Y')} ({person.birth_day}), {person.age} years old.")

            try:
                choice = int(input("Select the number of the person to delete: ").strip()) - 1
                if 0 <= choice < len(matches):
                    self.persons.remove(matches[choice])
                    print("\nPerson deleted successfully!")
                else:
                    print_error("Invalid selection.")
            except ValueError:
                print_error("Please enter a valid number.")

            if input("Delete another? (Y/N): ").strip().lower() == 'n':
                break

    def display_persons(self):
        cls()
        if not self.persons:
            print("No persons to display.")
            pause()
            return

        print("List of Persons:")
        for person in self.persons:
            print(f"- {person.name} is {person.age} years old, born on {person.birth_day} ({person.birthdate.strftime('%d-%m-%Y')}).")
        pause()

    def display_oldest_and_youngest(self):
        cls()
        if not self.persons:
            print("No persons to analyze.")
            pause()
            return

        oldest_age = max(p.age for p in self.persons)
        youngest_age = min(p.age for p in self.persons)

        oldest = [p.name for p in self.persons if p.age == oldest_age]
        youngest = [p.name for p in self.persons if p.age == youngest_age]

        print("Oldest Persons:")
        print("\n".join(oldest))

        print("\nYoungest Persons:")
        print("\n".join(youngest))

        pause()

    def display_born_on_sunday(self):
        cls()
        sunday_people = [p.name for p in self.persons if p.was_born_on_sunday()]

        if sunday_people:
            print("Persons born on Sunday:")
            print("\n".join(sunday_people))
        else:
            print("No persons were born on Sunday.")

        pause()

    def main_menu(self):
        while True:
            cls()
            print("Birthday Manager:")
            print("1. Add Person")
            print("2. Delete Person")
            print("3. Display Persons")
            print("4. Display Oldest and Youngest")
            print("5. Display Born on Sunday")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_person()
            elif choice == '2':
                self.delete_person()
            elif choice == '3':
                self.display_persons()
            elif choice == '4':
                self.display_oldest_and_youngest()
            elif choice == '5':
                self.display_born_on_sunday()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = BirthdayManager()
    manager.main_menu()
