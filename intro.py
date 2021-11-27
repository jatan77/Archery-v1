import time
import sys
import os

def design():
    lines = ["          * Coded By Hardik Makvana * [Version 2.0]"]
    print("""
           d8888                  888
          d88888                  888
         d88P888                  888
        d88P 888 888d888  .d8888b 88888b.   .d88b.  888d888 888  888
       d88P  888 888P"   d88P"    888 "88b d8P  Y8b 888P"   888  888
      d88P   888 888     888      888  888 88888888 888     888  888
     d8888888888 888     Y88b.    888  888 Y8b.     888     Y88b 888
    d88P     888 888      "Y8888P 888  888  "Y8888  888      "Y88888
                                                                 888
                                                            Y8b d88P
                                                             "Y88P" """)
    for line in lines:
        for c in line:
            print c,; sys.stdout.write(u"")
            sys.stdout.flush()
            time.sleep(0.05)
        print u''
