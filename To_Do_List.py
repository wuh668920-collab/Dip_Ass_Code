
# import json package to write and store the list in a text
import json
from json import JSONDecodeError




# use the SPACE with many dash to better show the process
SPACE = "--------------------------------------------------------------------------------------------------------------------"


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
        print(
            f"\n--- ITEM DETAILS ---\nName: {item[0]}\nTask: {item[1]}\nTime: {item[2]}\nState: {item[3]}\nMark: {item[4]}")

    # use function to update a particular item and changing its name and task
    def update_item(self, index_list, index_item):

        # the process allow use input a space if they don't need a name or task to the item'
        new_name = input("Enter new name (or skip): ")

        new_task = input("Enter new task (or skip): ")
        if new_name != "": self.store_3Dlist[index_list][2][index_item][0] = new_name
        if new_task != "": self.store_3Dlist[index_list][2][index_item][1] = new_task


    # use function to remove a particular item
    def remove_item(self, index_list, index_item):
        self.store_3Dlist[index_list][2].pop(index_item)
        # print item removed successfully to ensure the item is removed
        print("Item removed successfully.")
    # use function to change the state of the item if the user finish it
    def state_item(self, index_list, index_item):
        state = input("Complete? [Yes/No]: ").capitalize()

        if state == "Yes" :
             self.store_3Dlist[index_list][2][index_item][3] = "Completed"
        else:


            self.store_3Dlist[index_list][2][index_item][3] = "Uncompleted"
    # use the function to mark the item task
    def mark_item(self, index_list, index_item):
        mark = input("Give a mark (1-5 or description): ")
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

        # got the item name , item task, item deadline
        name = input("Item name: ")
        task = input("Task description: ")
        time = input("Time (eg. 12:00): ")

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
        if self.show_all_items(index_list):
            # to boundary the index_list
            try:
                index_operator= int(input("Select item index: ")) - 1
                if not (0 <= index_operator < len(self.store_3Dlist[index_list][2])):
                    print("Invalid index.")
                    return

                while True:
                    print(f"\nEditing: {self.store_3Dlist[index_list][2][index_operator][0]}")
                    for i, op in enumerate(self.item_check_list):
                        print(f"{i + 1}.{op}")

                    choice = int(input("Choice: "))
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
                    self.show_item_data(index_list, index_operator)
            except ValueError:
                print("Please enter a number.")

    def acted_item_operator(self, index_list):
        print(SPACE)
        self.show_list_name(self.operator_item)
        print(SPACE)
        try:
            choice = int(input(f"Choice[1-{len(self.operator_item)}]: "))
            if choice == 1:
                self.add_item(index_list)
            elif choice == 2:
                self.check_item_detail(index_list)
            elif choice == 3:
                self.store_3Dlist[index_list][2] = []
                print("All items cleared.")
            elif choice == 4:
                return 0
        except ValueError:
            print("Please enter a valid number.")
        return 1


class list_check(common_function):
    def __init__(self, list_check_list, store_3Dlist, item_op_cl):
        super().__init__()
        self.list_check_list = list_check_list
        self.store_3Dlist = store_3Dlist
        self.item_op_cl = item_op_cl

    def show_list_check_operator(self):
        for i, item in enumerate(self.list_check_list):
            print(f"{i + 1}.{item}")

    def acted_list_check(self, index_list):
        print(SPACE)
        print(f"List: {self.store_3Dlist[index_list][0]}")
        print(SPACE)
        self.show_list_check_operator()
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                new_name = input("New list name: ")
                if new_name: self.store_3Dlist[index_list][0] = new_name
            elif choice == 2:
                print(f"Description: {self.store_3Dlist[index_list][1]}")
            elif choice == 3:
                while True:
                    if self.item_op_cl.acted_item_operator(index_list) == 0:

                        break
            elif choice == 4:
                return 0
        except ValueError:
            print("Invalid input.")
        return 1


class list_operator(list_check):
    def __init__(self, operator_list, store_3Dlist, check_menu, item_op_cl):
        super().__init__(check_menu, store_3Dlist, item_op_cl)
        self.operator_list = operator_list
        self.store_3Dlist = store_3Dlist

    def acted_list_operator(self):
        print(SPACE)
        print("Current lists:")
        if not self.store_3Dlist:
            print("[Empty]")
        for i, lst in enumerate(self.store_3Dlist):
            print(f"{i + 1}. {lst[0]}")
        print(SPACE)

        self.show_list_name(self.operator_list)
        print(SPACE)
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                name = input("List name: ")
                desc = input("Description: ")
                self.store_3Dlist.append([name, desc, []])
            elif choice == 2:
                if self.store_3Dlist:
                    index_operator = int(input("Remove which list (index): ")) - 1
                    if 0 <= index_operator < len(self.store_3Dlist):
                        self.store_3Dlist.pop(index_operator)
                else:
                    print("Nothing to remove.")
            elif choice == 3:
                if self.store_3Dlist:
                    index_operator = int(input("Check which list (index): ")) - 1
                    if 0 <= index_operator < len(self.store_3Dlist):
                        while True:
                            if self.acted_list_check(index_operator) == 0: break
                else:
                    print("No lists to check.")
            elif choice == 4:
                self.store_3Dlist.clear()
            elif choice == 5:
                return 0
        except (ValueError, IndexError):
            print("Invalid selection.")
        return 1
# class to store compass functions

class compass:
    def __init__(self):
        pass



    def got_content(self):
        self.content=""
        with open("Compass_version1", "r") as file:
            self.content=file.read()
    def show_compass(self):
        self.got_content()
        print(SPACE)
        print(self.content)

# Function to show menu
def menu_show(menu):
    for i, element in enumerate(menu):
        print(f"{i + 1}.{element.upper()}")

# Function to show out the menu users can use
def menu_selected():
    print(SPACE)
    menu_choice = input("please enter your choice[1-3]: ")
    return int(menu_choice) if menu_choice.isdigit() else 0


def action_user():
    # open and check if there is existed file , got the last data, if there is not existed file, open a new and data is empty
    store_3Dlist = []
    filename = "To_Do_List.txt"
    try:
        with open(filename, "r") as file:
            store_3Dlist = json.loads(file.read())
    except (FileNotFoundError, JSONDecodeError):
        store_3Dlist = []

    # To store the all functions in these list and use class method to run the code
    item_check_menu = ["Remove", "Update", "Complete/State", "Mark", "Back"]
    item_op_menu = ["ADD NEW LIST", "Check Items", "Cancel All Items", "Back"]
    item_op_cl = item_operator(item_op_menu, store_3Dlist, item_check_menu)

    list_op_menu = ["Add New List", "Remove List", "Check List", "Clear All Lists", "Back"]
    list_check_menu = ["Update Info", "Show Desc", "Manage Items", "Back"]
    list_op_cl = list_operator(list_op_menu, store_3Dlist, list_check_menu, item_op_cl)



    while True:
        print(SPACE)
        menu = ["START LIST","Ending"]
        menu_show(menu)
        choice = menu_selected()
        # users can select to start a list , reading the negative and ending the process
        if choice == 1:
            while True:
                if list_op_cl.acted_list_operator() == 0:
                    break

        elif choice == 3:
            print("Exiting and Saving...")
            break

        # if user input an invalid choice
        else:
            print("Please select 1, 2, or 3.")

        # update the filename and store new data
        with open(filename, "w") as file:
            json.dump(store_3Dlist, file)


# the function to run the process
if __name__ == "__main__":
    action_user()