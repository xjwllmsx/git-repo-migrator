# Import Repo class
from Repo import Repo

# Import os module
import os

# Import set_root_dir
from set_root_dir import set_root_dir

# Root folder
root_dir = Repo()

# Initialize the root_dir
set_root_dir(root_dir)

# Create a list of subdirectories
list = root_dir.create_subdirs_list()


# Print list of subdirectories
def print_subdirs_list(list):
    counter = 1
    for obj in list:
        print(f"[{counter}] {obj.repo_name}")
        print(f"Path: {obj.dir_path}\n")
        counter += 1


# Removes indicated subdirectory
def remove_subdir(list, num):
    list.pop(num - 1)


print("\n")
print_subdirs_list(list)
confirm_subdirs = input(
    "Would you like to remove any of the listed subdirectories? \n[y/n]:"
)

if confirm_subdirs == "n" or confirm_subdirs == "y":
    if confirm_subdirs == "y":
        rm_subdir = input(
            f"Which subdirectory would you like to remove from the list? Enter a number between 1 - {len(list)}: "
        )
        if rm_subdir.isnumeric():
            remove_subdir(list, int(rm_subdir))
        else:
            print("Try again!")
    elif confirm_subdirs == "n":
        pass


# remove_subdir(list, 12)
print_subdirs_list(list)
