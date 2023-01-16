### Import personal modules
from console import Console

class Menu():
    def __init__(self, colored=True):
        self.console = Console(colored)
        self.menu_display=""
        self.valid_choices=[]

    def menu_choice_dynamic(self, lst_menu_display:list=[]) -> int:
        """Return correct menu selection from a menu build dynamically based on lst_menu_display 

        Args:
            lst_menu_display (lst): List of elements to display in sequence in a selection menu

        Returns:
            [int]: index of the element in the list (starting at position 1).Return 0(zero) in case of Cancel Choice.
        """
        self.console.print_msg("INFO", "Elements with your criteria:")
        print("0. Cancel")
        [print(f"{i+1}. {menu_display}") for i, menu_display in enumerate(lst_menu_display)]
        print()
        bad_choice = True
        # Loop until a good option is selected
        while bad_choice:
            menu_choice = input("What is your choice: ")
            if not menu_choice.isdigit() or int(menu_choice) not in range(0, len(lst_menu_display)+1):
                self.console.print_msg("ERROR", "Bad menu choice, please retry.")
            else:
                bad_choice = False
        return int(menu_choice)

    def menu_choice_fixed(self, menu:str="", menu_valid_choices:list=[]) -> str:
        """Print a menu & loop until selection is correct

        Args:
            menu (str) sring with the menu to display.
            menu_valid_choices (list: Array with valid response. Defaults to [].
        """
        print(menu)
        bad_choice = True
        # Loop until a good option is selected
        while bad_choice:
            menu_choice = input("What is your choice: ")
            if menu_choice not in menu_valid_choices:
                self.console.print_msg("ERROR", "Bad menu choice, please retry.")
            else:
                bad_choice = False
        return menu_choice

    def menu_choice_YN(self, msg:str="") -> str:
        confirm = False
        while not confirm == "Y" and not confirm == "N": 
            confirm = input(f"{msg} (Y/N) ? ").upper()
            if not confirm == "Y" and not confirm == "N":
                self.console.print_msg("ERROR", "Bad menu choice, please retry.")
        return confirm

if __name__ == "__main__":
    menu_fixed_valid_choice =["1", "10", "11", "12", "9", "A"]
    menu_fixed ="""
1. Test
    10. Add
    11. Modify
    12. Delete
A. A menu with letter
9. Exit
"""
    print("*** All menu will loop until you select a correct menu option")    
    menu = Menu()
    selection = menu.menu_choice_fixed(menu=menu_fixed, menu_valid_choices=menu_fixed_valid_choice)
    print(f"your selection : {selection}\n\n")
    selection = menu.menu_choice_dynamic(["Apple", "Peer", "Banana"])
    print(f"your selection : {selection}\n\n")
    selection = menu.menu_choice_YN("Are you sure ?")
    print(f"your selection : {selection}\n\n")
    