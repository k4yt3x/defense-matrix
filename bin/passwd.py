#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Password Checker

Dev: Ivens Portugal
Date Created: September 16, 2017
Last Modified: September 19, 2017

Dev: K4YT3X
Last Modified: November 4, 2018
"""
import getpass
import os
import re
import shutil
import subprocess
import sys

VERSION = '1.0.1'


def replace_original_passwd():
    """
    Move the original passwd bindary file to oldpassword
    Create a symbolic link from /usr/bin/passwd to /usr/share/DefenseMatrix/passwd
    """
    try:
        # Backup original passwd binary
        os.rename('/usr/bin/passwd', '/usr/bin/oldpasswd')
    except FileNotFoundError:
        # We got a problem
        pass
    shutil.copy(os.path.realpath(__file__), '/usr/bin/passwd')
    shutil.chown('/usr/bin/passwd', user=0, group=0)
    os.chmod('/usr/bin/passwd', 755)


def restore_original_passwd():
    """
    Moves the original passwd bindary back

    Returns:
        bool -- returns false if original file not found,
        otherwise return None
    """
    try:
        os.remove('/usr/bin/passwd')
        os.rename('/usr/bin/oldpasswd', '/usr/bin/passwd')
    except FileNotFoundError:
        return False


def change_password(username, password):
    output = subprocess.Popen(('mkpasswd', '-m', 'sha-512', password), stdout=subprocess.PIPE)
    shadow_password = output.communicate()[0].strip()
    subprocess.call(('usermod', '-p', shadow_password, username))


class PasswdCheck(object):

    min_num_chars = 8
    max_num_chars = 100

    SMALL_PW = 'Your password should contain at least ' + str(min_num_chars) + ' characters.'
    LARGE_PW = 'Your password should contain at most ' + str(max_num_chars) + ' characters.'
    AT_LEAST_LOWC = 'Your password should have at least one lowercase character.'
    AT_LEAST_UPPC = 'Your password should containt at least one uppercase character.'
    AT_LEAST_NUMB = 'Your password should contain at least one number.'
    AT_LEAST_SPEC = 'Your password should contain at least one special character.'

    def check_password_complexity(self, passwd):
        cout_small_pw = re.search(r'^[A-Za-z\d$@$!%*#?&]{' + str(self.min_num_chars) + ',}$', passwd)
        cout_large_pw = re.search(r'^[A-Za-z\d$@$!%*#?&]{,' + str(self.max_num_chars) + '}$', passwd)
        cout_at_least_lowc = re.search(r'^(?=.*[a-z]).+$', passwd)
        cout_at_least_uppc = re.search(r'^(?=.*[A-Z]).+$', passwd)
        cout_at_least_numb = re.search(r'^(?=.*\d).+$', passwd)
        cout_at_least_spec = re.search(r'^(?=.*[$@$!%*#?&]).+$', passwd)

        if not cout_small_pw:
            return self.SMALL_PW
        elif not cout_large_pw:
            return self.LARGE_PW
        elif not cout_at_least_lowc:
            return self.AT_LEAST_LOWC
        elif not cout_at_least_uppc:
            return self.AT_LEAST_UPPC
        elif not cout_at_least_numb:
            return self.AT_LEAST_NUMB
        elif not cout_at_least_spec:
            return self.AT_LEAST_SPEC
        else:
            return True


if __name__ == '__main__':
    try:
        for _ in range(3):
            passwd = getpass.getpass('Enter new UNIX password:')
            repasswd = getpass.getpass('Retype new UNIX password:')
            if passwd != repasswd:
                print('Sorry, passwords do not match', file=sys.stderr)
            else:
                p = PasswdCheck()
                checkres = p.check_password_complexity(passwd)
                if checkres is not True:
                    print(checkres)
                else:
                    change_password(getpass.getuser(), passwd)
                    print('passwd: password updated successfully')
                    exit(0)
        print('passwd: Authentication token manipulation error\npasswd: password unchanged', file=sys.stderr)
        exit(1)
    except KeyboardInterrupt:
        exit(0)
