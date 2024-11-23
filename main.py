# Import Repo class
from Repo import Repo

# Import os module
import os

# Import set_root_dir
from set_root_dir import set_root_dir

# Import eval_subdir
from eval_subdir import eval_subdir

# Root folder
root_dir = Repo()

# Initialize the root_dir
set_root_dir(root_dir)

# Create a list of subdirectories
list = root_dir.create_subdirs_list()

# Prints subdirectories and removes any subdirectories from the list
eval_subdir(list)
