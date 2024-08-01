import customtkinter as ctk
from tkinter import ttk
import os
from TopLevelAdd import TopLevel
from PIL import Image,ImageTk
from UpdateInterface import interface
import json

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("1450x1000")

        self.root.iconpath = ImageTk.PhotoImage(file="./images/fileIcon.jpg")
        #self.root.iconpath = ctk.CTkImage(light_image=Image.open("fileIcon.jpg"))


        self.root.wm_iconbitmap()
        self.root.iconphoto(False, self.root.iconpath)


        #Right Side of Window
        rightMainFrame = ctk.CTkFrame(self.root, width = 450, 
                                  height = 200, 
                                  fg_color = "grey23")
                                  
        rightMainFrame.pack(fill = "y", side = "right")

        rightMainFrame.pack_propagate(False)
        rightMainFrame.grid_propagate(False)


            #Right Frame Bottom Interior, no propagations
        rightMainFrameBot = ctk.CTkFrame(rightMainFrame, 
                                        width = 350, 
                                        height = 500, 
                                        #fg_color = "black"
                                        )
        
        rightMainFrameBot.pack(side = "bottom", pady = 30)
        rightMainFrameBot.pack_propagate(False)
        rightMainFrameBot.grid_propagate(False)
        
            #Temp picture to picture image of program
        tempPicture = ImageTk.PhotoImage(Image.open("./images/fileIcon.JPG").resize((400,400)))
        label = ctk.CTkLabel(rightMainFrame, image = tempPicture, text ="")
        label.pack(side ="top", padx = 30, pady = 30)        
        
        
        #Left Main Frame of window
        leftMainFrame = ctk.CTkFrame(self.root,  
                                  height = 200, 
                                  width= 1000,
                                  fg_color = "grey21")
                                  
        leftMainFrame.pack(fill = "both", expand = True, side = "left")







            #Top Frame with entry and search button. Separate comma for multi search. Also add file button to prompt new window.
        leftMainFrameTop = ctk.CTkFrame(leftMainFrame,  
                                  height = 60, 
                                  width= 700,
                                  fg_color = "thistle4")        
        leftMainFrameTop.pack(side = "top", fill = "both", padx = 30, pady = 20)
        leftMainFrameTop.pack_propagate(False)
        leftMainFrameTop.grid_propagate(False)

        entry = ctk.CTkEntry(leftMainFrameTop, 
                             width = 100, 
                             height = 30)
        entry.pack(side = "left", fill = "x", expand = True, padx = 10)



        #The Frame for the bottom left main frame
        
        leftMainFrameBot = ctk.CTkFrame(leftMainFrame,  
                                  height = 60, 
                                  width= 700,
                                  fg_color = "grey26")  
        leftMainFrameBot.pack(fill = "both", padx = 30, pady = 30, side = "bottom", expand = True)

        updateInterface = interface(leftMainFrameBot, rightMainFrame, rightMainFrameBot)
        
        #For use when prompting adding tags to files.
        addPrompt = TopLevel(self.root, updateInterface)








        addButton = ctk.CTkButton(leftMainFrameTop, 
                                     width = 100, 
                                     text = "Change", 
                                     height = 30,
                                     fg_color = "red3",
                                     hover_color = "firebrick4",
                                     command = lambda : addPrompt.open_toplevel())
        addButton.pack(side = "right", fill = "x", padx = 10)

        searchButton = ctk.CTkButton(leftMainFrameTop, 
                                     width = 100, 
                                     text = "Search", 
                                     height = 30, command = lambda: updateInterface.findFiles(str(entry.get())))
        searchButton.pack(side = "right", fill = "x", padx = 10)

        





            
        


















        self.root.mainloop()











