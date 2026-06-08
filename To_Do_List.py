
# import json package to write and store the list in a text
import json

from json import JSONDecodeError




# use the SPACE with many dash to better show the process
# SPACE = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

space_length=120
SPACE=f"-"*space_length
SPACE=SPACE+"\n"+SPACE+"\n""\n"
SPACE=f"\n{SPACE}"
intent_length=5
INTENT="-"*intent_length


#the common function class to store the function can be used in all classes
class common_function:
    def __init__(self):
        pass


# the function to show the item name when the user want to operator in items
    def show_item_name(self, list_got):
        for i, element in enumerate(list_got):
            print(f"{i}.{element[0]}")


# the function to show the list name when the user want to operator in items
    def show_list_name(self, list_got):
        i = 0
        print(f"Current List :")
        for element in list_got:
            i = i + 1
            print(f"{i}.{element}")


# the item check class to check a particular item for updating item , remove item, state a item, mark a item
class item_check:
    def __init__(self, item_check_list, store_3Dlist):

        #upload item check list and store 3D list as public variant
        self.item_check_list = item_check_list
        self.store_3Dlist = store_3Dlist


# show all items' data like name, task to do, deadline, state and mark if it have'
    def show_item_data(self, index_list, index_item):
        # use "item" to store an item with its data
        item = self.store_3Dlist[index_list][2][index_item]
        print(f"Item Detail: ")
        print(
            f"\n--- ITEM DETAILS ---\nName: {item[0]}\nTask: {item[1]}\nTime: {item[2]}\nState: {item[3]}\nMark: {item[4]}")

    # use function to update a particular item and changing its name and task
    def update_item(self, index_list, index_item):

        # the process allow use input a space if they don't need a name or task to the item'
        while True:
            new_name = input(f"Enter new name (or skip): ")



            new_task = input(f"Enter new task (or skip): ")
            # boundary the length of item name and item description
            #due to too long , it is not aesthetic
            if len(new_name) > 50 or len(new_task) > 500 :
                print(f"Item cannot be longer than 50 characters.","current length:",{len(new_name)})
                print("Item description cannot be longer than 500 characters. .","current length:",{len(new_task)})
            else:
                break


        if new_name != "": self.store_3Dlist[index_list][2][index_item][0] = new_name
        else:
            print("New name cannot be empty.")
        if new_task != "": self.store_3Dlist[index_list][2][index_item][1] = new_task
        else:
            print("New task cannot be empty.")


    # use function to remove a particular item
    def remove_item(self, index_list, index_item):
        self.store_3Dlist[index_list][2].pop(index_item)
        # print item removed successfully to ensure the item is removed
        print("Item removed successfully.")
    # use function to change the state of the item if the user finish it
    def state_item(self, index_list, index_item):
        state = input("Complete? [Yes/No]: ").capitalize()

        while True:

            if state == "Yes" :
                 self.store_3Dlist[index_list][2][index_item][3] = "Completed"
                 break
            elif state == "No" :


                self.store_3Dlist[index_list][2][index_item][3] = "Uncompleted"
                break
            else:
                print("Invalid input.")
                print("Please only type [Yes] or [No].")
    # use the function to mark the item task
    def mark_item(self, index_list, index_item):
        mark=0

        # boundary if the mark "*" is in 1 -5
        while True:


            mark = input("Give a mark (1-5 or description): ")
            if mark in ["1","2","3","4","5"]:
                break
            else:
                print("Invalid number.\nPlease only type 1 - 5.")

        mark="*"*int(mark)
        self.store_3Dlist[index_list][2][index_item][4] = mark

