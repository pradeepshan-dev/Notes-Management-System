notes_remove = []

def main():

    print("==============================")

    print("NOTES MANAGER")

    print("==============================")

    print("1. Add Note")

    print("2. View Note")

    print("3. Delete All Notes")

    print("4. Exit")

    print("5. Remove One Note")

    print()

while True:

    # print(notes_remove)

    main()

    try:

        user_choice = int(input("Enter Your Choice : "))

    except ValueError:

        print("Enter Number's Only")

        continue

    if user_choice == 1:

        with open("notes.txt","a") as file:

            note = input("Enter Your Note : ")

            file.write(note + "\n")

        print("NOTE ADDED SUCCESSFULLY")

    elif user_choice == 2:

        try:
            
            with open("notes.txt","r") as file:
                
                read_notes = file.read()
                
                print(read_notes)

        except FileNotFoundError:

            print("Add a Note to View the Notes.")



    elif user_choice == 3:

        with open("notes.txt","w+") as file:

            delete_note = file.write("")

        print("NOTES REMOVED SUCCESSFULLY")

    elif user_choice == 4:

        print("Thank You For Coming! Have a good day :)")

        break

    elif user_choice == 5:

        try:
            
            with open("notes.txt","r") as file:
                
                for content in file:
                    
                    notes_remove.append(content)

        except FileNotFoundError:

            print("Please add a note before trying to remove one. ")

        for i in range(len(notes_remove)):

            print(i+1,".",notes_remove[i])

        try:
            
            user_remove = int(input("Enter Number To Remove Particular Note : "))

        except ValueError:

            print("Enter Number's Only Based On Your Note")

        try:
            
            notes_remove.pop(user_remove - 1)

        except IndexError:

            print("Invalid note number. Please choose a number from the displayed list.")

        for i in range(len(notes_remove)):

            print(i+1,".",notes_remove[i])

        with open("notes.txt","w") as file:

            file.writelines(notes_remove)

        notes_remove.clear()
    
    else:
        
        print("Invalid Input Enter Number Between 1 to 5")