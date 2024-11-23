# Import Repo class
from Repo import Repo

# Import set_root_dir
from set_root_dir import set_root_dir

# Import eval_subdir
from eval_subdir import eval_subdir

# Import check_remotes_exist module
from check_remotes_exist import check_remotes_exist

# Import update_remotes module
from update_remotes import update_remotes

# Root folder
root_dir = Repo()

# Initialize the root_dir
set_root_dir(root_dir)

# Create a list of subdirectories
list = root_dir.create_subdirs_list()

# Prints subdirectories and removes any subdirectories from the list
eval_subdir(list)

# Looks for existing remotes and logs them
check_remotes_exist(list)

# Update Remotes
update_remotes(list)