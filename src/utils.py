import os
from . import constants

def input_ip():
    ip = input(constants.TAG + constants.INPUT_MSG)
    octet = ip.rfind('.')
    return ip[0:octet + 1]


def ping(host: str):
    return os.system(constants.PING_CMD + host + ">/null")


def remove_file():
    if os.path.exists(constants.RESULT_FILE):
        os.remove(constants.RESULT_FILE)


def append_file(host: str):
    res_file = open(constants.RESULT_FILE, "a")
    res_file.write(host + "\n")
    res_file.close()


def scan(ip: str):
    print(constants.TAG + constants.START_MSG)
    for x in range(1, 255):
        host = ip + str(x)
        res = ping(host)

        if res == 0:
            print(constants.TAG + host + constants.RES_UP)
            append_file(host)
        else:
            print(constants.TAG + host + constants.RES_DOWN)

