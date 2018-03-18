[![Join the chat at https://gitter.im/K4YT3X-DEV/SCUTUM](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/K4YT3X-DEV/SCUTUM?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![status](https://travis-ci.org/K4YT3X/SCUTUM.svg)](https://travis-ci.org/K4YT3X/SCUTUM)
# DefenseMatrix

## This is an alpha version. Please look at "Updates" section for more information before installation.

#### Current Version: 1.0 alpha
**Project Initialized During HackTheNorth**

</br>

## Quick Install
### Prerequisites
* Designed for Linux OS
* `curl` or `wget` is required for quick install
* `git` should be installed

**Detailed dependency list can be found in [DEPENDENCIES.md](https://github.com/K4YT3X/DefenseMatrix/blob/master/DEPENDENCIES.md)**

**via curl**
~~~~
$ sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/K4YT3X/DefenseMatrix/master/quickinstall.sh)"
~~~~

**via wget**
~~~~
$ sudo sh -c "$(wget https://raw.githubusercontent.com/K4YT3X/DefenseMatrix/master/quickinstall.sh -O -)"
~~~~

<br>

## Updates (March 18, 2018):
+ Tested on Kali VM
+ Some minor improvements needed
  + (Maybe) get rid of config file since it's now useless
  + Scheduled security audit?
+ Added Dependency list

<br>

#### Current Version Changes
+ Added detailed file information for every file
+ Added Shebangs for every executable

#### Recent Changes:
+ Deciding to continue this project and add SCUTUM
+ Other decisions about this project is being made

</br>

## Why do you need DefenseMatrix?
During HTN we made a test. Our nameless linux server which is exposed to the internet received roughly 6000 attacks and port scanning attempts every 24 hours. 

</br>

## What is DefenseMatrix?
DefenseMatrix helps individuals and organizations who use Linux to secure their servers on various dimentions automatically. It makes securing a Linux server faster and easier.

Never before have a program been able to have so many security features packed in one. Therefore we provide you with this all-in-one solution that will make the following difficult things easier to handle.

</br>

## DefenseMatrix features:
 - TCP/UDP/ICMP firewall
 - ARP firewall
 - Rootkit Detection
 - Password complexity check
 - Attack analysis and visualization

These basic security features will defend your server(s) against most tech based attacks.  
We configure these things automatically for you.  

</br>


## Uninstallation
We still make it easy for you
~~~~
$ sudo DefenseMatrix --uninstall
~~~~

</br>

## Usage
**OUTDATED**  
This is how you get started with DefenseMatrix
~~~~
$ sudo DefenseMatrix                  # Print Help Page
$ sudo service DefenseMatrix start    # Start DefenseMatrix service
$ sudo service DefenseMatrix stop     # Stop DefenseMatrix service
~~~~

</br>

## What if I want to be more secure?

If you still feel unsafe after installing this security suite, we recommend you to look into IDSs and WAFs. [Snort](https://www.snort.org/) will be a good one to begin with.