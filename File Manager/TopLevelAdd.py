import customtkinter as ctk
import tkinter
import os
from PIL import Image,ImageTk
from tkinter import ttk
import json
from UpdateInterface import interface


class TopLevel:
    def __init__(self, root, updateInterface):
        self.root = root
        self.topLevelWindow = None
        self.updateInterface = updateInterface
        #self.json = jsonData


    #Later Implement: add file parameter so can specify which file to change.
    def open_toplevel(self):
        if self.topLevelWindow is None or not self.topLevelWindow.winfo_exists():
            self.topLevelWindow = ctk.CTkToplevel(self.root)  # master argument is optional 

            self.topLevelWindow.grab_set()
            self.topLevelWindow.title("Add File")
        
            self.topLevelWindow.minsize(600,800)
            self.topLevelWindow.maxsize(600,800)

            #Adding Top Frame for picture
            self.topFrame = ctk.CTkFrame(self.topLevelWindow, 
                                    width = 350, 
                                    height = 300, 
                                    fg_color = "white")
            self.topFrame.pack(side ="top", padx = 50, pady = 30)

            #Adding bottom frame 
            bottomFrame = ctk.CTkFrame(self.topLevelWindow, 
                                    width = 500, 
                                    height = 350, 
                                    fg_color = "white")
            
            #stops frame from fitting into children widgets inside.
            bottomFrame.pack_propagate(False)
            bottomFrame.grid_propagate(False)

            bottomFrame.pack(side ="top", padx = 50, pady = 10, expand = True)

            #Displays image of file
            self.displayJSONImage()

            #Name of file
            name = ctk.CTkLabel(bottomFrame, 
                                width = 10, 
                                height = 10, 
                                text = "File Name: " + self.getJSONName(), 
                                text_color = "red",
                                anchor = "w",
                                font=("Helvetica", 18, "bold"))
            name.pack(pady = 5)

            #Tags
            tagName = ctk.CTkLabel(bottomFrame, 
                                width = 10, 
                                height = 10, 
                                text = "Tags", 
                                text_color = "red",
                                anchor = "w",
                                font=("Helvetica", 14, "bold"))
            tagName.pack(pady = 5)
                #textbox entry
            self.tags = ctk.CTkTextbox(bottomFrame, 
                                  width = 500, 
                                  height = 50)
            
            self.tags.insert("0.0", ', '.join(map(str, self.getJSONTags())))
            self.tags.pack(padx = 25)


            descriptionName = ctk.CTkLabel(bottomFrame, 
                                width = 10, 
                                height = 10, 
                                text = "Description", 
                                text_color = "red",
                                anchor = "w",
                                font=("Helvetica", 14, "bold"))
            descriptionName.pack(pady = 5)
                #textbox entry
            self.description = ctk.CTkTextbox(bottomFrame, 
                                  width = 500, 
                                  height = 185)
            
            self.description.insert("0.0", self.getJSONDescription())
            self.description.pack(padx = 25)




            #Submit and cancel button at bottom of entire topLevelFrame
            submit = ctk.CTkButton(self.topLevelWindow, 
                                   text = "Submit", 
                                   width = 100, 
                                   height = 30,
                                   fg_color= "green",
                                   hover_color = "darkgreen",
                                   #interface class
                                   command = lambda: self.updateJSON(self.updateInterface.selectItem())
                                   )
            submit.pack(side = "right", pady = 10, padx = 10)

            cancel = ctk.CTkButton(self.topLevelWindow, 
                                   text = "Cancel", 
                                   width = 100, 
                                   height = 30,
                                   fg_color= "red",
                                   hover_color = "red4",
                                   command = lambda: self.topLevelWindow.destroy()
                                   )
            cancel.pack(side = "right", pady = 10, padx = 10)

            

        #Kinda unneeded due to grab_set() which prevents clicking on main window   
        else:
            self.topLevelWindow.focus()  # if window exists focus it
            


    #note: might have to state command that makes file read from the JSON top after change. But as it 
    #reopens file every command, probably don't have to. Like iterator in jave.
        #closes topview also.

        #Also, gets rid of original tags, so have to get original JSON.
    def updateJSON(self, fileName):
        #Include original JSON text so won't repeat enter tags. Place above I believe, not in this method.


        #fileName orginates from interface class's method selectItem(), which returns none if no File is selected.
        if(fileName == None):
            print("No File Changed.")
            self.topLevelWindow.destroy()
            return
        
        inputTags = self.tags.get("1.0",'end-1c')
        inputDescription = self.description.get("1.0",'end-1c')


        #Open the file for reading 
        with open('fileData.json', 'r') as f: 
            data = json.load(f) 
        
        #Update the value, make it into sets for tags? 
        #Can't add previous tags, must put it in entry before hand.
        data[fileName]['description'] = inputDescription
        data[fileName]['tags'] = list(set(inputTags.replace(" ", "").lower().split(",")))
        
        #Open the file for writing and write the updated data 
        with open('fileData.json', 'w') as f: 
            json.dump(data, f, indent = 4) 
        

        self.updateInterface.updateMainFileInfo(fileName)
        self.topLevelWindow.destroy()

    def getJSONTags(self):
        fileName = self.updateInterface.selectItem()
        if(fileName != None):
            with open('fileData.json', 'r') as f: 
                data = json.load(f) 
            
            return data[fileName]["tags"]
        return ["N/A"]

    def getJSONDescription(self):
        fileName = self.updateInterface.selectItem()
        
        if(fileName != None):
            with open('fileData.json', 'r') as f: 
                data = json.load(f) 
            return data[fileName]["description"]
        
        return "N/A"
    
    def getJSONName(self):
        fileName = self.updateInterface.selectItem()

        if(fileName!= None):
            return fileName
        
        return "N/A"

    def displayJSONImage(self):
        fileName = self.updateInterface.selectItem()

        print("Called displayJSONImage")
        
        if(fileName != None):
            with open('fileData.json', 'r') as f: 
                data = json.load(f) 
                try:
                    my_image = ctk.CTkImage(light_image=Image.open(data[fileName]["image"]),
                                  size=(350,300))
                    image_label = ctk.CTkLabel(self.topFrame, image=my_image, text="")  # display image with a CTkLabel
                    image_label.pack()
                    print("Image activated")
                except:
                    print("Image not found")
                    print(data[fileName]["image"])


        
        


        







    