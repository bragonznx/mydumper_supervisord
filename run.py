#!/usr/bin/env python3.4

import os, sys
import time

## what is the configuration loop ?
sys.path.append(os.path.abspath("conf.py"))
from conf import *

if howoften == 'infinite':
    os.system('bash bkp_mydumper')
    exit 0

if howoften == 'hourly':
    time.sleep(3600)
    os.system('bash bkp_mydumper')
    exit 0
    
if howoften == 'daily':
    time.sleep(86400)
    os.system('bash bkp_mydumper')
    exit 0
    
if howoften == 'weekly':
    time.sleep(6004800)
    os.system('bash bkp_mydumper')
    exit 0
    
