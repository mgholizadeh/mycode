#!/usr/bin/env python3
import shutil
import os
def main():
    os.chdir("/home/student/mycode")
    shutil.move("gholizadeh.obj", "ceph_storage/")
    xname = input("what is your new name for mohammad.obj?")
    shutil.move("ceph_storage/mohammad.obj","ceph_storage/" + xname)
main()
