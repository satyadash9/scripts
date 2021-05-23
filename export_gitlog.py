import subprocess
import os
import shutil

clone_cmd = "git clone git@github.com:satyanarayanadash/project1"
export_gitlog = "git log > gitlog.txt | ls"

repo_name = clone_cmd.split("/")[1]
repo_path = os.getcwd() + "/" + repo_name

def chk_del_dir(path):
    if os.path.exists(path) is True:
        shutil.rmtree(path)
        print("\n", "Deleted existing repo directory", "\n")
        subp_run(clone_cmd)
    else:
        print("\n", "Repo directory does not exist", "\n")
        subp_run(clone_cmd)

def subp_run(cmd):
        subprocess.run(cmd, shell=True)

def change_dir(path):
    try:
        os.chdir(path)
        print("Changed current working directory", "\n")
        subp_run(export_gitlog)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

chk_del_dir(repo_path)
change_dir(repo_path)
