import os


def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/Users/euijin/dev/python/Programming Fundations with Python/01.rename_files/minsook")
    print (file_list)

    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"/Users/euijin/dev/python/Programming Fundations with Python/01.rename_files/minsook")

    # (2) for each file, rename filename
    for file_name in file_list:
        print ("Old Name - " + file_name)
        new_file_name = file_name.translate(None, "0123456789")

        print ("New Name - " + new_file_name)
        os.rename(file_name, new_file_name)
    os.chdir(saved_path)


rename_files()
