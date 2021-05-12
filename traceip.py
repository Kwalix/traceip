#!/usr/bin/env python3

__author__ = 'Kwalix <hallerlucas@outlook.com>'
__version__ = '1.0.0'

from optparse import OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")


if __name__ == '__main__':
    main()