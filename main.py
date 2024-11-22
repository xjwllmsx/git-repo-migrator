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

list = root_dir.create_subdirs_list()


# def print_subdirs_list(list):


for obj in list:
    print(f"\n{obj.repo_name}:")
    print(obj.dir_path)

print(len(list))
popped_item = list.pop(3)
print(len(list))
print(popped_item.repo_name)

# print(list[4-4].repo_name)
