import subprocess



def get_list_of_modified_files():
	try:
		command = subprocess.run("git branch --show-current", check=True, capture_output=True, encoding="utf-8")
		command_output = command.stdout.splitlines()
		current_branch_name = command_output[0]
		print("CURRENT BRANCH NAME >>> ", current_branch_name)

		list_all_commits_command = subprocess.run(["git", "reflog", "show", "--no-abbrev", "--pretty=format:%h", current_branch_name], check=True, capture_output=True, encoding="utf-8")
		list_all_commits_output = list_all_commits_command.stdout.splitlines()
		inital_state = list_all_commits_output[0]
		latest_state = list_all_commits_output[-1]
		print("INITIAL COMMIT ID >>>", inital_state)
		print("LATEST COMMIT ID >>>", latest_state)

		list_modified_files_command = subprocess.run(["git", "diff", "--name-only", inital_state, latest_state], check=True, capture_output=True, encoding="utf-8")
		list_modified_files_command_output = list_modified_files_command.stdout.splitlines()
		print("LIST OF MODIFIED FILES >>>", list_modified_files_command_output)






	except subprocess.CalledProcessError as err:
		print("Git command returned following error", err)

	except IndexError as index_err:
		print("Git command output returned Empty list")



get_list_of_modified_files()