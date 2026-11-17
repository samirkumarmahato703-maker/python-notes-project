# DIGITAL NOTES MANAGEMENT SYSTEM
# Project No. 49
# Language: Python 3

FILE_NAME = "notes.txt"


# Load notes from file
def load_notes():
    notes = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|", 2)

                    if len(parts) == 3:
                        notes.append({
                            "id": parts[0],
                            "title": parts[1],
                            "content": parts[2]
                        })

    except FileNotFoundError:
        open(FILE_NAME, "w").close()

    return notes


# Save notes permanently
def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(
                note["id"] + "|" +
                note["title"] + "|" +
                note["content"] + "\n"
            )


# Generate new note ID
def generate_id(notes):
    highest = 0

    for note in notes:
        note_id = note["id"]

        if note_id.startswith("N") and note_id[1:].isdigit():
            highest = max(highest, int(note_id[1:]))

    return "N" + str(highest + 1)


# Add new note
def add_note(notes):
    print("\n--- ADD NOTE ---")

    title = input("Enter Title: ").strip()

    if title == "":
        print("Title cannot be empty. Note not saved.")
        return

    content = input("Enter Content: ").strip()

    note_id = generate_id(notes)

    note = {
        "id": note_id,
        "title": title,
        "content": content
    }

    notes.append(note)
    save_notes(notes)

    print("Note saved. ID:", note_id, "|", title)


# View all notes
def view_notes(notes):
    print("\n--- ALL NOTES ---")

    if len(notes) == 0:
        print("No notes found.")
        return

    for note in notes:
        print("\nID:", note["id"])
        print("Title:", note["title"])
        print("Content:", note["content"])


# Search notes
def search_notes(notes):
    print("\n--- SEARCH NOTE ---")

    keyword = input("Enter keyword: ").strip().lower()

    if keyword == "":
        print("Please enter a keyword.")
        return

    found = False

    for note in notes:
        if (keyword in note["title"].lower()
                or keyword in note["content"].lower()):

            print(
                note["id"], "|",
                note["title"], "|",
                note["content"]
            )
            found = True

    if not found:
        print("No matching notes found.")


# Edit note
def edit_note(notes):
    print("\n--- EDIT NOTE ---")

    note_id = input("Enter Note ID: ").strip().upper()

    for note in notes:
        if note["id"].upper() == note_id:

            new_content = input("Enter new content: ").strip()

            note["content"] = new_content
            save_notes(notes)

            print("Note", note_id, "updated.")
            return

    print("Note ID does not exist.")


# Delete note
def delete_note(notes):
    print("\n--- DELETE NOTE ---")

    note_id = input("Enter Note ID: ").strip().upper()

    for note in notes:
        if note["id"].upper() == note_id:

            notes.remove(note)
            save_notes(notes)

            print("Note", note_id, "deleted.")
            print("Notes left:", len(notes))
            return

    print("Note ID does not exist.")


# Main program
def main():

    notes = load_notes()

    while True:

        print("\n===================================")
        print(" DIGITAL NOTES MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        print("===================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            edit_note(notes)

        elif choice == "5":
            delete_note(notes)

        elif choice == "6":
            print("Thank you for using Digital Notes Management System!")
            break

        else:
            print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()