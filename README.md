# UserManager : Linux 大量使用者管理工具

為程式設計課課程所開發的伺服器帳號管理工具，可大量建立學生使用者的帳號，

並可對單一使用者帳號，進行刪除及密碼重設或過期重設等功能。

## Setup

```
chmod +x ./manage_account.py
```
在 account.csv 中設定所需大量建立使用者的帳號、密碼，第一欄為帳號，第二欄為密碼。

## Usage
大量建立 account.csv 中設定的使用者
```
$ ./manage_account.py create
```
重設指定使用者密碼
```
$ ./manage_account.py reset <uesrname> <password>
```
指定使用者密碼過期
```
$ ./manage_account.py expire <uesrname>
```
大量使 account.csv 中設定的使用者密碼過期
```
$ ./manage_account.py expireAll
```
刪除指定使用者
```
$ ./manage_account.py delete <uesrname>
```
大量刪除 account.csv 中設定的使用者
```
$ ./manage_account.py deleteAll
```
