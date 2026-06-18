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
