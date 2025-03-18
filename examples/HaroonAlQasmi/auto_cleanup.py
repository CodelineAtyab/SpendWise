import os

given_directory = input("Enter a valid directoty path:")
given_directory_list = os.listdir(given_directory)
new_dir_list = []
for dir in given_directory_list: # the following loops are used to scan the files so we can create new directories for each group of them
    new_dir = ""
    for char in reversed(dir):
        if char == ".":
            break
        new_dir = char + new_dir
    new_dir_list.append(new_dir)
new_dir_list = list(set(new_dir_list))
for path in new_dir_list:
    new_path = given_directory + "/" + path
    os.mkdir(new_path)

