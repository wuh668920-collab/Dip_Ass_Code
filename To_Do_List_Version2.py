# import json package to write and store the list in a text
import json

from json import JSONDecodeError
from subprocess import check_output

import easygui as eg

global MENU_OP
global LISTS_OP
global TN



MENU_OP = ["START LIST", "Ending", "COMPASS", "ACCOUNT"]
LISTS_OP = ["Add New List", "Remove List", "Check List", "Clear All Lists", "Back"]
TN="To-Do-List-App"






def got_data():
    filename="To_Do_List.txt"
    try:
        with open(filename, "r") as file:

            data = json.loads(file.read())

    # if it doesn't exist to do list text , it will create a empty list and create a new file '
    except (FileNotFoundError, JSONDecodeError):
        data=[]

    if data==None:
        data=[]

    return data




def store_data(data):
    filename="To_Do_List.txt"
    with open(filename, "w") as file:
        json.dump(data, file)
    eg.msgbox("Successfully stored data",title=TN)

def compass_show():
    pass


def show_list(data):
    content=""
    for i,element in enumerate(data):
        i=i+1
        content=f"{str(i)}"+"."+element[0]+"\n"
    if content=="":
        eg.msgbox("The entered list cannot be empty",title=TN)
    eg.textbox(content,title=TN)



def add_list(data):
    while True:
        list_name=eg.enterbox("Please enter the name of the list you want to add",title=TN)
        list_desc=eg.enterbox("Please enter the description of the list you want to add",title=TN)
        if list_name=="" or list_desc=="":
            eg.msgbox("The entered name and description cannot be empty\nPlease try it again",title=TN)
        elif len(list_name) >50 or len(list_desc) >999:
            eg.msgbox("The entered name cannot be longer than 50 characters\nThe entered description cannot be longer than 999 characters\nPlease try it again",title=TN)
        else:
            break


    items=[]
    list=[list_name,list_desc,items]

    data.append(list)

def remove_list(data,index_element):
    count=0
    for element in data:
        if element[0]==index_element:
            index=count
        else:
            count+=1



    data.pop(index)
    return data




def check_list(index,data):
    show_list(data)


def clear_list(data):
    data.clear()




def got_index_list(data):
    
    content=[]
    for element in data:
        content.append(element[0])
    choice_index_list=eg.buttonbox("Select a Current List",choices=content,title=TN)
    return choice_index_list


def lists_operator(data):
    while True:

        while True:
            lists_operator_choice_gain = eg.buttonbox("Please enter your choice in Lists Menu:", title=TN,
                                                      choices=LISTS_OP)
            if data==[]:
                if lists_operator_choice_gain in ["Back","Clear All Lists","Add New List"]:
                    break
                else:
                    eg.msgbox("The Current lists is empty, so cannot to do it",title=TN,)
            else:
                break



        if lists_operator_choice_gain == "Back":
            break
        elif lists_operator_choice_gain == "Add New List":

            add_list(data)


        elif lists_operator_choice_gain == "Remove List":
            index=got_index_list(data)
            remove_list(data,index)
            eg.msgbox("Successfully remove list",title=TN)


        elif lists_operator_choice_gain == "Check List":
            index=got_index_list(data)
            check_list(index,data)


        elif lists_operator_choice_gain == "Clear All Lists":
            clear_list(data)


        else:
            eg.msgbox(f"current choice:{lists_operator_choice_gain}\nPlease enter your choice in Lists Menu!\nplease enter again")


    return data



def action():
    global data

    while True:
        data=got_data()
        menu_choice_got=eg.buttonbox("Please enter your choice in Menu:",title=TN, choices=MENU_OP)
        if menu_choice_got=="START LIST":
            data=lists_operator(data)


        elif menu_choice_got=="Ending":
            break


        elif menu_choice_got=="COMPASS":
            compass_show()


        elif menu_choice_got=="ACCOUNT":
            pass


        else:
            eg.msgbox(f"current choice: {menu_choice_got}\nPlease select a menu option\nInvalid choice you do\nTry it Again")

        store_data(data)

def main():



    action()













# the function to run the process
if __name__ == "__main__":
    main()