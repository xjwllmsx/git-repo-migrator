# Migrate Repos from Gitea to Soft Serve

The goal of this project is to automate the transfer of my repositories that were previously saved on my Gitea server, and move them to my new Soft Serve server.

For this project, I plan to use Python.

## Goals

~~1. Save repository to an accessible location (on local drive or an attached external hard drive)~~
~~2. Print that the program is about to begin~~
~~3. Print navigating to selected directory~~
~~4. Navigate to directory with repositories~~
~~5. Print number of directories (which will equal the total number of jobs) and save to a variable to recall later~~
~~6. Create a counter variable~~
**The following steps will be done for each directory:**
7. Print 'adding Soft Serve as remote'
8. Add Soft Serve server as the remote repository.
9. Print 'Soft Serve added successfully!'
10. Print 'Pushing repo to server'
11. Push each repository to the server
12. Print 'Repository was successfully pushed to Soft Serve server'
13. Add +1 to counter variable
14. Repeat this process for each directory
15. After the last repo, print '{counter} / {# of directories} successfully pushed to the Soft Serve server.
16. If counter == # of directories, print 'All repos have been successfully migrated to the server'
17. Else, print '{# of directories - counter} repos have not been migrated to the server
18. Terminate the program
