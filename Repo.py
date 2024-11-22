class Repo:
    def __init__(self):
        self._repo_name = ""
        self._root_path = "."
        self._dir_path = ""

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
    
    def set_root_path(self, path):
        self._root_path = path

    def get_root_path(self):
        return self._root_path
    
    repo_name = property(get_repo_name, set_repo_name)

    dir_path = property(get_dir_path, set_dir_path)

    root_path = property(get_root_path, set_root_path)