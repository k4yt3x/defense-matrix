from logger import logger
import os
import subprocess

log = logger()


class ufw:
    def __init__(self):
        pass

    def adjustStatus():
        """
        Checks and adjusts the default rules of ufw which control outgoing data
        and incoming data.
        We drop all incoming data by default
        """
        cout = subprocess.Popen(["ufw", "status", "verbose"], stdout=subprocess.PIPE).communicate()[0]
        coutparsed = cout.decode().split('\n')
        for line in coutparsed:
            if "Default:" in line:
                if not (line.split(' ')[1] + line.split(' ')[2] == "deny(incoming),"):
                    print(line.split(' ')[1] + line.split(' ')[2])
                    log.writeLog("Adjusting default rule for incoming packages to drop")
                    os.system("ufw default deny incoming")
                if not (line.split(' ')[3] + line.split(' ')[4] == "allow(outgoing),"):
                    line.split(' ')[3] + line.split(' ')[4]
                    log.writeLog("Adjusting default rule for outgoing packages to allow")
                    os.system("ufw default allow outgoing")
            if 'inactive' in line:
                log.writeLog("Enabling ufw")
                os.system("ufw enable")

    def allow(port):
        """
        Accept all traffic from one address

        Arguments:
            port {int} -- Port number
        """
        log.writeLog("Allowing port " + str(port))
        os.system("ufw allow " + str(port) + "/tcp")

    def expire(port):
        """
        Disallows all traffic from one address

        Arguments:
            port {int} -- Port number
        """
        log.writeLog("Expiring port " + str(port))
        os.system("ufw --force delete allow " + str(port) + "/tcp")

    def generateStatistics():
        """
        Generates a statistic csv file at /tmp/dmstats.csv
        """
        log.writeLog("Stats Generation")
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
