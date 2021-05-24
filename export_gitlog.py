import subprocess
import os
import shutil
from datetime import datetime

clone_cmd = "git clone git@github.com:satyanarayanadash/project1"
export_gitlog = "git log > gitlog.txt | ls"

repo_name = clone_cmd.split("/")[1]
repo_path = os.getcwd() + "/" + repo_name

def chk_del_clone(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("Deleted existing repo directory")
        subp_run(clone_cmd)
    else:
        print("Repo directory does not exist")
        subp_run(clone_cmd)

def subp_run(cmd):
        subprocess.run(cmd, shell=True)

def chdir_export_gitlog(path):
    try:
        os.chdir(path)
        print("Changed current working directory ->", os.getcwd(), "\n")
        subp_run(export_gitlog)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

def format_logfile():
    try:
        previous_line = ""
        with open("gitlog.txt", 'r') as f:
            all_lines = f.readlines()
        with open("gitlog.txt", 'w') as f:
            for line in all_lines:
                if line.startswith("commit", 0):
                    f.write("\n" + line)
                elif line.startswith("Date", 0):
                    # Date:   Sun May 23 09:08:29 2021 +0530
                    dt_str = (line.rstrip()).split("   ")
                    dt_obj = datetime.strptime(dt_str[-1], "%a %b %d %H:%M:%S %Y %z")
                    f.write(dt_str[0] + str(dt_obj) + "\n")
                elif previous_line.startswith("Date"):
                    f.write("Commit message: " + line.lstrip())
                elif not line.isspace():
                    f.write(line.lstrip())
                else:
                    pass
                previous_line = line
    except Exception as e:
        print(e)

chk_del_clone(repo_path)
chdir_export_gitlog(repo_path)
format_logfile()
