import json

try:
    with open("tasks.json", "r") as file:
        notes = json.load(file)
except:
    notes = []

def isValid(choice):
    if choice < 1 or choice > 5:
        return False
    return True


def addNote():
    note = input("Add the note: ")
    notes.append(note)


def listNote():
    if(len(notes) == 0):
        print("No notes to list ): ")
    else:
        i = 1
        for note in notes:
            print(f"{i}. {note}")
            i += 1


def deleteNote():

    if(len(notes) == 0):
        print("Nothing to delete :/ ")
    else:    
        note = int(input("Delete the note: "))
        try:
            noteNumber = note
            noteName = notes[note - 1]
            notes.remove(notes[note - 1])
            print(f"Successfully deleted note number {noteNumber}: '{noteName}'")
        except:
            print()
            print(f"Note number '{note}' doesn't exist")


def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(notes, file)


while 1:
    print("Press 1 to add a note")
    print("Press 2 to delete a note")
    print("Press 3 to list the notes")
    print("Press 4 to save changes")
    print("Press 5 to quit the program")

    print()
    while 1:
        try:
            choice = int(input("Select a number from 1 to 5: "))
            break
        except ValueError:
            print("This isn't a correct option")
        except:
            print("How tf did you get here")
   
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

