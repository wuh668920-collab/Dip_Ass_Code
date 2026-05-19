# Welcome to Version To To Do List python program
# Compare to Version1, the advance of version 2 is that:
# 1.The version 2 colours the text:
# 2.The version 2 use tkinter package to chang the interfaces from input() and print() in Python Console to button by msgbox
# The changing make the program to be easier to use
# 3.The version 2 use tkinter to show the list and item. More aesthetically pleasing.


# import json package to write and store the list in a text
import json
from json import JSONDecodeError
# import easygui to use msgbox to show buttons



def store_file():
    # open an empty list to get and update the data in the program

    store_list=[]

    # To ensure the stored file name as To_DO_List
    file_name="To_Do_List.txt"


    # The try to ensure the programming continue running if the file does not exist
    try:
        # if the file exists, using the Json to get the data from the file
        with open(file_name, "r") as file:

            store_list=json.load(file.read())

        # if the file does not exist, pass and continue
    except (FileNotFoundError, JSONDecodeError) :
        pass






# This is the main function to run the programming
def main():
    store_file()



# To run the main function
if __name__ == "__main__":
    main()

