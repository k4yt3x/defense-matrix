#!/usr/bin/python3
import re
import subprocess
import getpass


# class PasswdCheck(object):
#  def checkPasswdComplexity(self, passwd):
#    cmd = "echo " + passwd  + " | cracklib-check"
#    cout = subprocess.check_output(cmd, shell=True).decode()
#    coutparsed = cout[cout.index(":")+2:-1]
#    return coutparsed


def replaceOriginalPasswd():
    import os
    if os.rename("/usr/bin/passwd", "/usr/bin/oldpasswd") != 0:
        return False
    os.system("ln -s /usr/bin/passwd /usr/share/DefenseMatrix/passwd")


def changePassword(username, password):
    output = subprocess.Popen(('mkpasswd', '-m', 'sha-512', password), stdout=subprocess.PIPE)
    shadow_password = output.communicate()[0].strip()
    subprocess.call(('usermod', '-p', shadow_password, username))


class passwdCheck(object):

    min_num_chars = 8
    max_num_chars = 20

    SMALL_PW = "Your password should contain at least " + str(min_num_chars) + " characters."
    LARGE_PW = "Your password should contain at most " + str(max_num_chars) + " characters."
    AT_LEAST_LOWC = "Your password should have at least one lowercase character."
    AT_LEAST_UPPC = "Your password should containt at least one uppercase character."
    AT_LEAST_NUMB = "Your password should contain at least one number."
    AT_LEAST_SPEC = "Your password should contain at least one special character."

    def checkPasswdComplexity(self, passwd):
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
    for _ in range(3):
        passwd = getpass.getpass("Enter new UNIX password:")
        repasswd = getpass.getpass("Retype new UNIX password:")
        if passwd != repasswd:
            print("Sorry, passwords do not match")
        else:
            p = passwdCheck()
            checkres = p.checkPasswdComplexity(passwd)
            if checkres is not True:
                print(checkres)
            else:
                changePassword(getpass.getuser(), passwd)
                print("passwd: password updated successfully")
                exit(0)
    print("passwd: Authentication token manipulation error\npasswd: password unchanged")
