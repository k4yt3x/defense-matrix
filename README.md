<center>
<font face="Fira Code">

# Defense MatriX

**Full security solution for Linux Servers**

</font>
</center>
</br>

### Project Initialized During HackTheNorth


#### Current Version: 0.9 alpha

Recent Changes:
+ Deciding to continue this project and add SCUTUM
+ Other decisions about this project is being made


</br>

## SCUTUM is to be added into DefenseMatrix Project
After consideration, SCUTUM, as a nice firewall controller, is to be added into DefenseMatrix. It will soon replace the iptables controller and arptables controller in DefenseMatrix. Expect lots of improvements.

</br>

## What is DefenseMatrix?
DefenseMatrix helps individuals and organizations who use Linux to secure their servers on various dimentions automatically. It makes securing a Linux server faster and easier.

Never before have a program been able to have so many security features packed in one. Therefore we provide you with this all-in-one solution that will make the following difficult things easier to handle.

</br>

## Why do we need to secure Linux?
Did you know that an ordinary server receives almost 6000 attacks per day? With our help, these attacks don't come in.


</br>

## DefenseMatrix features:
 - iptables tcp/udp/icmp firewall
 - arptables ARP firewall
 - Rootkit Detection
 - Password complexity check
 - Attack analysis and visualization

We configure these things automatically for you.

</br>

## Installation
We make it fast, easy, and simple
~~~~
$ sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/K4YT3X/DefenseMatrix/master/quickinstall.sh)"
~~~~

</br>


## Uninstallation
We still make it easy for you
~~~~
$ sudo DefenseMatrix --uninstall
~~~~

</br>

## Usage
This is how you get started with DefenseMatrix
~~~~
$ sudo DefenseMatrix                  # Print Help Page
$ sudo service DefenseMatrix start    # Start DefenseMatrix service
$ sudo service DefenseMatrix stop     # Stop DefenseMatrix service
~~~~