import subprocess
import os

clone_cmd = str("git clone git@github.com:satyanarayanadash/project1")

def repo_clone():
    subprocess.run(str(clone_cmd), shell=True)
    return

def export_gitlog():
    cwd = os.getcwd()
    repo_name = clone_cmd.split("/")
    repo_path = cwd + "/" + repo_name[1]
    os.chdir(repo_path)
    subprocess.run("git log > gitlog.txt", shell=True)
    return

repo_clone()
export_gitlog()
