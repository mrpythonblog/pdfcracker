#!/usr/bin/python3
from pikepdf import open as openfile
import sys
from os import path,system
from time import sleep

def dict_attack():
    print("*"*40)
    pdf_file = input("PDF File : ")
    if path.isfile(pdf_file) == False:
        print("{} Does not Exist !".format(pdf_file))
        sys.exit(1)

    password_file = input("Dictionery : ")
    if path.isfile(password_file) == False:
        print("{} Does not Exist !".format(pdf_file))
        sys.exit(1)
    password_file = open(password_file)
    system("clear")
    print("Starting Attack ...")
    sleep(3)
    find = False
    for password in password_file:
        password = password.strip("\n")
        print("Testing : {}".format(password))
        try:
            openfile(pdf_file,password)
            print("-"*50)
            print("Password : {}".format(password))
            find = True
            break
        except:
            continue
    if find:
        system("beep")
        sys.exit()
    system("beep")
    print("*"*50)
    input("Sorry ! Crack Faild !")
    

def num_attack():
    print("*"*50)
    pdf_file = input("PDF File : ")
    if path.isfile(pdf_file) == False:
        print("{} Does not Exist !".format(pdf_file))
        sys.exit(1)

    start = input("Start Number (Default = 0) :")
    if start == "" :
        start = 0
    try:
        start = int(start)
    except:
        print("Invalid Value !")
        sys.exit(1)
    
    system("clear")
    print("Starting Attack ...")
    sleep(3)
    find = False
    while not find:
        print("Testing : {}".format(start))
        try:
            openfile(pdf_file,str(start))
            print("*"*50)
            print("Password : {}".format(start))
            find = True
        except:
            start += 1
            continue
    system("beep")
    sys.exit(0)
   
while True:
    system("clear")
    method = input("""
            [1] Dictionery Attack
            [2] Nummerical Attack
            [3] Exit
            >>> """)
    if method == "3":
        sys.exit()
    elif method == "1":
        dict_attack()
    elif method == "2":
        num_attack()
    else:
        continue

