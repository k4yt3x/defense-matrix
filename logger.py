#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defense Matrix Logger

Writes logs into log file
"""
import datetime
import os
LOGPATH = "/var/log/DefenseMatrix.log"


class logger:

    def writeLog(self, content):
        with open(LOGPATH, "a+") as log:
            log.write(str(datetime.datetime.now()) + " " + str(content) + "\n")
            log.close()

    def purge(self):
        os.remove(LOGPATH)
