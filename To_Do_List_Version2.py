# import json package to write and store the list in a text
import json



# import JSON package to store and load data in file
from json import JSONDecodeError

# import easygui package to use buttonbox, textbox, msgbox usage to interface with users.
import easygui as eg
from easygui import buttonbox


# I use global to these var. let them can be used in anywhere of the file.
global MENU_OP
global LISTS_OP

# TN is all title of box in my program
global TN

# SPACE is barrier in my program
global SPACE
global LIST_F_OP
global ITEMS_OP
global ITEM_F_OP
global data


#I create these lists to store the all functions  can be used in my app
MENU_OP = ["START LIST", "ENDING"]
LISTS_OP = ["Check List","Add New List", "Remove List",  "Clear All Lists", "Back"]
LIST_F_OP = ["Manage Items","Update Info", "Show Detail", "Manage Items", "Back"]
ITEMS_OP = [ "Check Items","Add New Items", "Cancel All Items", "Back"]
ITEM_F_OP = ["Remove", "Update", "Complete/State", "Mark", "Back"]
TN = "To-Do-List-App"

# use space as barrier in the textbox
SPACE = "-" * 60 + "\n" + "-" * 60










# function to get data from To_Do_list.txt
def got_data():
    # to ensure the file name
    filename="To_Do_List.txt"

    # to open filename and get the data
    try:
        with open(filename, "r") as file:

            data = json.loads(file.read())

    # if it doesn't exist to do list text , it will create a empty list and create a new file '
    except (FileNotFoundError, JSONDecodeError):
        data=[]

    # if data is None type, can boundary it , let the program running continue
    if data==None:
        data=[]
    # return data, let it involved following functions
    return data



# function to store data into the To_Do_list.txt
def store_data(data):
    # to ensure the file name
    filename="To_Do_List.txt"
    #to use new data to cover old data
    with open(filename, "w") as file:
        json.dump(data, file)

    # if data is stored, msg out successfully stored data
    eg.msgbox("Successfully stored data",title=TN)



# function to show out current lists has been stored
def show_list(data):
    # create empty list and named it as content to stored sentence
    content=[]
    # input elements set, and tell user which content list includes
    content.append("order ."+"List Name" + "\t:\n" + "List Description" + "\n"+SPACE+"\n")

    # to show out all of lists
    for i,element in enumerate(data):

        # input all lists in content list

        content.append(str(i+1)+"."+element[0]+"\t:\t"+element[1]+"\n"+SPACE+"\n")

    # use the textbox to show out all of lists
    eg.textbox("Current lists: ",TN,content)


# function to add a new list
def add_list(data):
    # use a loop to got list name and description until the list name and description is valid
    while True:

        # try the list name and description if they are  None type
        try:
            # use enterbox to get list name
            list_name=eg.enterbox("Please enter the name of the list you want to add",title=TN)

            #use enterbox to get list description
            description="Your Description:\n"
            list_desc=eg.textbox(f"Description for {list_name} :",TN,description)

            #use selectively order to stop the loop until the list name and description is valid
            if list_name=="" or list_desc=="":#if the list name and description is empty
                eg.msgbox("The entered name and description cannot be empty\nPlease try it again",title=TN)

            elif len(list_name) >50 or len(list_desc) >999:#if the list name and description is longer than limitation
                eg.msgbox("The entered name cannot be longer than 50 characters\nThe entered description cannot be longer than 999 characters\nPlease try it again",title=TN)
            else:
                break

        except TypeError:
            eg.msgbox("The entered name and description cannot be empty\nPlease try it again",title=TN)

    # create an empty list to store the list data, list name, list description, and list storing items which is "list" type
    items=[]
    list=[list_name,list_desc,items]

    #use append to  add new list

    data.append(list)


# function to remove a current list. into data, and index of the list you want to remove
def remove_list(data,index_element):

    # the index of the list is the name of the list, so use the loop and count to let the index is the order(int type) of the list in data
    count=0
    for element in data:
        if element[0]==index_element:
            index=count
        else:
            count+=1


    # use pop to remove the current list
    data.pop(index)
    return data



