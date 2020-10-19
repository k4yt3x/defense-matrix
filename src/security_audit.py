#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Defense Matrix Security Audit Module
Dev: K4YT3X
Date Created: October 19, 2018
Last Modified: October 19, 2018
"""
from avalon_framework import Avalon
from utilities import Utilities
import sys

VERSION = '1.0.0'


class SecurityAudit:
    """ Defense Matrix Security Audit Module

    This module runs all the security auditing tools installed,
    and it might also help parsing the results in the future.
    """

    def __init__(self):
        pass

    def run(self):
        self._run_tiger()
        self._run_rkhunter()

    def _run_tiger(self):
        Avalon.info('Launching tiger')
        Utilities.execute(['tiger'], std_in=sys.stdin, std_out=sys.stdout, std_err=sys.stderr)

    def _run_rkhunter(self):
        Avalon.info('Launching rkhunter')
        Utilities.execute(['rkhunter'], std_in=sys.stdin, std_out=sys.stdout, std_err=sys.stderr)
