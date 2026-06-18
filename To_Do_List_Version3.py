# This is version 3 to do list app
# compare to version 2 and version 1
# I have use colourize and tkinter to show my project
# more aesthetic and more useful

import json
import tkinter as tk

from tkinter import messagebox, simpledialog

FIlE = "To_Do_List.txt"


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
        self.root=root
        self.root.title("To_Dd_List App")#title name
        self.root.geometry("480x520")#size of screen
        self.root.config(bg="grey")#background of screen is white
        self.lists=load_data()#get data
        self.index_list=None#list index in data
        self.show_menu()


    def clear_window(self):
        # Remove every widget so we can draw a fresh screen
        for window in self.root.winfo_children():
            window.destroy()

    def header(self,text,color="purple"):
        # Input a text, default colour is purple
        tk.Label(self.root,text=text,font=("Arial",16,"bold"),fg=color,bg="#f5f5f5").pack(pady=12)

    def bottom_bar(self):
        #A block placed in the bottom of the window.
        bottom_frame=tk.Frame(self.root,bg="white",pady=10)
        #put the block in the bottom and fill in all  x-axis
        bottom_frame.pack(side="bottom",fill="x")
        return bottom_frame
    def show_menu(self):
        self.clear_window()
        self.index_list=None
        self.header("To_Dd_List")
        option_frame=tk.Frame(self.root)
        option_frame.place(relx=0.5,rely=0.5,anchor="center",)

        tk.Button(option_frame,text="Start",width=15,height=2,bg="white",font=("Helvetica",11,"italic"),command=self.show_dashboard).pack(pady=5)
        tk.Button(option_frame, text="Ending", width=15, height=2, bg="white",font=("Helvetica",11,"italic"), command=self.close_app).pack(pady=5)

    def close_app(self):
        print("Closing app........")
        self.root.destroy()


    def show_dashboard(self):
        self.clear_window()
        self.index_list=None
        self.header("To_Dd_List")

        bottom_frame=tk.Frame(self.root,bg="white")
        bottom_frame.pack(fill="both", expand=True,padx=20)

        #if there is no lists in the data
        if not self.lists:
            tk.Label(bottom_frame,text="Sorry, no lists yet.Please click Add List Button below",font=("Arial",11,"italic"),fg="white",bg="#f5f5f5").pack(pady=30)

        else:
            #if there are lists in the data, use loop and Frame to show
            for i,list in enumerate(self.lists):
                # create a row to show each list
                row=tk.Frame(bottom_frame,bg="#f5f5f5")
                row.pack(fill="x",pady=3)
                # to delect and check list
                tk.Button(row,text=f"  {i+1}.  {list['name']}  ({len(list['items'])} tasks)",font=("Arial",11,"italic"),anchor="w",bg="lightblue",width=40, command=lambda index_list=i:self.show_list(index_list)).pack(side="left")
                tk.Button(row,text="x",bg="red",command=lambda index_list=i: self.delete_list(index_list)).pack(side="left")

        bar=self.bottom_bar()
        tk.Button(bar,text="Add List",font=("Arial",11,"bold"),bg="lightblue",command=self.add_list).pack(side="left",padx=15)
        tk.Button(bar,text="Clear All",bg="orange",command=self.clear_lists).pack(side="right",padx=15)


    def add_list(self):
        name=simpledialog.askstring("New list","List name:")
        if name:
            self.lists.append({"name":name,"items":[]})
            save_data(self.lists)
            self.show_dashboard()

    def delete_list(self,index_list):
        if messagebox.askyesno("Delect",f"Delect '{self.lists[index_list]['name']}'?"):
            self.lists.pop(index_list)
            save_data(self.lists)
            self.show_dashboard()

    def clear_lists(self):
        if messagebox.askyesno("Clear lists","Delect All Lists?"):
            self.lists.clear()
            save_data(self.lists)
            self.show_dashboard()

            


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()