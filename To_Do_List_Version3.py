# This is version 3 to do list app
# compare to version 2 and version 1
# I have use colourize and tkinter to show my project
# more aesthetic and more useful

# import json to load and store data
import json
# import tkinter to show window
import tkinter as tk

# import messagebox and simpledialog is in order to choose yes or no
from tkinter import messagebox, simpledialog


#global variable to ensure the store filename
FIlE = "To_Do_List_version3.txt"


# Use load_data function to load current data and
def load_data():
    # use try to except if there is errors
    try:
        with open(FIlE, "r") as file:
            # use json to store data
            data= json.load(file)
            return data

    except:
        # if there is no current data or NoFounderFileError then data is empty
        data=[]
        return data
# Use save_data function to store new data
def save_data(data):
    with open(FIlE, "w") as file:
        json.dump(data, file)
class App:

    def __init__(self,root):
        # Ensure the size, background,title,data used and menu.
        self.root=root
        self.root.title("To_Dd_List App")#title name
        self.root.geometry("480x520")#size of screen
        self.root.config(bg="grey")#background of screen is white
        self.lists=load_data()#get data
        self.index_list=None#list index in data
        self.show_menu()

    # when a process has done, use clear_window to close last window

    def clear_window(self):
        # Remove every widget so we can draw a fresh screen
        for window in self.root.winfo_children():
            # to destroy the last window
            window.destroy()

    # use header to open a rectangle block
    def header(self,text,color="purple"):
        # Input a text, default colour is purple
        tk.Label(self.root,text=text,font=("Arial",16,"bold"),fg=color,bg="#f5f5f5").pack(pady=12)

    # use bottom_bar to open a rectangle to show add list and clear all lists
    def bottom_bar(self):
        #A block placed in the bottom of the window.
        bottom_frame=tk.Frame(self.root,bg="white",pady=10)
        #put the block in the bottom and fill in all  x-axis
        bottom_frame.pack(side="bottom",fill="x")
        return bottom_frame
    # initial window to show user start or not
    def show_menu(self):
        self.clear_window()
        self.index_list=None
        self.header("To_Dd_List")
        option_frame=tk.Frame(self.root)
        option_frame.place(relx=0.5,rely=0.5,anchor="center",)

        tk.Button(option_frame,text="Start",width=15,height=2,bg="white",font=("Helvetica",11,"italic"),command=self.show_dashboard).pack(pady=5)
        tk.Button(option_frame, text="Ending", width=15, height=2, bg="white",font=("Helvetica",11,"italic"), command=self.close_app).pack(pady=5)
    # if user do not want to start
    def close_app(self):
        print("Closing app........")
        self.root.destroy()

    # show the lists
    def show_dashboard(self):
        self.clear_window()
        self.index_list=None
        self.header("To_Dd_List")

        bottom_frame=tk.Frame(self.root,bg="white")
        bottom_frame.pack(fill="both", expand=True,padx=20)

        #if there is no lists in the data
        #
        if not self.lists:
            tk.Label(bottom_frame,text="Sorry, no lists yet.Please click Add List Button below",font=("Arial",11,"italic"),fg="black",bg="#f5f5f5").pack(pady=30)

        else:
            #if there are lists in the data, use loop and Frame to show
            for i,list in enumerate(self.lists):
                # create a row to show each list
                row=tk.Frame(bottom_frame,bg="#f5f5f5")
                row.pack(fill="x",pady=3)
                # to delect and check list
                tk.Button(row,text=f"  {i+1}.  {list['name']}  ({len(list['items'])} tasks)",font=("Arial",11,"italic"),anchor="w",bg="lightblue",width=40, command=lambda index_list=i:self.show_list(index_list)).pack(side="left")
                tk.Button(row,text="x",bg="red",command=lambda index_list=i: self.delete_list(index_list)).pack(side="left")

        # show add_list and clear_lists function by buttom bar
        bar=self.bottom_bar()
        tk.Button(bar,text="Add List",font=("Arial",11,"bold"),bg="lightblue",command=self.add_list).pack(side="left",padx=15)
        tk.Button(bar,text="Clear All",bg="orange",command=self.clear_lists).pack(side="right",padx=15)

    # function to add new list
    def add_list(self):
        name=simpledialog.askstring("New list","List name:")
        if name:
            self.lists.append({"name":name,"items":[]})
            save_data(self.lists)
            self.show_dashboard()
    # function to delete current list
    def delete_list(self,index_list):
        if messagebox.askyesno("Delect",f"Delect '{self.lists[index_list]['name']}'?"):
            self.lists.pop(index_list)
            save_data(self.lists)
            self.show_dashboard()
    # function to clar all current lists
    def clear_lists(self):
        if messagebox.askyesno("Clear lists","Delect All Lists?"):
            self.lists.clear()
            save_data(self.lists)
            self.show_dashboard()
    # function to show all current lists
    def show_list(self,list_index):
        self.clear_window()
        self.current=list_index
        list=self.lists[list_index]

        self.header(f"List: {list['name']}  ",color="purple")

        tk.Button(self.root,text="Rename list",command=self.rename_list).pack(side="left")

        frame=tk.Frame(self.root,bg="#f5f5f5")
        frame.pack(fill="both",expand=True,padx=20,pady=10)
        # if there is no tasks in the list
        if not list["items"]:
            tk.Label(frame,text="No task found in the list",font=("Arial",11,"italic"),fg="grey",bg="#f5f5f5").pack(fill="x",pady=2)
        #    show the complete or incomplete  by different colours
        else:
            for i ,task in enumerate(list["items"]):
                done=task["done"]
                symbol="!" if done else "o"
                color="green" if done else "red"

                row=tk.Frame(frame,bg="#f5f5f5")
                row.pack(fill="x",pady=2)

                tk.Button(row,text=f"{symbol},{task['name'] } -{task['description']}",font=("Arial",10),anchor="w",bg=color,width=38,command= lambda index=i:self.open_task(index)).pack(side="left")

        bar=self.bottom_bar()
        tk.Button(bar,text="Back",command=self.show_dashboard).pack(side="left",padx=10)
        tk.Button(bar,text="+ Add Task",font=("Arial",11,"bold"),bg="lightyellow",command=self.add_task).pack(side="right",padx=15)

    # function to  rename the list
    def rename_list(self):
        new=simpledialog.askstring("Rename","New list name:")
        if new:
            self.lists[self.current]["name"]=new
            save_data(self.lists)
            self.show_list(self.current)
    # function to add new task

    def add_task(self):
        name=simpledialog.askstring("Task Name","Task name:")
        if not name:
            return
        description=simpledialog.askstring("Task Description","Task description:(optional)")
        self.lists[self.current]["items"].append({"name":name,"description":description,"done":False,"mark":""})
        save_data(self.lists)
        self.show_list(self.current)

    # function to open the task to check it
    def open_task(self,index):
        li=self.current
        task=self.lists[li]["items"][index]
        # size and title and bg of the task window
        popup=tk.Toplevel(self.root)
        popup.title(task["name"])
        popup.geometry("300x300+160+160")
        popup.grab_set()
        popup.config(bg="white")

        status="Done" if task["done"] else "Pending"
        mark_text=task.get("mark","") or "No mark yet"
        # put the task as li in the window
        tk.Label(popup,text=task["name"].upper(),font=("Arial",13,"bold"),bg="white").pack(pady=10)
        tk.Label(popup,text=f"Description:{task['description']}\nStatus:{status}\nMark: {mark_text}",font=("Arial",10),bg="white",justify="left").pack(pady=5)

        # refresh when the data is changed
        def refresh():
            save_data(self.lists)
            popup.destroy()
            self.show_list(li)

        # change the state in done or incomplete

        def status_control():
            self.lists[li]["items"][index]["done"]=not task["done"]
            refresh()

        # function to control and get the mark.
        def mark_control():
            rating=simpledialog.askinteger("Mark Task","Give a mark or note (1~100)",parent=popup)
            if rating in range(1,101):
                if rating:
                    self.lists[li]["items"][index]["mark"]=rating
                    refresh()
            else:
                messagebox.showerror("Mark Error","Mark must be between 1 and 100")

        # function to get new name and new description of the current task
        def edit():
            nn=simpledialog.askstring("Edit name","Rename:",parent=popup)
            nt=simpledialog.askstring("Edit Task","Description:",parent=popup)
            if nn:self.lists[li]["items"][index]["name"]=nn
            if nt:self.lists[li]["items"][index]["description"]=nt
            refresh()
        # function to delete a current item
        def delete():
            self.lists[li]["items"].pop(index)
            refresh()

        # place these button to run functions
        tk.Button(popup,text="Done/Pending",command=status_control,width=28).pack(pady=6)
        tk.Button(popup,text="edit",command=edit,width=28).pack(pady=6)
        tk.Button(popup,text="Mark Rate",command=mark_control,width=28,bg="lightyellow").pack(pady=8)
        tk.Button(popup,text="Delete",command=delete,bg="pink").pack(pady=8)


# initial the project
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()