import customtkinter as ctk
from tkinter import ttk
import os
from PIL import Image,ImageTk
import json

#Interface for leftMainFrameBot that updates all the files.
class interface():
    def __init__(self, leftFrame, rightFrameTop, rightFrameBot):
        self.leftFrame = leftFrame
        self.rightFrameTop = rightFrameTop
        self.rightFrameBot = rightFrameBot

         #Populates rightMainFrameBot with intel
        self.name = ctk.CTkLabel(self.rightFrameBot, text = "Name: ")
        self.name.pack()
        #Could also do a for loop to make a label for each individual tag
        self.tags = ctk.CTkLabel(self.rightFrameBot, text = "Tags: ")
        self.tags.pack()

        self.description = ctk.CTkLabel(self.rightFrameBot, text = "Description: ")
        self.description.pack()
    
        #Lists out the files in folder and shows it in leftMainFrame
        self.treeview = ttk.Treeview(leftFrame, height=50, columns = ("Files"), show="tree")
        self.treeview.pack(fill = "both")

        ###Treeview Customisation (theme colors are selected)
        bg_color = leftFrame._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = leftFrame._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = leftFrame._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", 
                            background=bg_color, 
                            foreground=text_color, 
                            fieldbackground=bg_color, 
                            borderwidth=0, 
                            font = ("roboto", 20),
                            rowheight=36)

        #bg_color
        treestyle.map('Treeview', background=[('selected', "gray25")], foreground=[('selected', selected_color)])

       
        #Adds all the files in the directory on startup
        self.addAllFiles()
            

        self.treeview.bind("<Double-1>", lambda a: self.onDoubleClick())
        self.treeview.bind('<ButtonRelease-1>', lambda a: self.selectItem())

        #Helps with single
        #tree.bind('<ButtonRelease-1>', selectItem)
        

    def addAllFiles(self):
        
        #Use Tree View
        #On launch, fill frame --> treeview with files.
        with open ("./fileData.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print("Empty or invalid JSON file. Initializing with default data.")
                    data = {}

        #Tags is a list of tags associated with each object, perfect.
        for fileName in os.listdir("./Files"):
            #The "" specify its parents
    
            
            #Appends data into JSON FILE
            if fileName not in data:
                #Open the file for reading 
                #Update dictionary to fill with fileNames not in JSON. 
                data.update({
                    fileName : {
                        "name" : fileName,
                        "tags" : [fileName.split(".")[1].lower()],  #Add "" to everything so when search "" it finds it.
                        "description" : "N/A",
                        "image" : self.imageType(fileName)
                    }
                })

                
        
            
            if fileName in data:
                
                self.treeview.insert('', 
                                'end', 
                                iid = fileName, 
                                text = fileName, 
                                tags = data.get(fileName).get("tags"))
                    
                

        # Open the file for writing and write the updated data to JSON
            with open('fileData.json', 'w') as f: 
                json.dump(data, f, indent =4) 



        #Note: try to include something that deletes fileData from json if removed from file.
        #
        #
        #
        #
        #
        #                           not added
        #
        #
        #





    #Find desginated tags. Checks every children if have tags or else hide it.
    def findFiles(self, entryString):
        tagList = entryString.replace(" ","").split(",")
        self.clearAll()

        #Checks if no tags are inputted, if so, then show everything.
        #If search bar = none, call show all files.
        if not entryString:
            self.addAllFiles()
            
    
        else: 
            #Issue is that if multiple searches, won't search through all the files. FIX THAT.
            self.addAllFiles()
            children = self.treeview.get_children()
            
        
            for child in children:
                
                if(not set(tagList).issubset(self.treeview.item(child)["tags"])):
                    print("Deleted Items")
                    self.treeview.delete(child)

                   
    def imageType(self, fileName):
        #Gets the type of file (ex. pdf, txt, jpg, etc.)
        type = fileName.split(".")[1].lower()

        #Returns location of image to show or show type representation.
            #If find out how to get preview image of files, implement and remove this.
        match type:
            case "jpg":
                return "./Files/" + fileName
            
            case "png":
                return "./Files/" + fileName
            
            case "jfif":
                return "./Files/" + fileName
            
            case "mp4":
                return "./images/mp4 image.png"
            
            case "pdf":
                return "./images/pdf picture.png"
            
            case "txt":
                return "./images/text image.png"
            
            case "zip":
                return "./images/zip file.jfif"
            
            case default:
                return "./images/can't find.png"
        
    #Clears all the children
    def clearAll(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)


    #Use this to select item and change it.
    def selectItem(self):
        selected = self.treeview.focus()

        #If none selected, selected = "", so code won't activate
        if(selected != ""):
            print("Selected item!")
            
            treeItem = self.treeview.item(selected)["text"]
            self.updateMainFileInfo(treeItem)
            return treeItem
        return None
        
    #Use curItem = tree.focus() to find single clikc I believe or just use bind (single-1) or something.
    def onDoubleClick(self):


        selected = self.treeview.focus()
        
        print(self.treeview.item(selected)["text"])

        path = ".\\Files\\" + self.treeview.item(selected)["text"]

        os.startfile(path)
        #item = self.treeview.selection()[0]
        #print(self.treeview.item(item,"text"))
         
    def updateTreeView(self):
        pass
        
    def updateMainFileInfo(self, fileName):

        with open('fileData.json', 'r') as f: 
            data = json.load(f) 

        if(fileName != ""):
            self.name.configure(text = "Name: " + fileName) 
            self.description.configure(text = "Description: " + data[fileName]["description"])
            self.tags.configure(text = "Tags: " + str(data[fileName]["tags"]))
            print(fileName)

        













