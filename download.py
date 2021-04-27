#!/bin/env python
"""
Emblem Academy Padlet Downloader
Usage: python download.py padletfile.csv
"""

import os
import sys
import requests
import csv

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Please specify padlet CSV file")
        sys.exit(1)

    padlet_csv = sys.argv[1]
    if not os.path.exists(padlet_csv) or not os.path.isfile(padlet_csv):
        print("File does not exist or is not a file.")
        sys.exit(2)

    bn = padlet_csv[0:padlet_csv.rindex(".")]
    print("Padlet CSV File:", padlet_csv)
    print("Padlet Target Dirctory: ", bn)

    if not os.path.exists(bn):
        os.mkdir(bn)
    
    with open(padlet_csv, newline='') as csvfile:
        padreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        n = 0
        for row in padreader:
            if n > 0:
                img_url = row[2]
                img_bn = os.path.basename(img_url)
                img_tgt = "%s/%s"%(bn, img_bn)
                if not os.path.exists(img_tgt):
                    print("Downloading", img_url, "to", img_bn)
                    r = requests.get(img_url, allow_redirects=True)
                    open(img_tgt, 'wb').write(r.content)
            n = n + 1