# the class to store the functions of items
class item_operator(common_function, item_check):
    def __init__(self, operator_item, store_3Dlist, item_check_menu):
        # super inherited from item_check and uploading the operator item and store 3D list as public variant
        item_check.__init__(self, item_check_menu, store_3Dlist)
        self.operator_item = operator_item
        self.store_3Dlist = store_3Dlist
    # function to get the data of item to prepare for add item
    def item_data_got(self):


        # boundary the length of item name , task , time , to be aesthetic.

        # got the item name , item task, item deadline
        while True:
            name = input("Item name: ")
            task = input("Task description: ")
            time = input("Time (eg. 12:00): ")
            if len(name)>50 or len(task)>250 or len(time)>20:
                print("Item name cannot be longer than 50 characters.","current length:",{len(name)})
                print("Item task cannot be longer than 250 characters. .","current length:",{len(task)})
                print("Item time cannot be longer than 20 characters.","current length:",{len(time)})
                print("Please enter again")

            elif name=="" or task=="":
                print("Item name, task cannot be empty")
                print("Please enter again")

            else:
                break

        # combine them as a list, default the state is uncompleted and mark is none
        self.item = [name, task, time, "Uncompleted", "None"]
    # function to add a new item
    def add_item(self, index_list):
        self.item_data_got()
        # Add new item as lastest item
        self.store_3Dlist[index_list][2].append(self.item)

        # If the item added successfully
        print("Item added.")


    # function to show existed items' name
    def show_all_items(self, index_list):
        items = self.store_3Dlist[index_list][2]
        if not items:
            # To ensure if there is item in the file or not
            print("No items found.")
            return False

        # To get the index of item and item name and item task
        for i, itm in enumerate(items):
            print(f"{i + 1}. {itm[0]} [{itm[3]}]")
            return True

    # Function to check the detail of an item
    def check_item_detail(self, index_list):

        # to show all current item in the list
        if self.show_all_items(index_list):
            # to boundary the index_list
            try:

                while True:
                    print(SPACE)
                    index_operator= int(input("Select item index: ")) - 1
                    if not (0 <= index_operator < len(self.store_3Dlist[index_list][2])):
                        print("Invalid index.")
                    else:break

                # use loop to run the operators
                while True:
                    print(f"\nEditing: {self.store_3Dlist[index_list][2][index_operator][0]}")
                    for i, op in enumerate(self.item_check_list):
                        print(f"{i + 1}.{op}")
                    print("Please select your action")

                    # boundary if user enter an invalid choice number
                    while True:
                        choice =int(input("Choice: "))
                        if len(self.item_check_list)+1>choice>0:
                            break
                        else:
                            print("Please enter a valid choice!")
                            print("Please enter again")

                    if choice == 1:
                        self.remove_item(index_list, index_operator)
                        break
                    elif choice == 2:
                        self.update_item(index_list, index_operator)
                    elif choice == 3:
                        self.state_item(index_list, index_operator)
                    elif choice == 4:
                        self.mark_item(index_list, index_operator)
                    elif choice == 5:
                        break
                    print("New Item Data:")
                    self.show_item_data(index_list, index_operator)
            # if the choice is not in the choice list
            except ValueError:
                print("Please enter a number.")
    # use a loop to run the operator
    def acted_item_operator(self, index_list):
        print(SPACE)
        self.show_list_name(self.operator_item)
        print(SPACE)
        try:
            # boundary if users input invalid choice number
            while True:
                choice = int(input(f"Choice[1-{len(self.operator_item)}]: "))
                if choice in range(1,len(self.operator_item)+1):
                    break
                else:
                    print("Please enter a valid choice!")
                    print("Please enter again")




            if choice == 1:
                self.add_item(index_list)
            elif choice == 2:
                self.check_item_detail(index_list)
            elif choice == 3:
                self.store_3Dlist[index_list][2] = []
                print("All items cleared.")
            elif choice == 4 :


                # return 0 to stop the loop
                return 0
        except ValueError:
            print("Please enter a valid number.")
        # return 1 to continue the loop
        return 1


