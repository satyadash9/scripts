import subprocess
import os

def repo_clone():
    subprocess.run(["git", "clone", "git@github.com:satyanarayanadash/project1.git"])
    return

def export_gitlog():
    repo_name = "/project1"
    cwd = os.getcwd()
    repo_path = cwd + repo_name
    os.chdir(repo_path)
    with open('gitlog.txt', 'w') as file:
        subprocess.run(["git", "log"], stdout=file, text=True)
    return

repo_clone()
export_gitlog()
