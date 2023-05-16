#!/usr/bin/python3
# GoogD0rk3r 3.0
# Python 3 re-write of version 1.0

import argparse
import time
import httpx


def main():
    parser = argparse.ArgumentParser(description='GoogD0rker performs Google dork queries to uncover information about a domain.')
    parser.add_argument('-d', '--domain', required=True, help='Specify the target domain, e.g., target.com')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode for debugging purposes')
    args = parser.parse_args()

    site = args.domain
    results_list = []

    dorks = {
        'site': 'site:"{}" OR inurl:"gov"'.format(site),
        'php': 'inurl:"?id=" AND filetype:"php"',
        'loginPage': 'loginpage.txt'
    }

    for dork in dorks:
        if args.verbose:
            print("Currently Running: {}".format(dorks[dork]))

        search_results = google_search(dorks[dork])

        results_list.extend(search_results)

        # Aguarde 5 segundos antes de fazer a próxima solicitação
        # time.sleep(5)

    print(results_list)


def google_search(query):
    url = 'https://www.google.com/search?q=' + query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'
    }

    response = httpx.get(url, headers=headers)
    response.raise_for_status()

    return extract_urls(response.text)


def extract_urls(html):
    urls = []
    start_marker = '<a href="/url?q='
    end_marker = '&amp;sa='
    start_index = html.find(start_marker)

    while start_index != -1:
        end_index = html.find(end_marker, start_index)
        url = html[start_index + len(start_marker):end_index]

        if url.startswith('http'):
            urls.append(url)

        start_index = html.find(start_marker, end_index)

    return urls


if __name__ == '__main__':
    main()

