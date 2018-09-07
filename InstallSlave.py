##
# This script will install software dependencies onto a base image needed by GMA.
# It must be run under an account with administrator permissions.
# Modified: 9/7/2018
# Author: Ricardo Alcazar
##
import CommandManager

# get the sudo password, cast to string
pw = raw_input("Sudo password? ")
print(pw)

# get shell manager
mgr = CommandManager.CommandManager()

# create jenkins user, add to the staff group
mgr.executeWithSudo("sudo systemadminctl -addUser jenkins -password gmadevop -home /Users/jenkins -uid 1000")
mgr.executeWithSudo("sudo dseditgroup -o edit -a jenkins -t user staff")

#
mgr.executeWithSudo("sudo systemsetup -getremotelogin", pw)
mgr.execute("hostname")

print("Complete")
exit(0)