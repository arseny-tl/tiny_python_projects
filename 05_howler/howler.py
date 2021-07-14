#!python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Howler (upper-cases input)
"""

import argparse
import io
import os


# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, encoding='UTF-8')
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, mode='wt', encoding='UTF-8') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
