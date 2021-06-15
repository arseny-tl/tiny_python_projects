#!python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-noc',
                        '--no-oxford-comma',
                        help='Not to print Oxford comma',
                        action='store_true')

    parser.add_argument('-cs',
                        '--custom-separator',
                        help='Separate items with a custom character',
                        metavar='str',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.str

    if args.sorted:
        items.sort()

    separator = args.custom_separator if args.custom_separator else ','
    separator += ' '
    count = len(items)
    if count == 1:
        result = items[0]
    elif count == 2:
        result = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        if args.no_oxford_comma:
            result = separator.join(
                items[:len(items) - 1]) + ' ' + items[len(items) - 1]
        else:
            result = separator.join(items)

    print(f'You are bringing {result}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
