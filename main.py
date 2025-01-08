from sys import exit
from os import name,system
from time import sleep
import datetime

def cls():
    system('cls' if name == 'nt' else 'clear')

class Birthday:
    def __init__(self):
        self.persons_list = []
        self.sunday_person = []
        self.oldest_persons = []
        self.youngest_persons = []
        self.the_date_today = datetime.datetime.today()

    def add_persons(self): 
        #was born on sunday?
        def was_born_on_sunday(day):
            if day == 'Sunday'.lower():
                return True
            else:
                return False
        
        while True:
            cls()
            print("Welcome In add part:\n")#The hello
            input_name_date = input("Enter The name and date (like: Name, dd-mm-yyyy) : ")
            name_date = input_name_date.split(',')

            if len(name_date) != 2:
                print("\nInvalid Input! Please Enter in this way : (Name, dd-mm-yyyy) .\n")
                sleep(3)

            else:
                if not name_date[0].strip().isalpha():
                    print("Invalid Name,Please write only letters.")
                    sleep(3)
                else:
                    try:
                        oked_date = datetime.datetime.strptime(name_date[1].strip() , '%d-%m-%Y')
                        if oked_date > self.the_date_today :
                            print("\nInvalid Date, Please Enter a Birthday .\n")
                            sleep(3)
                        else:
                            age = self.the_date_today.year - oked_date.year
                            if (self.the_date_today.month < oked_date.month) or (self.the_date_today.day < oked_date.day):
                                age -= 1
                            name_of_day = datetime.datetime.strftime(oked_date, '%A')
                            if was_born_on_sunday(name_of_day):
                                self.sunday_person.append(name_date[0].strip().capitalize())
                            
                            self.persons_list.append({
                                'name':name_date[0].strip().capitalize(),
                                'date':name_date[1].strip(),
                                'age':age,
                                'day':name_of_day,
                                'sunday':was_born_on_sunday(name_of_day)
                            })
                            print("\nAdded Successfully.\n")
                            if input("Do you want to add anther one ? (Y/N) : ").lower() == 'n':
                                cls()
                                self.show_the_msg()
                                self.youngest_and_oldest_persons()
                                input("Click Enter to back to main minu :")    
                                self.main_minu()
                            else:
                                continue
                    except ValueError:
                        print("\nInvalid date, Please Try again with a valid date.\n")
                        sleep(3)

    def delete_person(self):
        while True:
            cls()
            print("Welcome to delete part :\n")
            if self.persons_list:
                name = input ("Enter the name of the person : ").strip().capitalize()
                list_of_esist_persons = []
                list_of_number_of_index = []
                number_of_index = 0
                for i in self.persons_list:
                    if i['name'].find(name) != -1 :
                        number_of_index += 1
                        print("Searching ...")
                        sleep(1.5)
                        print("\nI Got It : ")
                        print(f"His Ditals:")
                        print('-'*25)
                        print(f"{number_of_index}) name : {i['name']}\nBirthday Date : {i['date']}\nHis Age : {i['age']}\nWas born on : {i['day']}")
                        print('-'*25,"\n")
                        list_of_esist_persons.append(i)
                        list_of_number_of_index.append(number_of_index)

                if list_of_esist_persons:
                    if len(list_of_esist_persons) == 1:
                        sure = input("Do you sure of this step? (Y/N) : ").lower()
                        while sure not in ("y","n"):
                            print("Plz Enter only (y for the ok) or (n for cancel).")
                            sure = input("Do you sure of this step? (Y/N) : ").lower()
                        if sure == 'y':
                            self.persons_list.remove(i)
                            print("\nDeleted successfully.\n")
                        elif sure == 'n':
                            print("\nThe precess of delete was canceld successfully.\n")
                    else:
                        choice = input("Enter The number of the Person you want to delete : ")

                        
                        while (int(choice) > len(list_of_esist_persons)) or (int(choice) <= 0) or (not choice.isdigit()) or (int(choice) not in list_of_number_of_index):
                            print("\nYou have to choice a number of the person from the list you see now .\n")
                            choice = input("Enter The number of the Person you want to delete : ")

                        choice_to_delete = list_of_esist_persons[(int(choice)-1)]

                        sure = input("Do you sure of this step? (Y/N) : ").lower()
                        while sure not in ("y","n"):
                            print("Plz Enter only (y for the ok) or (n for cancel).")
                            sure = input("Do you sure of this step? (Y/N) : ").lower()
                        if sure == 'y':
                            self.persons_list.remove(choice_to_delete)
                            print("\nDeleted successfully.\n")
                        elif sure == 'n':
                            print("\nThe precess of delete was canceld successfully.\n")

                        


                if not list_of_esist_persons:
                    print("Searching ...\n")
                    sleep(2.5)
                    print("I couldn't get it.")
                    print("You don't have a name like what you have written.\n")

                if input("Do you want to delete another one ? (Y/N) : ").lower() == 'n':
                    input("\nClick 'Enter' to back to main menu : ")
                    self.main_minu()        
            else:
                print("\nYou don't have anything to delete.\n")
                input("Click 'Enter' to back to main menu : ")
                self.main_minu()
                                            
    def show_the_msg(self):
        for n,i in enumerate(self.persons_list, start=1):
            print(f"{n}){i['name']} is {i['age']} years old and she/he was born on {i['day']}\n")
        
    def youngest_and_oldest_persons(self):
            if len(self.persons_list) == 1 :
                print("There is no oldest or youngest person.\n")
            else:
                self.oldest_persons=[]
                self.youngest_persons=[]
                def oldest():
                    maxi = max(i['age'] for i in self.persons_list)
                    for i in self.persons_list :
                        if i['age'] == maxi and i['name'] not in self.oldest_persons :
                            self.oldest_persons.append(i['name'])
                    all = '\n'.join(self.oldest_persons)
                    print(f"The Oldest :  \n{all}\n")

                def youngest():
                    mini = min(i['age'] for i in self.persons_list)
                    for i in self.persons_list :
                        if i['age'] == mini and i['name'] not in self.youngest_persons:
                            self.youngest_persons.append(i['name'])
                    all = '\n'.join(self.youngest_persons)
                    print(f"The Youngest :  \n{all}\n")
                oldest()
                youngest()

    def born_on_sunday(self):
        cls()
        print("Welcome to Sunday part:\n")
        if self.persons_list:
            if self.sunday_person:
                all = '\n'.join(self.sunday_person)
                print(f"All persons that were born on Sunday :\n{all}\n")
                input("Click 'Enter' to back to main menu : ")
                self.main_minu()
            else:
                print("You don't have anyone that born on Sunday.\n")
                input("Click 'Enter' to back to main menu : ")
                self.main_minu()
        print("You don't have anything yet.\n")
        input("Click 'Enter' to back to main menu : ")
        self.main_minu()
        

    def reverse_order_of_input(self):
        cls()
        print("Welcome to reverse input part:\n")
        if self.persons_list:
            reversed_list = []
            for i in range(len(self.persons_list)):
                i += 1
                i *= -1
                reversed_list.append(self.persons_list[i])

            print("The input reversed :\n")
            for i in reversed_list:
                print(f"{i['name']}, {i['date']}\n")
            input("Click 'Enter' to back to main menu : ")
            self.main_minu()

        else:
            print("You don't have anything yet.\n")
            input("Click 'Enter' to back to main menu : ")
            self.main_minu()

    def sort_from_oldest_to_youngest(self):
        cls()
        print("Welcome to sort part:\n")
        if self.persons_list:
            def filter_sorted(index):
                return index['age']
            sorted_list = sorted(self.persons_list,key=filter_sorted,reverse= -1)
            print("The sort of the people from oldest to youngest :\n")
            for i in sorted_list:
                print(f"{i['name']} that has {i['age']} years old.\n")
            input("Click 'Enter' to back to main menu : ")
            self.main_minu()
        else:
            print("You don't have anything yet.\n")
            input("Click 'Enter' to back to main menu : ")
            self.main_minu()


    def main_minu(self):
        cls()
        print("Welcome to Birthday App :\n")
        print("1. Add Persons.")
        print("2. Delete Persons.")
        print("3. Sort from oldest to youngest all person you have.")
        print("4. Reverse order of input.")
        print("5. Exit.")
        choice = input("\nEnter your Choice : ")
        if choice == "1":
            self.add_persons()
        elif choice == "2":
            self.delete_person()
        elif choice == "3":
            self.sort_from_oldest_to_youngest()
        elif choice == "4":
            self.reverse_order_of_input()
        elif choice == "5":
            exit()
        else:
            print("Invalid Choice!, Plz Try Again.")
            sleep(2)
            self.main_minu()
        
        

birth = Birthday()
birth.main_minu()