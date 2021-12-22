import os 
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_file_count = 0
    
    path = input("Enter your path")
    mins = 10
    seconds = time.time()-(mins*60)
    
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds <= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders_count +=1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if seconds <= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count +=1
                        
                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if seconds <= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_file_count +=1
        else:
            if seconds <= get_file_or_folder_age(path):
                remove_file(path)
                deleted_folders_count +=1
                
    else:
        print(f"{path} is not found")
    print ("Total files deleted",deleted_file_count)
    print ("Total folders deleted",deleted_folders_count)        
        
            

def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed succesfully")
        
    else:
        print("Unable to remove file succesfully")
        
def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is succesfully removed")
    else:
        print("Unable to remove the folder succesfully")
        
        
def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

main()
