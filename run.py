#!/usr/bin/env python3.5

import os, sys
import time
import argparse
from subprocess import Popen, PIPE, STDOUT

## what is the configuration loop ?
sys.path.append(os.path.abspath("configuration.py"))
from configuration import *


# Define a function to launch the bkp_mydumper shell script with params
def executor(cmd):
    """ Executes a system command and returns STDERR and STDOUT """
    try:
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        return stdout, stderr
    except OSError as err:
        print("OS error: {0}".format(err))
        err, err
    except Exception as ex:
        print(ex)
        return ex,'C.ERROR'

if servers:
    for server in servers:
        info = servers[server]
        howoften = info[3]
        command = "%s %s %s %s" % (MYSQL_BINARY, info[0], info[1], info[2])
        time.sleep(howoften)
        out, err = executor(command)
        print('Backuped up %s' % server, out.decode())
        if len(err) > 0:
            print(err)
else:
    print('Dude, are you sure "servers" entry exists in your configuration.py')
