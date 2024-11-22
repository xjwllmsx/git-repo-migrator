import os


# Asks user for root directory information
def set_root_dir(root_dir):
    root_dir.repo_name = input("Enter name of directory: ")
    root_dir.root_path = input("Enter the root directory's path: ")
    root_dir.dir_path = f"{root_dir.root_path}/{root_dir.repo_name}"

    # Condition statement
    everything_is_correct = False

    while not everything_is_correct:
        # Verify the root's path with the user
        correct_root_path = input(
            f'Is this the correct path for the directory: "{root_dir.dir_path}" \n[y/n]: '
        ).lower()

        # If the user entered a valid response
        if correct_root_path == "n" or correct_root_path == "y":
            # If the root path is NOT correct
            if correct_root_path == "n":
                set_root_dir(root_dir)

            # If the root path is correct
            elif correct_root_path == "y":
                # If the directory does not exist
                if not os.path.isdir(root_dir.dir_path):
                    print(
                        f'"{root_dir.repo_name}" does not exist. Please double check the root directory name and path.'
                    )
                    set_root_dir(root_dir)
                # If the directory exists
                else:
                    print(
                        f'Great! Locating all subdirectories of "{root_dir.repo_name}"'
                    )

            # Change condition
            everything_is_correct = True

        # For all invalid entries
        else:
            print("Not a valid response.")
