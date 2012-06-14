import os
folder_path = "C:\BEN\\text scrape test\\Traders\\"
files = os.listdir(folder_path)
files = filter(lambda x: x.find("Traders.txt") >-1, files)
name_n_timestamp = dict([(x, os.stat(folder_path+x).st_mtime) for x in files])
newest_log_file_name = max(name_n_timestamp, key=lambda k: name_n_timestamp.get(k))
print "The latest log file is " + newest_log_file_name
file_path = folder_path+newest_log_file_name
print "File path = " + file_path
file_open = open(file_path, 'r')
file_contents = file_open.read()
string_occurrence_count = file_contents.count('New User Session')
print "There were " + str(string_occurrence_count) + " new user sessions listed in the log file"

raw_input("Press enter to continue")

"""
def printGreeting():
	print "HELLO MUM - TOP OF THE WORLD"

printGreeting()

raw_input("Press enter to continue")
"""
