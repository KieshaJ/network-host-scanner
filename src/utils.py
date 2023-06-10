import os
from . import constants

def input_ip():
    """
    Takes input from the command line as an IP address
        Returns:
        ip (str): The network ID of the IP address octet (the first 3 bytes)
    """
    ip = input(constants.TAG + constants.INPUT_MSG)
    octet = ip.rfind('.')
    return ip[0:octet + 1]


def ping(host: str):
    """
    Returns the result of a ping request
        Parameters:
            host (str): The IP address to ping
        Returns:
            result (int): The result of the ping request
    """
    return os.system(constants.PING_CMD + host + ">/null")


def remove_file():
    """
    Removes the result file if it exists
    """
    if os.path.exists(constants.RESULT_FILE):
        os.remove(constants.RESULT_FILE)


def append_file(host: str):
    """
    Appends a new host to the result file
        Parameters:
            host (str): The host to append
    """
    res_file = open(constants.RESULT_FILE, "a")
    res_file.write(host + "\n")
    res_file.close()


def scan(ip: str):
    """
    Iterates through all of the IPs with the given network ID
    and appends any that are up to the result file
        Parameters:
            ip (str): The network ID
    """
    print(constants.TAG + constants.START_MSG)
    for x in range(1, 255):
        host = ip + str(x)
        res = ping(host)

        if res == 0:
            print(constants.TAG + host + constants.RES_UP)
            append_file(host)
        else:
            print(constants.TAG + host + constants.RES_DOWN)

