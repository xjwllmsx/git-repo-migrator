import os

# root_dir class
class RootDir:
    # Root dir name
    root_dir_folder = "gitea_repos"

    # Root dir path
    root_dir_path = f"./{root_dir_folder}"

    # List of sub directories in root folder
    root_sub_dirs = [sub_dir for sub_dir in os.listdir(root_dir_path)]

    # Number of subdirectories
    num_of_subs = len(root_sub_dirs)
