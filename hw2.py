#!/usr/bin/python

import pexpect

newprimates = open("primates2.nex", "w")
oldprimates = open("primates.nex").read()

print(oldprimates)

corrected = oldprimates.replace("mcmc", "mcmcp")

print(corrected)

newprimates.write(corrected)

newprimates.close()

print(":testttttt")

child = pexpect.spawn("mb -i primates2.nex")

child.sendline(r"mcmc")

child.sendline("no")

child.expect("MrBayes >")

print child.before

child.sendline("sumt")

child.expect("MrBayes >")

child.sendline("sump")

child.expect("MrBayes >")

child.sendline("quit")

