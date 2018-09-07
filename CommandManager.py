##
# Modified: 9.7.2018
# Author: Ricardo Alcazar
##

import pexpect


# Simple command manager
class CommandManager:

    # execute the specified command, assume sudo is required and provide password
    def executeWithSudo(self, cmd, pw):
        print("CommandManager.execute(): Invoking spawn()")
        shell = pexpect.spawn(cmd)
        shell.expect("Password")
        shell.sendline(pw)
        print(shell.read())

    # execute the specified command
    def execute(self,cmd):
        print("CommandManager.execute(): Invoking spawn()")
        shell = pexpect.spawn(cmd)
        print(shell.read())