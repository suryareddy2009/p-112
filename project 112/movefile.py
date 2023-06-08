import os
import shutil
from_dir="C:/Users/Subhash/downloads"
to_dir="C:/Users/Subhash/downloads/di"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for i in list_of_files:
    name,ext=os.path.splitext(i)
   # print(name)
   # print(ext)
    if ext =="":
        continue
    if ext in [".txt, .doc, .docx, .pdf"]:
        path1=from_dir+"/"+i
        path2=to_dir+"/"+"imagefiles"
        path3=to_dir+"/"+"imagefiles"+"/"+i
        if os.path.exists(path2):
            print("moving"+i+".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+i+"...")
            shutil.move(path1,path3)
        