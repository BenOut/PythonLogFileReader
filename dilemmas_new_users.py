# Python Log File Reader
# For Traders "Dilemmas Interactive"
# 
# By BenOut
# https://github.com/BenOut/PythonLogFileReader


# Imports
import os
import operator

# Define constant vars
python_log_file_name = "python_log.txt"
interactive_log_file_directory = "C:\BEN\\text scrape test\\Traders\\"
python_log_file = None
python_log_file_exists = False
python_log_file_contents = ""
total_new_user_sessions  = 0

# Common functions
def report_error(function_in_error, error_message):
	print "Error in function: " + function_in_error
	print error_message
	raw_input("Press enter to continue")
	#END - report_error


def check_text_file_existence(file_name):
	function_name = "check_text_file_existence"
	file_existence_status = os.path.exists(file_name)
	return file_existence_status
	#END - check_text_file_existence


def create_text_file(file_name):
	function_name = "create_text_file"
	created_file = open(file_name, 'w')
	return created_file
	#END - create_text_file


def open_text_file(file_name):
	function_name = "open_text_file"
	opened_file = open(file_name, 'r')
	return opened_file
	#END - open_text_file


def read_text_file(file_name):
	function_name = "read_text_file"
	read_file = file_name.read()
	return read_file
	#END - read_text_file


def write_to_text_file(recipient_file, text_to_write):
	recipient_file.write(text_to_write)
	#END - write_to_text_file


def string_index_in_text_file(file_name, search_string):
	string_index = file_name.rfind(search_string)
	return string_start_index
	#END - string_index_in_text_file






# Specific functions

def main():
	function_name = "main"
	find_previous_timestamp_in_logs()
	#END - main


def find_previous_timestamp_in_logs():
	function_name = "find_previous_timestamp_in_logs"
	
	global total_new_user_sessions
	
	previously_used_timestamp = get_previous_timestamp_from_python_log()	
	interactive_log_file_count = total_interactive_log_files()
	#DEBUG
	print "There are " + str(interactive_log_file_count) + " log files"
	
	if previously_used_timestamp == "":
		i = 0
		while i < interactive_log_file_count:
			next_interactive_log_file_path = find_next_newest_interactives_log_file(i+1)
			interactive_log_file = open(next_interactive_log_file_path, 'r')
			interactive_log_file_text = interactive_log_file.read()
			new_user_sessions_this_file = interactive_log_file_text.count('New User Session')
			total_new_user_sessions = total_new_user_sessions + new_user_sessions_this_file
			i = i + 1
			print "Pass #" + str(i) + " >> Cumulative frequency: " + str(total_new_user_sessions) + " ---- Frequency: " + str(new_user_sessions_this_file)
		print "Final - " + str(total_new_user_sessions)
	else:
		i = 0
		while i < interactive_log_file_count:
			next_interactive_log_file_path = find_next_newest_interactives_log_file(i+1)
			interactive_log_file = open(next_interactive_log_file_path, 'r')
			interactive_log_file_text = interactive_log_file.read()
			previous_reported_position = interactive_log_file_text.find(python_log_file_contents)
			if previous_reported_position == -1:
				new_user_sessions_this_file = interactive_log_file_text.count('New User Session')
				total_new_user_sessions = total_new_user_sessions + new_user_sessions_this_file
				i = i + 1
				print "Pass #" + str(i) + " >> Cumulative frequency: " + str(total_new_user_sessions) + " ---- Frequency: " + str(new_user_sessions_this_file)
			else:
				print "The previous reporting position is in this doc"
				i = interactive_log_file_count
		print "Final - " + str(total_new_user_sessions)
	
	python_log_file_for_updating = open(python_log_file_name, 'w')
	
	newest_interactive_log_name = find_next_newest_interactives_log_file(1)
	newest_interactive_log_file = open(newest_interactive_log_name, 'r')
	newest_interactive_log_file_text = newest_interactive_log_file.read()
	last_timestamp_position = newest_interactive_log_file_text.rfind(" GMT+0100 2012")
	print "last_timestamp_position = " + str(last_timestamp_position)
	latest_timestamp_in_interactive_logs = newest_interactive_log_file_text[(last_timestamp_position-19):(last_timestamp_position+14)]
	print "latest_timestamp_in_interactive_logs = " + latest_timestamp_in_interactive_logs + "!!!"
	write_to_text_file(python_log_file_for_updating, latest_timestamp_in_interactive_logs)
	#END - find_previous_timestamp_in_logs

