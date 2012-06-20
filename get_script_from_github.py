import urllib2
response = urllib2.urlopen("https://raw.github.com/BenOut/PythonLogFileReader/master/dilemmas_new_users.py")
python_script_from_git = response.read()
exec python_script_from_git
raw_input("Press enter to close")
