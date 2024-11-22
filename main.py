from Repo import Repo
import os

# print(repo.repo_name)

# repo.url = 'google.com'
# print(repo.url)

# test_dict = {}

# for dirs in os.listdir("./gitea_repos"):
#     print(dirs[:-4])
#     dirs_name = dirs[:-4]
#     dirs_path = f"./gitea_repos/{dirs}/"
#     test_obj = Repo(dirs_name, dirs_path)
#     count = 1
#     test_dict[dirs_name]= dirs_path
#     count += 1

# print(test_dict)

# Root folder
root_folder_name = Repo()
root_folder_name.repo_name = input('Enter name of directory: ')
root_folder_name.root_path = input("Enter the root directory's path: ")
root_folder_name.dir_path = f"{root_folder_name.root_path}/{root_folder_name.repo_name}"

verify = input(f'Is this the correct path for the directory: "{root_folder_name.dir_path}" \n[y/n]: ').lower()

if verify == 'n':
    root_folder_name.set_repo_name(input('Enter name of directory: '))
    root_folder_name.set_root_path(input("Enter the root directory's path: "))
    root_folder_name.set_dir_path(f"{root_folder_name.root_path}/{root_folder_name.repo_name}") 
elif verify == 'y':
    print('Great!')
else:
    print('Not a valid response.')
# # Create list with all directory 
# for dirs in os.listdir("./gitea_repos"):
#     list.append(Repo(dirs[:-4],f"./gitea_repos/{dirs}"))

# for obj in list:
#     print(f"\n{obj.repo_name}:")
#     print(obj.repo_path)

# print(list[1].repo_name)
print(root_folder_name.dir_path)
print(os.path.isdir(root_folder_name.dir_path))