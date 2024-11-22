import os


class Repo:
    def __init__(self):
        self._repo_name = ""
        self._root_path = "."
        self._dir_path = ""
        self._sub_dirs = []
        # self._num_of_subdirs = 0

    # Set Repo Name
    def set_repo_name(self, name):
        self._repo_name = name

    # Get Repo Name
    def get_repo_name(self):
        return self._repo_name

    # Set Repo Path
    def set_dir_path(self, path):
        self._dir_path = path

    # Get Repo Path
    def get_dir_path(self):
        return self._dir_path

    # Set Root Path for Repo
    def set_root_path(self, path):
        self._root_path = path

    # Get Root Path for Repo
    def get_root_path(self):
        return self._root_path

    # Create a list with all subdirectories
    def create_subdirs_list(self):
        # Create list with all directory
        for dirs in os.listdir(self.dir_path):
            repo = Repo()
            repo.repo_name = dirs[:-4]
            repo.root_path = self.dir_path
            repo.dir_path = f"{repo.root_path}/{dirs}"
            self._sub_dirs.append(repo)
        
        # self._num_of_subdirs = len(self._sub_dirs)

        # Return list
        return self._sub_dirs
    
    # # Get number of subdirectories
    # def get_num_of_subdirs(self):
    #     return self._num_of_subdirs

    repo_name = property(get_repo_name, set_repo_name)

    dir_path = property(get_dir_path, set_dir_path)

    root_path = property(get_root_path, set_root_path)

    # num_of_subdirs = property(get_num_of_subdirs)