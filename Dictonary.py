'''Write a Python program that allows the user to create a dictionary of personal details for
a group of people.
The program should ask the user to enter the name, age, and occupation for each person, and then store
this information in a dictionary.
Once all the details have been entered, the program should print out the dictionary.'''

############################

def create_personal_details():
    personal_details_list = []

    while True:
        name = input("Enter the name (or type 'exit' to stop entering details): ").strip()
        if name.lower() == "exit":
            break

        age = int(input("Enter the age: "))
        occupation = input("Enter the occupation: ").strip()

        person_details = {"Name": name, "Age": age, "Occupation": occupation}
        personal_details_list.append(person_details)

    return personal_details_list

def main():
    print("Create a dictionary of personal details for a group of people.")
    personal_details_list = create_personal_details()

    print("\nPersonal Details Dictionary:")
    for person in personal_details_list:
        print(person)

if __name__ == "__main__":
    main()
