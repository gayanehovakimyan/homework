notes_list=[]
def note_creation():
    while True:
        stop=int(input('If you want to stop press 1, else press 2:'))
        note_bov=input('Enter the text you want to note:  ')

        if stop==1:
            break
        elif stop==2:
            if note_bov:
                note_id=len(notes_list)+1
                note={'id': note_id,
                    'description':note_bov}
                notes_list.append(note)
                print(f"Your '{note_bov}' succesfully appended in {note_id}:")
	#else:
		#break
note_creation()

def listing():
    check=input("Do you want to check your  notes? (y/n).")
    if check=='n':
        if not notes_list:
            print("There are no notes in your note list.")
    elif check=='y':
         for notes in  notes_list:
            print(f"ID: {notes['id']}, Description: {notes ['description']}")
listing()

def retrieval():
    note_id = int(input("Enter the ID of the note you want to retrieve: "))
    note_ret=[note for note in notes_list if note['id'] == note_id]
    if  note_ret:
        print(f"Note ID:{note_id} Description:{note_ret}")
    else:
        print("Note not found. ")

retrieval()

def delete():
    try:
        delete_id = int(input("Enter the ID you want to delete: "))
        notes_to_delete = []

        for notes in notes_list:
            if notes['id'] == delete_id:
                notes_to_delete.append(notes)
        if notes_to_delete:
            for notes in notes_to_delete:
                notes_list.remove(notes)
            print(f"Note with ID {delete_id} is found and successfully deleted.")
        else:
            print(f"No note found with ID {delete_id}.")
                    
    except ValueError:
        print("Please enter the right ID.")


delete()

def keyword_note():
    keyword = input("Enter the keyword to search for: ")
    note_search=[note for note in notes_list if keyword.lower() in note ['description']]
    if note_search:
        print(f"The keyword you entered is true, whit following detailed.")
        for found in note_search:
            print(f"Note ID: {found['id']}, {found['description']}")
    else:
        print(f"{keyword} you entered not found")
    
    
keyword_note()
