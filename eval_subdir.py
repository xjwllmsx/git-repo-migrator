def eval_subdir(list):
    # Print list of subdirectories
    def print_subdirs_list():
        counter = 1
        for obj in list:
            print(f"[{counter}] {obj.repo_name}")
            print(f"Path: {obj.dir_path}\n")
            counter += 1

    # Removes indicated subdirectory
    def remove_subdir(num):
        list.pop(num - 1)

    # Outer loop condition
    condition_1 = True
    while condition_1:
        # Stores the list length
        list_len = len(list)
        # Print the subdirectories
        print_subdirs_list()
        # Ask user if they want to remove any of the listed subdirectories
        rm_subdir = input(
            f'To remove a subdirectory from the list, select a number between 1-{list_len}, or select "0" to continue without removing a subdirectory: '
        )
        # For valid inputs
        try:
            # Stores the user input as an integer
            selection = int(rm_subdir)
            # If the user selected "0"
            if selection == 0:
                print("Moving on...")
                # End while loop
                condition_1 = False
            # If the user entered a number from the list
            elif 0 < selection <= list_len:
                # Condition for inner loop
                condition_2 = True
                # Store the name of the subdirectory the user wants to remove
                subdir_to_remove = list[selection - 1].repo_name
                while condition_2:
                    # Ask user if they are sure they want to remove the subdirectory
                    confirm_removal = input(
                        f'Are you sure you would like to remove "{subdir_to_remove}"? [y/n]: '
                    )
                    # If they DO NOT want to remove the subdirectory
                    if confirm_removal == "n":
                        # End while loop
                        condition_2 = False
                    # Continue with subdirectory removal
                    elif confirm_removal == "y":
                        print(f'Removing "{subdir_to_remove}"')
                        remove_subdir(selection)
                        print(f'"{subdir_to_remove}" has been removed')
                        # End while loop
                        condition_2 = False
                    # For all invalid inputs
                    else:
                        print('Invalid input. Please enter "y" or "n"')
            # For inputs out of range
            else:
                print("You did not input a valid number. Please try again.")
        # For non-integer inputs
        except ValueError:
            print("That is not an integer. Please try again.")
