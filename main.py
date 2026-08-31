import json

with open("tasks.json", "r") as file:
    notes = json.load(file)


def isValid(choice):
    if choice < 1 or choice > 5:
        return False
    return True


def addNote():
    note = input("Add the note: ")
    notes.append(note)


def listNote():
    i = 1
    for note in notes:
        print(f"{i}. {note}")
        i += 1


def deleteNote():
    note = int(input("Delete the note: "))

    try:
        notes.remove(notes[note - 1])
    except:
        print()
        print(f"Note number '{note}' doesn't exist")


def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(notes, file)


while True:
    print("Press 1 to add a note")
    print("Press 2 to delete a note")
    print("Press 3 to list the notes")
    print("Press 4 to save changes")
    print("Press 5 to quit the program")

    print()

    choice = int(input("Select a number from 1 to 5: "))

    print()

    if isValid(choice):
        if choice == 1:
            addNote()
            print()
        elif choice == 2:
            deleteNote()
            print()
        elif choice == 3:
            listNote()
            print()
        elif choice == 4:
            saveTasks()
        else:
            saveTasks()
            break
    else:
        print("Invalid option.")

