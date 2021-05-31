from datetime import datetime
import json

def gitlog_json():
    with open("gitlog.txt", 'r') as rf:
        previous_line = ""
        commit_key = 0
        commit_dict = {}
        for line in rf:
            # line as "commit 30f405719ab6738e38132eaf708aa82372322cf1"
            if line.startswith("commit", 0):
                value = (line.strip()).split(" ")[1]
                commit_key = commit_key + 1
                commit_dict[commit_key] = {}
                commit_dict[commit_key]["Commit_id"] = value
            # line as "Author: Satyanarayana Dash <satya.d135@gmail.com>"
            elif line.startswith("Author", 0):
                value = (line.strip()).split(": ")[1]
                commit_dict[commit_key]["Author"] = value
            # line as "Date:   Sun May 23 09:08:29 2021 +0530"
            elif line.startswith("Date", 0):
                date_str = (line.rstrip()).split("   ")
                date_obj = datetime.strptime(date_str[-1], "%a %b %d %H:%M:%S %Y %z")
                value = str(date_obj.strftime("%d-%m-%Y"))
                commit_dict[commit_key]["Date"] = value
            # line as "    1st line of commit messages ."
            elif previous_line.isspace() and line.startswith("   "):
                value = line.strip()
                commit_dict[commit_key]["Subject"] = value
            # lines as "    For the commit msgs written in multiple lines"
            elif not previous_line.isspace() and line.startswith("   "):
                value = line.strip()
                commit_dict[commit_key]["Subject"] = commit_dict[commit_key]["Subject"] + ", " + value
            else:
                pass
            previous_line = line

    # Dictionary to json
    json_str = json.dumps(commit_dict, indent=5)
    with open("gitlog.json", 'w') as wf:
        wf.write(json_str)

    # printing dictionary/all commits
    for commit_key, commit_values in commit_dict.items():
        print("\nCommit Key:", commit_key)
        for key in commit_values:
            print(key + ':', commit_values[key])

    # # printing commits on a particular date
    # commit_date = str(input("Commits on Date: "))
    # for commit_key, commit_values in commit_dict.items():
    #     if commit_dict[commit_key]["Date"] == commit_date:
    #         print("\nCommit No:", commit_key)
    #         for key in commit_values:
    #             print(key + ':', commit_values[key])

gitlog_json()
