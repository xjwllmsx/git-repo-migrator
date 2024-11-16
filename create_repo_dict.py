def create_repo_dict(root_repo_path, sub_dirs_list):
    # Dictionary for repo info
    repo_dict = {}

    # Number for repos_dict key
    key_num = 1

    # Loop through sub_dirs_list
    for dirs in sub_dirs_list:
        # Subdirectory name
        dir_name = dirs[:-4]

        # Subdirectory path
        dir_path = f"{root_repo_path}/{dirs}/"

        # Add subdirectory information to dictionary
        repo_dict[key_num] = {"repo_name": dir_name, "repo_path": dir_path}

        # Increase the dictionary key by 1 each iteration
        key_num += 1

    return repo_dict
