# Budu Hijack

This package demonstrates how a python code can be used to change user password on Windows OS without knowing the password of the admin user. In a more elaborate term, it helps you hack any Windows system. The only thing you need is the username of the user you want to hack.

## Installation

Clone the github repository

## Usage


### Run directly from terminal

Grab the username of the system and choose your desired new password, then run the code below to generate the code.py file

``` cmd

C:\Users\user\Desktop> python execute.py username password

```

### Run code.py directly

```
python code.py

```

### Convert code.py to Windows executable format (exe)

install pyinstaller

```
pip install pyinstaller

```

Then run convert using the command below

```
C:\Users\user\Desktop> pyinstaller -y -F  "C:/Users/user/Desktop/code.py"

```
## Disclaimer

#### Programmers

This project is a demonstration of how python can change Windows computer password. We do not encourage this package to be used in a live program without disclosure and usage must be at users discretion. Attempt to use this package for malicious purpose is not allowed.


## Developer(s)


[Oyeniyi Abiola Peace](https://twitter.com/_iamoracle)