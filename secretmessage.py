import os
def rename_files():
    #(1) get the file names form a folder
    file_list = os.listdir(r"C:/users/rd176h/Documents/GitWorkspace/udacity/prank")
    print(file_list)

    #Ensuring that the images are being renamed in the appropriate Directory
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:/users/rd176h/Documents/GitWorkspace/udacity/prank")

    #Iterating over the file list to rename them
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
