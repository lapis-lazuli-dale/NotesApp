import sys
from notebook import Note, Notebook

class Menu:
    def __init__(self):
        self.notebook=Notebook()
        self.choices={
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_notes,
        "4": self.modify_notes,
        "5": self.quit_program
        }
    def display_menu(self):
#        print("\n"*20)
        print('''
        
        Notebook Menu:
        
        1 : Show Notes
        2 : Search Notes
        3 : Add notes
        4 : Modify Notes
        5 : Quit
        
        '''
        )
        
    def run(self):
        while True:
            self.display_menu()
            choice=input('What is your choice?  ')
            action=self.choices.get(choice)
            if action:
                action()
            else:
                print("\n")
                print("{0} is not a valid choice".format(choice))
    def show_notes(self,notes=None):
        if not notes:
            notes=self.notebook.notes
        for note in notes:
            print("\n")
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
            
    def search_notes(self):
        search_input=input("What keyword do you have for your search?   ")
        notes=self.notebook.search_for_notes(search_input)
        self.show_notes(notes)
        
    def add_notes(self):
        tags=input("What's title do you want to give this note?    ")
        memo=input("Write anything here:    ")
        self.notebook.create_new_note(memo, tags)
        print("\n")
        print("Your note has been added.")
        
    def modify_notes(self):
        identity=input("What is the note's id number?   ")
        memo=input("What do you want to write?   ")
        tags= input("What title do you want to save this note with?    ")
        if memo:
            self.notebook.edit_note_memo(identity, memo)
        if tags:
            self.notebook.edit_note_tags(identity, tags)
            
    def quit_program(self):
        print("\n")
        print("The program has been quit.")
        sys.exit(0)
        
if __name__ == "__main__":
    Menu().run()