class list_check(common_function):
    def __init__(self, list_check_list, store_3Dlist, item_op_cl):
        # super inherite the class_check_list
        super().__init__()
        self.list_check_list = list_check_list
        self.store_3Dlist = store_3Dlist
        self.item_op_cl = item_op_cl

        # show all list check operators
    def show_list_check_operator(self):
        print("List Operator Menu:")
        for i, item in enumerate(self.list_check_list):
            print(f"{i + 1}.{item}")
        #Acted the list check related functions
    def acted_list_check(self, index_list):
        print(SPACE)
        print(f"List: {self.store_3Dlist[index_list][0]}")
        print(SPACE)
        self.show_list_check_operator()
        while True:
            try:
                print("Please enter your action")
                while True:
                    choice = int(input("Choice: "))
                    if choice in range(1,6):
                        break
                    else:
                        print("Please enter a valid choice!")
                        print("Please enter again")
                choice=int(choice)
                if choice == 1:
                    while True:
                        new_name = input("New list name: ")
                        if new_name == "":
                            print("New name cannot be empty!")
                            print("Please try again")
                        elif len(new_name)>50:
                            print("New name cannot be longer than 50 characters!","current length",len(new_name))
                            print("Please try again")
                        else:break



                    if new_name: self.store_3Dlist[index_list][0] = new_name
                elif choice == 2:
                    print(f"Description: {self.store_3Dlist[index_list][1]}")
                elif choice == 3:
                    while True:
                        if self.item_op_cl.acted_item_operator(index_list) == 0:

                            break
                elif choice == 4:
                    break
                return 0
            except ValueError:
                print("Invalid input.")
        return 1

# class to store the list operators functions
class list_operator(list_check):
    def __init__(self, operator_list, store_3Dlist, check_menu, item_op_cl):
        super().__init__(check_menu, store_3Dlist, item_op_cl)
        self.operator_list = operator_list
        self.store_3Dlist = store_3Dlist
    # function to act the list operators function
    def acted_list_operator(self):
        print(SPACE)
        print("Current lists:")

        # to justify if there is list in the store 3D list or not
        if not self.store_3Dlist:
            print("[Empty]")

        # if there is list in the store 3D list , it will show the order depends on creating time and show out name of list

        for i, lst in enumerate(self.store_3Dlist):
            print(f"{i + 1}. {lst[0]}")
        print(SPACE)

        print("List Function Menu")
        self.show_list_name(self.operator_list)
        print(SPACE)

        # follow different number to act different tasks

        print("Please enter your action")
        while True:
            try:
                choice = int(input("Choice: "))
                if choice in range(1,6):
                    break
                else:
                    print("Please enter a valid choice!")
                    print("Please enter again")
            except ValueError:
                print("Please enter a valid choice!")
                print("Please enter again")
        if choice == 1:
            while True:
                name = input("List name: ")
                desc = input("Description: ")

                if len(name)>50 or len(desc)>250:
                    print("List cannot be longer than 50 characters!","current length",len(name))
                    print("Description cannot be longer than 250 characters!","current length",len(desc))
                    print("Please try again")
                elif len(name) == 0 or len(desc) == 0 :
                    print("List cannot be empty!")
                    print("Description cannot be empty!")
                    print("Please try again")

                else:
                    self.store_3Dlist.append([name, desc, []])
                    break

        elif choice == 2:
            if self.store_3Dlist:

                while True:
                    try:


                        index_operator = int(input("Remove which list (index): ")) - 1

                        if 0 <= index_operator < len(self.store_3Dlist):
                            self.store_3Dlist.pop(index_operator)
                            break

                        else:
                            print("Nothing to remove.")
                            print("Please try again")
                    except ValueError:
                        print("Invalid input.")
                        print("Please enter a number")
                        print("Please try again")
        elif choice == 3:
            if self.store_3Dlist:

                while True:
                    try:
                        index_operator = int(input("Check which list (index): ")) - 1
                        if index_operator < 0 or index_operator > len(self.store_3Dlist):
                            print("No list to Use")
                            print("Please try again")
                        else:
                            break
                    except ValueError:
                        print("Invalid input.")
                        print("Please try again")


                if 0 <= index_operator < len(self.store_3Dlist):

                    self.acted_list_check(index_operator)

                else:
                    # boundary the choice is valid.
                    print("Invalid index.")
                    print("Please try again")
            else:
                print("No lists to check.")
        elif choice == 4:
            while True:
                ensure=input("Please ensure you want to clear all data\nThe data cannot be returned\nPlease enter [yes/no]")
                if ensure == "yes":
                    self.store_3Dlist.clear()
                    break

                elif ensure == "no":
                    break

                else:
                    print("Please enter [yes/no]")

        elif choice == 5:
            # return 0 to break the loop
            return 0


        # return 1 to continue the loop
        return 1

