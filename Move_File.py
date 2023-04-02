import os
import shutil
#I have a doubt regarding this, it shows me an error:                                         ^
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#I followed the instructions of the project, yet this error shows up.

from_dir = "C:\Users\DELL\Downloads"
to_dir = "C:\Users\DELL\Documents\Downloaded_Files"
list_of_files = os.listdir(from_dir)

for file in list_of_files:
    fime_name,file_extension = os.path.splitext(file)

    if file_extension == "":
        continue

    if file_extension in [".txt'", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+file
        path2 = to_dir+"/"+"Dcoument_files"
        path3 = to_dir+"/"+"Dcoument_files"+"/"+file
        if os.path.exists(path2):
            print(file + "has been moved to Document Files in Documents")
            #Moves file to a different one that exist
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Folder Called document_files has been created in documents")
            print(file + "has been moved to Document Files in Documents")
            shutil.move(path1, path3)
