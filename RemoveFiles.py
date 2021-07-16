#importing all modules
import os
import shutil
import time

#input from the user
pathOfFolder = input("Enter the path of the folder: ")
numberOfDays = float(input("How many days older files you want to keep in this path: "))
#converting the input day from the user to seconds
numberOfDays = numberOfDays*24*60*60
#current seconds from epoch of computers
now = time.time()


if(os.path.exists(pathOfFolder)):   # if the files exists
    allFiles = os.walk(pathOfFolder)    # storing all root, directories and files in allFiles       
    for (root, directories, files) in allFiles:     
        for (directory) in directories:
            directoryPath = os.path.join(root, directory)
            directoryCreatedTime = os.stat(directoryPath).st_ctime
            directoryDeleteTime = directoryCreatedTime + numberOfDays    
            if(directoryDeleteTime - now) > 0:
                print("Not deleting ", directoryPath)
            else:
                print("Deleting ", directoryPath)
                shutil.rmtree(directoryPath)
        
        for(files) in files:
            filePath = os.path.join(root, files)
            fileCreatedTime = os.stat(filePath).st_ctime
            fileDeleteTime = fileCreatedTime + numberOfDays
            if(fileDeleteTime - now) > 0:
                print("Not deleting ", filePath)
            else:
                print("Deleteds ", filePath)
                os.remove(filePath)
            
            
else:
    print("Not found")