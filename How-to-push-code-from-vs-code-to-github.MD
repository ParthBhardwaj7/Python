# Pushing code from VS Code to GitHub involves a few steps
## 1. Install Git
* Ensure Git is installed on your system.
* Download Git and install it.
* To verify, run this command in your terminal:
```
git --version
```
![Image](https://github.com/user-attachments/assets/607d06e0-113b-4892-a497-0a38cbdf29d4)
## 2. Configure Git (First-Time Setup)
* Set your name and email in Git:
```
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
## 3. Create a GitHub Repository
* Go to GitHub and log in.
* Click the + icon in the top-right corner and select New repository.
* Name your repository and optionally initialize it with a README file.
## 4. Open Your Project in VS Code
* Open your project folder in VS Code.
* If your project isn’t already a Git repository, initialize it:
* Open the VS Code terminal and run:
```
git init
```
## 5. Link Your Project to the GitHub Repository
* Copy the repository URL from GitHub:
* Go to your GitHub repository.
* Click the Code button and copy the HTTPS or SSH URL.
* In the VS Code terminal, link the repository:
```
git remote add origin <repository-URL>
```
## 6. Add and Commit Your Changes
* Stage your changes:
```
git add .
```
* Commit your changes with a message:
```
git commit -m "Initial commit"
```
## 7. Push Code to GitHub
* Push your code to the main branch (or the branch you’re using):
```
git branch -M main
git push -u origin main
```
## 8. Verify the Push
* Go to your GitHub repository, and you should see your code!

# If Error Occurs:
![Image](https://github.com/user-attachments/assets/32f0f29a-b3b9-4464-8c35-5226e04ac699)
## 1. Pull Changes from the Remote Repository
* Run the following command in your terminal to fetch and merge the changes from the remote repository into your local branch:

```
git pull origin main --rebase
```
* What This Does:
* git pull: Fetches the changes from the remote repository.
* origin main: Specifies the remote (origin) and branch (main).
* --rebase: Applies your local changes on top of the remote changes to avoid conflicts.
## 2. Resolve Any Merge Conflicts (If Applicable)
* If there are conflicts, Git will notify you.
* Open the conflicted files in VS Code, resolve the conflicts, and then stage the changes:
```
git add <file-name>
```
* After resolving all conflicts, continue the rebase process:
```
git rebase --continue
```
## 3. Push Your Changes to GitHub
* Once the pull is successful and conflicts (if any) are resolved, push your changes:

```
git push origin main
```


![Image](https://github.com/user-attachments/assets/d0e7ca72-6f0d-4f7e-96c2-946d1bd8d6ae)
