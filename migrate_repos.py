# Import RootDir class
from RootDir import RootDir
from create_repo_dict import create_repo_dict

# New RootDir object
root_dir = RootDir()

# Dictionary to store necessary repo info
repos_dict = create_repo_dict(root_dir.root_dir_path, root_dir.root_sub_dirs)

# Num of Repos
num_of_repos = root_dir.num_of_subs

# Print that the program is about to begin
print("The program is now starting...")

# Print navigating to the selected directory
print(f"Migrating repositories from '{root_dir.root_dir_folder}'...")

# Print number of repos to migrate
print(f"There are a total of {num_of_repos} repos to migrate.")
