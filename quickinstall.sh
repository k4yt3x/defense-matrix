#!/bin/bash
# Name: Defense Matrix Quick Installation Script
# Author: K4YT3X
# Date Created: Sep 27, 2017
# Last Modified: October 19, 2018
# Version 1.0.1

# Check if user is root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Remove older versions of defense matrix
if [ -d "/usr/share/defense-matrix/" ]; then
  echo "Removing old defense matrix files..."
  rm -rf /usr/share/defense-matrix/
fi

# Clone the newest version of defense matrix
git clone https://github.com/K4YT3X/defense-matrix.git /usr/share/defense-matrix

# Run the installation script
/usr/bin/env python3 /usr/share/defense-matrix/bin/defense-matrix.py --install