# Function to show menu
def menu_show(menu):
    print("Welcome to TO DO LIST MENU")
    print("TO DO LIST APP\nMENU:\n")
    print("Warning: USERS MUST SELECT \"ENDING\" THE DATA CAN BE STORED ")
    for i, element in enumerate(menu):
        print(f"{i +1}.{element.upper()}")

# Function to show out the menu users can use
def menu_selected():
    while True:
        print(SPACE)

        try:
            menu_choice =int(input("please enter your choice[1-2]: "))
            # If the menu_choice is digit whether string type or int type , the return int(menu_choice)
            # but return 0 and run menu_selected function again
            if menu_choice in range(1,3):
                break
            else:
                print(f"Invalid choice.")
                print(f"Please try again")

        except ValueError:
            print(f"Invalid input.")
            print(f"Please try again")
    return menu_choice

def operator_list_recombine(list_name):
    new_list=[]
    gap_length=0
    gap=" "
    for operator in list_name:
        if len(operator)<20:
            block=" "*(20-len(operator))

            operator = f"{operator}{block}"
        operator=f"{gap*gap_length*3}{INTENT}{gap*(gap_length+2)}{operator}{gap*(gap_length-5)}{INTENT}"
        new_list.append(operator)
    return new_list


def main():
    # open and check if there is existed file , got the last data, if there is not existed file, open a new and data is empty
    store_3Dlist = []
    filename = "To_Do_List.txt"
    try:
        with open(filename, "r") as file:
            store_3Dlist = json.loads(file.read())

    # if it doesn't exist to do list text , it will create a empty list and create a new file '
    except (FileNotFoundError, JSONDecodeError):
        store_3Dlist = []

    # To store the all functions in these list and use class method to run the code
    item_check_menu = ["Remove", "Update", "Complete/State", "Mark", "Back"]
    item_check_menu=operator_list_recombine(item_check_menu)


    item_op_menu = ["Add New items", "Check Items", "Cancel All Items", "Back"]
    item_op_menu=operator_list_recombine(item_op_menu)
    item_op_cl = item_operator(item_op_menu, store_3Dlist, item_check_menu)

    list_op_menu = ["Add New List", "Remove List", "Check List", "Clear All Lists", "Back"]
    list_op_menu=operator_list_recombine(list_op_menu)
    list_check_menu = ["Update Info", "Show Detail", "Manage Items", "Back"]
    list_check_menu=operator_list_recombine(list_check_menu)
    list_op_cl = list_operator(list_op_menu, store_3Dlist, list_check_menu, item_op_cl)



    while True:
        print(SPACE)
        menu = ["START LIST","Ending"]
        menu=operator_list_recombine(menu)
        menu_show(menu)
        choice = menu_selected()
        # users can select to start a list , reading the negative and ending the process
        if choice == 1:

            list_op_cl.acted_list_operator()


        elif choice == 2:
            print("Exiting and Saving...")
            break

        # if user input an invalid choice
        else:
            print("Please select 1, 2")

        # update the filename and store new data
        with open(filename, "w") as file:
            json.dump(store_3Dlist, file)


# the function to run the process
if __name__ == "__main__":
    main()