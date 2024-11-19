# Import RootDir class
from RootDir import RootDir

# Import create_repo_dict function
from create_repo_dict import create_repo_dict

# Import RemoteServer class
from RemoteServer import RemoteServer

# Import logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="test.log",
)

# New RootDir object
root_dir = RootDir()

# Dictionary to store necessary repo info
repos_dict = create_repo_dict(root_dir.root_dir_path, root_dir.root_sub_dirs)

# Num of Repos
num_of_repos = root_dir.num_of_subs

# Print that the program is about to begin
logging.info("The program is now starting...\n")

# Print navigating to the selected directory
logging.info(f"Migrating repositories from '{root_dir.root_dir_folder}'...\n")

# Print number of repos to migrate
logging.info(f"There are a total of {num_of_repos} repos to migrate.\n")

for key in repos_dict:
    repo_name = repos_dict[key]["repo_name"]
    repo_path = repos_dict[key]["repo_path"]
    remote = RemoteServer(repo_name, repo_path)
    remote.check_remote_server()
    # print("\n")
