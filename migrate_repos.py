# Import RootDir class
from RootDir import RootDir

# Import create_repo_dict function
from create_repo_dict import create_repo_dict

# Import RemoteServer class
from RemoteServer import RemoteServer

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

for key in repos_dict:
    repo_name = repos_dict[key]["repo_name"]
    repo_path = repos_dict[key]["repo_path"]
    remote = RemoteServer(repo_name, repo_path)
    remote.check_remote_server()
    print("\n")
