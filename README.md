# Defense Matrix (Archived Project)

This project was an attempt to automate various aspects of Linux security auditing and hardening. As time passed, I (K4YT3X) found many of the methodologies used in this project to be unideal and obsolete. Therefore, I recommend not continuing using this project but instead turning towards more advanced, up-to-date solutions. Below are some examples.

- UFW (Uncomplicated Firewall): UFW is a wrapper of iptables/nftables. It makes configuring firewall fast and easy. If you have no experience configuring firewalls, or if you do not want to edit the rules manually, UFW is an excellent option to consider.
- [ArpON](http://arpon.sourceforge.net/): ArpON is a host-based ARP monitoring and MITM prevention software. There are also other solutions like arpwatch and arpalert.
- Lynis: Lynis is a Linux security auditing tool that helps you to identify security issues on a Linux host. It is also capable of checking a host's compliance with security standards.
- PAM: Instead of replacing the original `/usr/bin/passwd`, it's recommended for you to set appropriate password complexity rules in PAM.

This project might be revived as a generic Linux hardening script in the future, but there's too much uncertainty lying in front of this project.

---

[![Join the chat at https://gitter.im/K4YT3X-DEV/DefenseMatrix](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/K4YT3X-DEV/DefenseMatrix?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![status](https://travis-ci.org/K4YT3X/defense-matrix.svg)](https://travis-ci.org/K4YT3X/DefenseMatrix)

## Warning: `passwd` Binary Bug

The current method that defense matrix is using to enforce higher password strength seems defective. Therefore we have temporarily disabled the replacement of default system `passwd` binary.

If you wish to recover your default `passwd` binary file, please execute the following command to move the original binary back to its place.

```shell
sudo mv /usr/bin/oldpasswd /usr/bin/passwd
```

In the future, we'll be using a more stable, robust and secure way to implement this feature.

## 1.1.0 (October 20, 2018)

- Rearranged executable files.
- Removed everything that's redundant.
- All tests passed. We are not expecting major bugs.
- Integration with SCUTUM firewall fixed.
- Unified code style (`'` and `"`, function and variable naming scheme)

## Quick Install

### Prerequisites

- Designed for Linux OS
- `curl` or `wget` is required for quick install
- `git` should be installed

**Detailed dependency list can be found in [DEPENDENCIES.md](https://github.com/K4YT3X/defense-matrix/blob/master/DEPENDENCIES.md)**

Via `curl`:

```shell
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/K4YT3X/defense-matrix/master/quickinstall.sh)"
```

Via `wget`:

```shell
sudo bash -c "$(wget https://raw.githubusercontent.com/K4YT3X/defense-matrix/master/quickinstall.sh -O -)"
```

## What is Defense Matrix?

DefenseMatrix helps individuals and organizations who use Linux to secure their servers on various dimensions automatically. It makes securing a Linux server faster and easier.

Never before have a program been able to have so many security features packed in one. Therefore we provide you with this all-in-one solution that will make the following difficult things easier to handle.

## Why do you need Defense Matrix?

During HTN we made a test. Our nameless linux server which is exposed to the internet received roughly 6000 attacks and port scanning attempts every 24 hours.

## Defense Matrix Features

### `scutum`

- TCP/UDP/ICMP firewall
- ARP firewall

### `tiger` & `rkhunter`

- Rootkit Detection
- Configuration sanity check

### Other

- Password complexity check

### TODO

- Attack analysis and visualization

These basic security features will defend your server(s) against most tech based attacks.
We configure these things automatically for you.

## Uninstallation

We make this easy for you.

```shell
sudo defense-matrix --uninstall
```

## Usages

**ALL commands require root privilege.**

### Firewall Controls

Firewall is controlled by [SCUTUM Firewall](https://github.com/K4YT3X/scutum). For more details please visit [SCUTUM Help Page](https://github.com/K4YT3X/scutum/blob/master/README.md)

```shell
sudo openport [port1] [port2] [port3]      # Open tcp ports
sudo closeport [port1] [port2] [port3]     # Close tcp ports
sudo service scutum start     # Start scutum service
sudo service scutum stop      # Stop scutum service
sudo systemctl enable scutum  # Start SCUTUM with system
sudo systemctl disable scutum # Don't start SCUTUM with system
sudo scutum                   # Start SCUTUM Normally
sudo scutum --start           # Start SCUTUM Manually for once even it it's disabled
sudo scutum --enable          # Enable SCUTUM (Start automatically on connect)
sudo scutum --disable         # Disable SCUTUM (Don't start automatically on connect)
sudo scutum --reset           # Reset SCUTUM (Allow ALL ARP packages temporarily)
sudo scutum --purgelog        # Purge SCUTUM logs
sudo scutum --install         # Run scutum installation wizard and install SCUTUM into system
sudo scutum --uninstall       # Remove SCUTUM from system completely
sudo scutum --upgrade         # Upgrade SCUTUM and AVALON Framework
```

### Security Audit

Defense Matrix installs a number of security auditing tools for you, and more could be added later. To save you time executing those commands separately, we condense everything in to one command which will execute them all.

```shell
sudo defense-matrix --audit
```

### Password Complexity Check

The default `passwd` binary will be replaced by our enhanced `passwd` command, and the old binary file will be backed up at `/usr/bin/oldpasswd`. When you change the password using `passwd` after installing Defense Matrix, it will require password with higher complexity.

**TODO**
To restore the original passwd binary file:

```shell
sudo passwd --restore
```

## What if I want to be more secure?

If you still feel unsafe after installing this security suite, we recommend you to look into IDSs and WAFs. [Snort](https://www.snort.org/) will be a good one to begin with.
