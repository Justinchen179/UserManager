#!/usr/bin/env python3
import csv
import os
import sys


def ReadCSV():
    rows = []
    with open('account.csv', newline='') as csvfile:
        csv_rows = csv.reader(csvfile)
        for row in csv_rows:
            rows.append(row)
    return rows


def CreateAccount(rows):
    for row in rows:
        username = row[0]
        password = row[1]
        add_account_cmd = "sudo useradd %s" % username
        set_password_cmd = "echo \"%s\\n%s\"  | sudo passwd %s" % (password, password, username)

        os.system(add_account_cmd)
        os.system(set_password_cmd)


def DeleteAccount(username):
    del_account_cmd = "sudo userdel %s" % username

    os.system(del_account_cmd)


def DeleteAllAccount(rows):
    for row in rows:
        username = row[0]
        del_account_cmd = "sudo userdel %s" % username

        os.system(del_account_cmd)


def ExpireAccount(username):
    expire_account_cmd = "sudo passwd -e %s" % username

    os.system(expire_account_cmd)


def ExpireAllAccount(rows):
    for row in rows:
        username = row[0]
        expire_account_cmd = "sudo passwd -e %s" % username

        os.system(expire_account_cmd)


def SetAccountPassword(username, password):
    set_password_cmd = "echo  \"%s\\n%s\" |sudo passwd %s" % (password, password, username)

    os.system(set_password_cmd)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("\nmanage_account.py <create | delete | deleteAll | expire | expireAll | reset >\n")
        sys.exit()

    cmds = ["create", "delete", "deleteAll", "expire", "expireAll", "reset"]

    opt = sys.argv[1]

    if opt not in cmds:
        print("No support this argument")
        sys.exit()

    rows = ReadCSV()

    if opt == 'create':
        CreateAccount(rows)
    elif opt == 'delete':
        if len(sys.argv) < 3:
            print("\nmanage_account.py delete <uesrname> \n")
            sys.exit()
        uesrname = sys.argv[2]
        DeleteAccount(uesrname)
    elif opt == 'deleteAll':
        DeleteAllAccount(rows)
    elif opt == 'expire':
        if len(sys.argv) < 3:
            print("\nmanage_account.py expire <uesrname> \n")
            sys.exit()
        uesrname = sys.argv[2]
        ExpireAccount(uesrname)
    elif opt == 'expireAll':
        ExpireAllAccount(rows)
    elif opt == 'reset':
        if len(sys.argv) < 4:
            print("\nmanage_account.py reset <uesrname> <password>\n")
            sys.exit()
        uesrname = sys.argv[2]
        password = sys.argv[3]
        SetAccountPassword(uesrname, password)
