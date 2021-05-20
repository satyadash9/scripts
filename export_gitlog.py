import subprocess
import os

clone_cmd = "git clone git@github.com:satyanarayanadash/project1"
export_gitlog = "git log > gitlog.txt | ls -la"

def subp_run(cmd):
    subprocess.run(cmd, shell=True)

def change_dir():
    repo_name = clone_cmd.split("/")[1]
    repo_path = os.getcwd() + "/" + repo_name
    os.chdir(repo_path)
    print("Current working directory ->", os.getcwd())

subp_run(clone_cmd)
change_dir()
subp_run(export_gitlog)
