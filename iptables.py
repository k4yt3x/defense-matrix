import os
import subprocess


class ufw:
    def __init__(self):
        pass

    def getDefaultRule(self):
        """
        Checks if the default rule of iptables is ACCEPT or DROP
        """
        cout = subprocess.Popen(["ufw", "status", "verbose"], stdout=subprocess.PIPE).communicate()[0]
        coutparsed = cout.decode().split('\n')
        for line in coutparsed:
            if "Default:" in line:
                if not (line.split(' ')[1] + line.split(' ')[2] == "deny (incoming),"):
                    os.system("ufw default deny incoming")
                if not (line.split(' ')[3] + line.split(' ')[4] == "allow (outgoing),"):
                    os.system("ufw default allow outgoing")

    def allow(port):
        """
        Accept all traffic from one address

        Arguments:
            address {string} -- Address of target machine
            port {int} -- Port number
        """
        os.system("ufw allow " + str(port) + "/tcp")

    def expire(port):
        """
        Disallows all traffic from one address

        Arguments:
            address {string} -- Address of target machine
        """
        os.system("ufw --force delete allow " + str(port) + "/tcp")

    def generateStatistics():
        """
        Generates a statistic csv file at /tmp/dmstats.csv
        """
        iptables_logs = []
        with open("/var/log/messages", "r") as message:
            for line in message:
                if "UFW BLOCK" in line:
                    iptables_logs.append(line)
            message.close()
        stats = {}
        for line in iptables_logs:
            line = line.split(' ')
            for section in line:
                if "SRC" in section:
                    if section.replace("SRC=", '') not in stats:
                        stats[section.replace("SRC=", '')] = 1
                    else:
                        stats[section.replace("SRC=", '')] += 1
        with open("/tmp/dmstats.csv", "w") as statsf:
            for index in sorted(stats, key=stats.get, reverse=True):
                if index != "127.0.0.1":
                    statsf.write(index + ',' + str(stats[index]) + "\n")
            statsf.close()
