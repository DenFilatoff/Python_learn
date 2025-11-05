import sys
import json

with open('notebook.json', 'r') as fileRW:
    df = fileRW.read()
    df_dict = json.loads(df)
    

def allRec():
    count = 0
    print(f" {count} ")
    for key, value in df_dict.items():
        print(f" {count} ")
        count +=1
        print(f''' {count} {key} --- {value["name"]} -- {value["comment"]} -- {value["contact"]}''')


def bookmenu():
    try:
        print(''' Operation
             ------------------
             1) Print all contacts
             2) Search for people (by Name)
             3) Search for people (by Comment)
             4) Search for people (by Contact)
             5) Add new record
             6) Update record ( Name )
             7) Update record ( Comment )
             8) Update record ( Contact )
             9) Delete record 
             0) Exit
             ''')
        option = int(input("Please select an action: \t"))
        if option == 1:
            print("List all records:")
            allRec()
            bookmenu()
        elif option == 2:
            searchByName()
            bookmenu()
        elif option == 3:
            searchByComment()
            bookmenu()
        elif option == 4:
            searchByContact()
            bookmenu()
        elif option == 5:
            addNewRec()
            bookmenu()
        elif option == 6:
            keyforupdate = int(input("Input key for update:\t"))
            updateName(keyforupdate)
            bookmenu()
        elif option == 7:
            keyforupdate = int(input("Input key for update:\t"))
            updateComment(keyforupdate)
            bookmenu()
        elif option == 8:
            keyforupdate = int(input("Input key for update:\t"))
            updateContact(keyforupdate)
            bookmenu()
        elif option == 9:    
            deleteRec()
            bookmenu()
        elif option == 0:
            sys.exit();
            
        else:
            print("No such operation")
            bookmenu()
    except Exception as e:
        print(f"Exception done: {e}")


def addNewRec():
    newContactName = input("Enter Name:\t")
    newContactNumber = int(input("Enter Contact Number:\t"))
    newComment = input("Enter Comment:\t")
        # with open("directory.json", 'a') as fileAppend:
    df_dict[str(len(df_dict.keys()) + 1)] = {
            "name":newContactName,
            "contact":newContactNumber,
            "comment":newComment
        }
    
    fileRW.write(json.dumps(df_dict))
    print("Contact Added Successfully")
       
def deleteRec():
    key = input("Enter number of record to delete:\t")
    contact = df_dict.pop(key, "Key not found")
    print(f"Removed value: {contact}")  
    with open("notebook.json", "w") as fileR1:
        fileR1.write(json.dumps(df_dict))

 

def searchByName():
    name = input("Enter name for search:\t") 
    dc = {key: value for key, value in df_dict.items() if value["name"] == name}
    if len(dc):
        print(dc)
    else:
        print("Nothing found for ", name )
        
def searchByComment():
    comment = input("Enter comment for search:\t") 
    dc = {key: value for key, value in df_dict.items() if value["comment"] == comment}
    if len(dc):
        print(dc)
    else:
        print("Nothing found for ", comment )
        
    
def searchByContact():
    contact = int(input("Enter contact for search:\t"))
    dc = {key: value for key, value in df_dict.items()  if value["contact"] == contact}
    if len(dc):
        print(dc)
    else:
        print("Nothing found for ", contact )
        

def updateName(key):
    name = input("Enter new name for update:\t")
    df_dict[str(key)]["name"] = name
    with open("notebook.json", "w") as fileR:
        fileR.write(json.dumps(df_dict))
    print(f"Name Successfully Update to {name}")

def updateComment(key):
    comment = input("Enter new comment for update:\t")
    df_dict[str(key)]["comment"] = comment
    with open("notebook.json", "w") as fileR:
        fileR.write(json.dumps(df_dict))
    print(f"Comment Successfully Update to {comment}")    
    
def updateContact(key):
    contact = int(input("Enter new contact for update:\t"))
    df_dict[str(key)]["contact"] = contact
    with open("notebook.json", "w") as fileRead:
        fileRead.write(json.dumps(df_dict))
    print(f"Comment Successfully Update to {contact}")    
    
bookmenu()                  
