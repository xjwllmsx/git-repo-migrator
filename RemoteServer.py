# Import os
import os

# Import subprocess
import subprocess

# Import logging
import logging


# RemoteServer Class
class RemoteServer:
    def __init__(self, repo_name, repo_path):
        self.repo_name = repo_name
        self.repo_path = repo_path

    # Prints the current remote servers
    def check_remote_server(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename="test.log",
        )
        logging.info(f"Current remote servers for: '{self.repo_name}'")

        # Saves terminal output to a str variable
        self.output = subprocess.getoutput(f"cd {self.repo_path} && git remote -v")

        if "remote_mirror" in self.output:
            logging.info("This repo has a mirror")
            logging.info(f"{self.output}\n")
        elif "origin" in self.output:
            logging.info("This repo already has a remote")
            logging.info(f"{self.output}\n")
        elif "" in self.output:
            logging.info("This repo has no current remotes\n")

    # Removes remote server from repo
    def remove_remote_server(self):
        print(f"/nRemoving current remote servers for {self.repo_name}")
        os.system(f"cd {self.repo_path} && git remote remove origin")