# function to choose which function users want to do for lists
def choice_list_function_got(index,function):


    # use buttonbox to get the choice
    choice=buttonbox(f"Please enter your choice for list {index}",choices=function,title=TN)
    # return the choice out
    return choice

# function to update the name of list
def list_f_update(index,data):
    index_name=index
    count=0
    for element in data:
        if element[0]==index:
            index=count
        else:
            count+=1

    while True:

        new_name=eg.enterbox(f"Please enter your new list for {index_name} ",title=TN)
        if len(new_name)==0 or len(new_name)>50:
            eg.msgbox("The new name length cannot be longer than 50 characters OR empty\nPlease try it again",title=TN)
        else:
            break
    # if the name of list updates successfully
    data[index][0]=new_name
    eg.msgbox("Successfully updated list",title=TN)
    # return the new data
    return data


# function to show out all current list detail
def list_f_show_detail(index,data):
    index_name=index
    count=0
    for element in data:
        if element[0]==index:
            index=count
        else:
            count+=1
    # use content which is list type to  store name and description and textbox
    content=f"Description of The list [{index_name}] is: \n{data[count][1]}]"
    eg.textbox(f"List and Description:" ,TN,content)

#function to got the item function choice
def item_operator_choice_got(index):

    ITEMS_OP = ["Check Items","Add New Items",  "Cancel All Items", "Back"]

    choice=buttonbox(f"Please enter your choice for list {index} ",choices=ITEMS_OP,title=TN)

    # return the item function choice

    return choice

def add_item():
    # use a loop to get the item information until the item information is valid

    while True:
        # use try to except if information is None type
        try:

            item_name=eg.enterbox("Please enter the name of the item you want to add",title=TN)
            description="Your Description:\n"
            item_desc=eg.textbox(f"Description for {item_name} :",TN,description)
            time="Your time:"
            item_time=eg.textbox(f"Time for {item_name}],E.G.[12:30]:",TN,time)
            # if the information is empty
            if item_name=="" or item_desc=="" or item_time=="":
                eg.msgbox("The entered name and description, time cannot be empty\nPlease try it again",title=TN)
            # if the information is longer than limitation
            elif len(item_name) >50 or len(item_desc) >999 or len(item_time) >50:
                eg.msgbox("The entered name cannot be longer than 50 characters\nThe entered description cannot be longer than 999 characters\nThe entered time cannot be longer than 50 character\nPlease try it again",title=TN)
            else:
                break

        except TypeError:
            eg.msgbox("The entered name and description , time cannot be empty\nPlease try it again",title=TN)

    # the default of state is Incomplete and the default of mark is 0 .
    state="Incomplete"
    mark=0
    # use item which is list type to store the item information
    item=[item_name,item_desc,item_time,state,mark]

    # return the item out to store the item in data
    return item


# function to run the item functions options
def item_f_op(choice,data,index,item_index):
    # if there is no item in the selected list, use msgbox to warm the uers and let users to add new item in the list
    # continue in the loop, to select a new list which contain items
    if data[index][2]==[]:

        eg.msgbox("Your items is empty\nplease Add items in the list",TN,)
    # if there are items in the selected list. To run the function depends on choice
    else:
        # remove the item function
        if choice=="Remove":
            data[index][2].pop(item_index)

        # update the item function
        elif choice=="Update":
            new_item=add_item()
            data[index][2][item_index]=new_item

        # change the item state, complete or incomplete or doing
        elif choice=="Complete/State":
            state=eg.buttonbox("Please select the item state [Incomplete/Complete/Doing]",TN,["Incomplete","Complete","Doing"])
            data[index][2][item_index][3]=state

        # change the item mark from 0 to 1-5
        elif choice=="Mark":
            mark=eg.buttonbox("Please select the item mark[*]",TN,["1","2","3","4","5"])
            # use string * to show user's mark
            data[index][2][item_index][4]=int(mark)

        # if nothing, users can use the back directly out of the loop
        elif choice=="Back":
            pass

        # if choice is invalid, use msgbox to show and let users try it again
        else:
            eg.msgbox("Your choice is invalid\nPlease try again",title=TN)



