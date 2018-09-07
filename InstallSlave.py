

import CommandManager

# get the sudo password, cast to string
pw = raw_input("Sudo password? ")
print(pw)

# get shell manager
mgr = CommandManager.CommandManager()

#
mgr.executeWithSudo("sudo systemsetup -getremotelogin", pw)
mgr.execute("hostname")

print("Complete")
exit(0)