#!/usr/bin/env python3
def main():
    stringlist = "here is my test"
    newlist = stringlist.split(" ")
    print(newlist)
    
    myip = ["192","168","0","1"]
    singleip = ".".join(myip)
    print(singleip)

main()
