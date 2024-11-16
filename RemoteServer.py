# Import os
import os

# Import subprocess
import subprocess


# RemoteServer Class
class RemoteServer:
    def __init__(self, repo_name, repo_path):
        self.repo_name = repo_name
        self.repo_path = repo_path

    # Prints the current remote servers
    def check_remote_server(self):
        print(f"Current remote servers for: '{self.repo_name}'")

        # os.system(f"cd {self.repo_path} && git remote -v")

        # Saves terminal output to a str variable
        self.output = subprocess.getoutput(f"cd {self.repo_path} && git remote -v")

        if "remote_mirror" in self.output:
            print("This repo has a mirror")
            print(self.output)
        elif "origin" in self.output:
            print("This repo already has a remote")
            print(self.output)
        elif "" in self.output:
            print("This repo has no current remotes")

    # Removes remote server from repo
    def remove_remote_server(self):
        print(f"/nRemoving current remote servers for {self.repo_name}")
        os.system(f"cd {self.repo_path} && git remote remove origin")