# function to show all current lists detail and select which one you want to check
def item_f_show_current_item(index,data):
    # use content to store the item information use item_names to store the item's name to use for selecting
    content=[]
    item_names=[]
    set=f"order.Item Name;\t\tItem Description;\nItem Time;\tState;\tMark\n{SPACE}\n"
    content.append(set)

    # use the loop to append item information in the content list
    for i,element in enumerate(data[index][2]):
        # use the selectively order, if the element is 0 show str No mark, if the element is not 0, show str * about num
        if element[4]==0:
            mark="No mark"

        elif element[4]!=1:
            mark="*"*element[4]
            mark="mark:"+mark


        content.append(str(i+1)+"."+element[0]+"\t:\t"+element[1]+"\n"+element[2]+element[3]+"\t\t"+mark+f"\n{SPACE}\n")
        item_names.append(element[0])
    # use textbox to show out all current items detail
    eg.textbox("Current Items: ",TN,content)
    # use buttonbox to select which item you want to manage
    item_index=eg.buttonbox("Select which item you want to manage ",TN,item_names)
    for i,element in enumerate(data[index][2]):
        if element[0]==item_index:
            index=i
    # return the index of item the user want to check
    return index


# function to  select which function you want to do for items
def item_f_choice_got(data,index,item_index):
    ITEM_F_OP = ["Remove", "Update", "Complete/State", "Mark", "Back"]
    choice=buttonbox(f"Please select a function to the item [{data[index][2][item_index][0]}]  ",choices=ITEM_F_OP,title=TN)

    return choice

# to run all functions in the manage item menu
def manage_item(index,data):


    # to get index which is int type
    index_name=index
    count=0
    for element in data:
        if element[0]==index:
            index=count
        else:
            count+=1



    # if the list does not contain any items, it will warn users, you cannot to do remove and check function

    while True:
        while True:
            choice = item_operator_choice_got(index_name)
            if data[index][2] == []:

                if choice in ["Back", "Add New Items"]:
                    break

                elif choice in ["Check Items", "Cancel All Items"]:
                    eg.msgbox("The list does not have any items\nPlease firstly [Add New Items]")

            else:
                break
        # if users choose the back button to stop the loop
        if choice=="Back" or choice is None:
            break
        # add new items in
        elif choice=="Add New Items":
            new_item=add_item()
            data[index][2].append(new_item)
            eg.msgbox("Successfully added new items")


        # check the items information

        elif choice=="Check Items":
            item_index=item_f_show_current_item(index,data)
            f_choice_got=item_f_choice_got(data,index,item_index)
            item_f_op(f_choice_got,data,index,item_index)



        elif choice=="Cancel All Items":
            data[index][2]=[]

        else:
            eg.msgbox("Your choice is invalid\nPlease enter it again")

def check_list(index,data):

    while True:
        choice_got=choice_list_function_got(index,LIST_F_OP)
        if choice_got=="Update Info":

            data=list_f_update(index,data)
        elif choice_got=="Show Detail":
            list_f_show_detail(index,data)


        elif choice_got=="Manage Items":
            manage_item(index,data)

        elif choice_got=="Back":
            break
        else:
            eg.msgbox("Your choice is invalid\nPlease enter it again")

        return data


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
            show_list(data)
            index=got_index_list(data)
            check_list(index,data)


        elif lists_operator_choice_gain == "Clear All Lists":
            clear_list(data)


        else:
            eg.msgbox(f"current choice:{lists_operator_choice_gain}\nPlease enter your choice in Lists Menu!\nplease enter again")


    return data



def action():


    while True:
        data=got_data()
        menu_choice_got=eg.buttonbox("Please enter your choice in Menu:",title=TN, choices=MENU_OP)
        if menu_choice_got=="START LIST":
            data=lists_operator(data)


        elif menu_choice_got=="ENDING":
            break



        else:
            eg.msgbox(f"current choice: {menu_choice_got}\nPlease select a menu option\nInvalid choice you do\nTry it Again")

        store_data(data)


def main():

    print("Welcome to To_Do Lists!")

    action()
    print("App is ENDING")













# the function to run the process
if __name__ == "__main__":
    main()