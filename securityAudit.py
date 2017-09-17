#!/usr/bin/python3
from prettytable import PrettyTable
import subprocess
import sys


def generateReport(reportFile):
    table = PrettyTable(["Category", "Name", "Description"])
    rf = ""
    with open(reportFile, "r") as reportf:
        for line in reportf:

            rf += line
    rfinal = rf.replace("\n         ", "")
    for line in rfinal.split("\n"):
        if "FAIL" in line or "ALERT" in line:
            table.add_row([line.split(" ")[0].replace("-", ""), line.split(" ")[1], ' '.join(line.split(" ")[2:])])
    print(table)


class tiger:

    def check():
        output = ''
        process = subprocess.Popen(['tiger'], stdout=subprocess.PIPE)
        for c in iter(lambda: process.stdout.read(1), ''):
            if not c:
                break
            sys.stdout.write(c.decode())
            output += c.decode()
        for line in output.split('\n'):
            if "Security report is in" in line:
                return line.split("`")[1].split("'")[0]


def audit():
    generateReport(tiger.check())
