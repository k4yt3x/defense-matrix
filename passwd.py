import subprocess
import re

#class PasswdCheck(object):
#  def checkPasswdComplexity(self, passwd):
#    cmd = "echo " + passwd  + " | cracklib-check"
#    cout = subprocess.check_output(cmd, shell=True).decode()
#    coutparsed = cout[cout.index(":")+2:-1]
#    return coutparsed

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
    cout_small_pw = re.search(r'^[A-Za-z\d$@$!%*#?&]{'+str(self.min_num_chars)+',}$', passwd)
    cout_large_pw = re.search(r'^[A-Za-z\d$@$!%*#?&]{,'+str(self.max_num_chars)+'}$', passwd)
    cout_at_least_lowc = re.search(r'^(?=.*[a-z]).+$', passwd)
    cout_at_least_uppc = re.search(r'^(?=.*[A-Z]).+$', passwd)
    cout_at_least_numb = re.search(r'^(?=.*\d).+$', passwd)
    cout_at_least_spec = re.search(r'^(?=.*[$@$!%*#?&]).+$', passwd)

    if not cout_small_pw: return self.SMALL_PW
    elif not cout_large_pw: return self.LARGE_PW
    elif not cout_at_least_lowc: return self.AT_LEAST_LOWC
    elif not cout_at_least_uppc: return self.AT_LEAST_UPPC
    elif not cout_at_least_numb: return self.AT_LEAST_NUMB
    elif not cout_at_least_spec: return self.AT_LEAST_SPEC
    else: return "0"
