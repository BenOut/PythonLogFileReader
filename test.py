import os
file_path = "C:\BEN\\text scrape test\\000 - logs\\"
files = os.listdir(file_path)
files = filter(lambda x: x.find("log0") >-1, files)
name_n_timestamp = dict([(x, os.stat(file_path+x).st_mtime) for x in files])
print max(name_n_timestamp, key=lambda k: name_n_timestamp.get(k))

raw_input("Press enter to continue")

"""
def printGreeting():
	print "HELLO MUM - TOP OF THE WORLD"

printGreeting()

raw_input("Press enter to continue")
"""