def get_previous_timestamp_from_python_log():
	function_name = "get_previous_timestamp_from_python_log"
	
	global python_log_file_contents
	
	python_log_file_exists = check_text_file_existence(python_log_file_name)
	
	if python_log_file_exists == True:
		python_log_file_contents = get_python_log_file_contents()
	elif python_log_file_exists == False:
		create_python_log_file()
		python_log_file_contents = ""
	else:
		report_error(function_name, "Unexpected value (" + str(python_log_file_exists) + ") in python_log_file_exists")
		python_log_file_contents = ""
	
	return python_log_file_contents
	#END - get_previous_timestamp_from_python_log


def get_python_log_file_contents():
	function_name = "get_python_log_file_contents"
	#global python_log_file
	
	python_log_file = open_text_file(python_log_file_name)	
	python_log_file_contents = read_text_file(python_log_file)
	
	return python_log_file_contents
	#END - open_python_log_file


def create_python_log_file():
	function_name = "create_python_log_file"
	python_log_file = create_text_file(python_log_file_name)
	#END - create_python_log_file


def total_interactive_log_files():
	function_name = "total_interactive_log_files"
	global interactive_log_file_path
	interactive_log_files = os.listdir(interactive_log_file_directory)
	interactive_log_files = filter(lambda x: x.find("Traders.txt") >-1, interactive_log_files)
	interactive_log_files_timestamps = list([(x, os.stat(interactive_log_file_directory+x).st_mtime) for x in interactive_log_files])
	return len(interactive_log_files_timestamps)
	#END total_interactive_log_files


def find_first_interactive_log_file():
	function_name = "find_first_interactive_log_file"
	global interactive_log_file_path
	interactive_log_files = os.listdir(interactive_log_file_directory)
	interactive_log_files = filter(lambda x: x.find("Traders.txt") >-1, interactive_log_files)
	interactive_log_files_timestamps = dict([(x, os.stat(interactive_log_file_directory+x).st_mtime) for x in interactive_log_files])
	first_interactive_log_file = min(interactive_log_files_timestamps, key=lambda k: interactive_log_files_timestamps.get(k))
	interactive_log_file_path = interactive_log_file_directory + first_interactive_log_file
	#DEBUG
	print "found first file = " + str(interactive_log_file_path)
	#END - find_first_interactive_log_file


def find_latest_interactives_log_file():
	function_name = "find_latest_interactive_log_file"
	global interactive_log_file_path
	interactive_log_files = os.listdir(interactive_log_file_directory)
	interactive_log_files = filter(lambda x: x.find("Traders.txt") >-1, interactive_log_files)
	print interactive_log_files
	interactive_log_files_timestamps = dict([(x, os.stat(interactive_log_file_directory+x).st_mtime) for x in interactive_log_files])
	first_interactive_log_file = max(interactive_log_files_timestamps, key=lambda k: interactive_log_files_timestamps.get(k))
	interactive_log_file_path = interactive_log_file_directory + first_interactive_log_file
	#DEBUG
	print "found latest file = " + str(interactive_log_file_path)
	#END - find_latest_interactives_log_file


def find_next_newest_interactives_log_file(log_file_list_index):
	function_name = "find_latest_interactive_log_file"
	global interactive_log_file_path
	interactive_log_files = os.listdir(interactive_log_file_directory)
	interactive_log_files = filter(lambda x: x.find("Traders.txt") >-1, interactive_log_files)
	interactive_log_files_timestamps = list([(x, os.stat(interactive_log_file_directory+x).st_mtime) for x in interactive_log_files])
	#print "------------------------------------------------------------------"
	#print "------------------------------------------------------------------"
	#print interactive_log_files_timestamps
	#print "=================================================================="
	#print "=================================================================="
	sorted_interactive_log_files_timestamps = sorted(interactive_log_files_timestamps, key=lambda interactive_log_files_timestamps: interactive_log_files_timestamps[1])
	#print sorted_interactive_log_files_timestamps
	#print "The last item is:"
	next_newest_interactive_log_file = sorted_interactive_log_files_timestamps[len(sorted_interactive_log_files_timestamps)-log_file_list_index]
	#print next_newest_interactive_log_file
	next_newest_interactive_log_file = str(next_newest_interactive_log_file).split("'")
	next_newest_interactive_log_file = next_newest_interactive_log_file[1]
	#print next_newest_interactive_log_file
	#print "------------------------------------------------------------------"
	#print "------------------------------------------------------------------"
	interactive_log_file_path = interactive_log_file_directory + next_newest_interactive_log_file
	#DEBUG
	print "found latest file = " + interactive_log_file_path
	return interactive_log_file_path
	#END - find_latest_interactives_log_file





# 






main()

raw_input("Press enter to continue")
