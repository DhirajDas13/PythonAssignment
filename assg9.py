import os

def file_size(file_path):
    
    my_list= os.listdir(file_path)
    for i in my_list: 
        path=file_path+"\\"+i
        file_info = os.stat(path)
        if file_info.st_size == 0:        
            print (i)
            
file_path = r"C:\Users\dh319684\Documents\Python"
file_size(file_path)