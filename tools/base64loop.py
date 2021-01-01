#!/usr/bin/python3
import sys, os

f = open("pwdbackup.txt","r")


for i in range(0,13):
    newfile = 'pwdbackup.txt' + str(i)
    
    if i == 0:
        filename = 'pwdbackup.txt'
        cmd = 'cat ' + filename + ' | base64 -d > pwdbackup.txt' + str(i)
        os.system(cmd)

    else:
        newfile = 'pwdbackup.txt' + str(i)
        integer = i - 1
        oldfile = 'pwdbackup.txt' + str(integer)
        file2 = open(oldfile, "r")
        cmd = 'cat ' + oldfile + ' | base64 -d > pwdbackup.txt' + str(i)
        os.system(cmd)
