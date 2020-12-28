import json
import threading
from threading import *
import time
import os

# Functions
d = {}


def read(k):
    if k not in d:
        print("Error: This key is not Present")
    else:
        b = d[k]
        if b[1] != 0:
            if time.time() < b[1]:
                stri = str(k) + ":" + str(b[0])
                return stri
            else:
                print("Error: time-to-live of", k, "has expired")
        else:
            stri = str(k) + ":" + str(b[0])
            print(stri)


def create(key, value, timeout=0):
    if key in d:
        print("error: this key already exists")  # error message1
    else:
        if (key.isalpha()):
            if len(d) < (1024 * 1020 * 1024) and value <= (
                    16 * 1024 * 1024):  # constraints for file size less than 1GB and Jasonobject value less than 16KB
                k = value
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:  # constraints for input key_name capped at 32chars
                    d[key] = l
            else:
                print("error: Memory limit exceeded!! ")  # error message2
        else:
            print(
                "error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")  # error message3


def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")  # error message4
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of", key, "has expired")  # error message5
        else:
            del d[key]
            print("key is successfully deleted")


# It will print all the data at once
def completeData():
    print(d)


# if you want to store the content at any specific location
def save_data(loc = ""):
    path = loc
    file = 'data.txt'
    with open(os.path.join(path, file), 'a') as fp:
        json.dump(d, fp)
