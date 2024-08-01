import customtkinter as ctk
from tkinter import ttk
import os
import mainGUI
from PIL import ImageTk
import json

#root.geometry("") sets dimensions
#Use layout to get widgets into GUI
#principle is objects (widgets) inside of master objects (root)

#General Aesthetic listed below
ctk.set_appearance_mode("dark") # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#frame = customtkinter.CTkFrame(master=root_tk, width=200, height=200)

#Use top level for pop up



if __name__ == "__main__":
    root = ctk.CTk()
                #root.resizable(False, False)
    manager = mainGUI.FileManager(root)
    
    





