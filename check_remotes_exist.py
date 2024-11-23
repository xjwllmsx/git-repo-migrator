# Import subprocess module
import subprocess

# Import logging module
import logging


def check_remotes_exist(list):
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        filename="repo_migration.log",
    )

    mirrors = 0
    remote_exist = 0
    # Check if a remote exists
    for obj in list:
        # Store output from command
        output = subprocess.getoutput(f"cd {obj.dir_path} && git remote -v")
        # If a remote already exists
        if output:
            remote_exist += 1
            if "remote_mirror" in output:
                mirrors += 1
            logging.info(f"[{obj.repo_name}]")
            logging.info(f'{output}\n')

    if remote_exist > 0:
        print(
            f'There are currently {remote_exist} repos with existing remotes and {mirrors} {'are mirror repositories' if 0 == mirrors > 1 else 'is a mirror repository'}. All previous remotes have been logged for later review.'
        )
