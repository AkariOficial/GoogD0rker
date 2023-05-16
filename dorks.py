#!/usr/bin/python3
# GoogD0rk3r 3.0 && Akari
# Python 3 re-write of version 2.0

import argparse
from re import L
from googlesearch import search
from time import sleep

def main():
    parser = argparse.ArgumentParser(description='GoogD0rker performs Google dork queries to uncover information about a domain.')
    parser.add_argument('-d', '--domain', required=True, help='Specify the target domain, e.g., target.com')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode for debugging purposes')
    args = parser.parse_args()

    site = args.domain
    results_list = []

    dorks = {
        'site': 'site:"{}" inurl:"wp-" OR inurl:"plugin" OR inurl:"upload" OR inurl:"download"'.format(site),
        'php': 'inurl:"?id=" AND filetype:"php"',
        'loginPage': 'loginpage.txt'
    }

    for dork in dorks:
        if args.verbose:
            print("Currently Running: {}".format(dorks[dork]))

        search_results = search(dorks[dork], tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
        print(next(search_results))
        results_list.extend(search_results)
        sleep(4)

    print(results_list)


if __name__ == '__main__':
    main()

