#!/usr/bin/python

import pexpect

def function1(nexus_file, numgen):
    child = pexpect.spawn("mb -i " + nexus_file)
    child.sendline("set nowarn = yes")
    child.sendline("mcmcp ngen = " + numgen)
    child.sendline("mcmc")
    child.sendline("no")
    child.sendline("quit")

def function2(nexus_file):
    child = pexpect.spawn("mb -i " + nexus_file)
    child.sendline("sumt")
    child = pexpect.spawn("mb -i " + nexus_file)
    child.sendline("sump")
    child.expect("MrBayes >")
    child.sendling("quit")

number_of_files = pexpect.run("ls | wc -l")
print(number_of_files)

nexus_file = "primate2.nex"
function1(nexus_file, 2000)
function2(nexus_file)

