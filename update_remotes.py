# Import os module
import os

# Import logging
import logging

# Import subprocess
import subprocess


def update_remotes(list):
    new_remote_url = input("Enter the URL for the new repository server: ")

    condition_1 = True
    while condition_1:
        correct_url = input(f'You entered "{new_remote_url}", is this correct? [y/n]: ')
        if correct_url == "y":
            condition_1 = False

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="repo_migration.log",
    )

    print("Starting migration process...")

    for obj in list:
        # Store repo name
        repo_name = obj.repo_name

        # Store repo's directory location
        repo_path = obj.dir_path

        # Inform user of which repo is being updated
        print(f'Updating remotes for "{repo_name}"...')

        # Look for existing remotes
        output = subprocess.getoutput(f"cd {obj.dir_path} && git remote -v")

        # If there are existing remotes
        if output:
            # Log remote removal
            logging.info(f'Removing existing remotes for "{repo_name}"...')
            # Move working directory to repo's directory and remove existing remote
            os.system(f"cd {repo_path} && git remote rm origin")

        # Add new remote
        os.system(
            f"cd {repo_path} && git remote add origin {new_remote_url}/{repo_name}.git"
        )

        # Log update
        logging.info(f'Updated remote for "{repo_name}" to {new_remote_url}')

        # Verify repo's remote has been updated
        remote_repos = subprocess.getoutput(f"cd {repo_path} && git remote -v")

        # Log verification
        if new_remote_url in remote_repos:
            logging.info(f'Verified remotes for "{repo_name}" has been updated')
            # Push repo to new server
            os.system(f"cd {repo_path} && git push --set-upstream origin main")
            # Log update
            logging.info(
                f'"{repo_name}" has been successfully pushed to {new_remote_url}/{repo_name}.git'
            )

        else:
            logging.info(
                f'The remotes for "{repo_name}" did not pass verification. You may need to manually check that the remote has been updated'
            )

        # Inform user of successful remote
        print(f'Successfully updated remotes for "{repo_name}"')

        logging.info("\n")
