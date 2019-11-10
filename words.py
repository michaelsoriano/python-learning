#!/usr/bin/env python3
"""Fetch a list of words from a URL

Usage: 

    python3 words.py http://sixty-north.com/c/t.txt
""" 
import sys
from urllib.request import urlopen

def fetch_words(url):       
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def pr_items(items):
    for item in items:
        print(item)


def main(url):
    pr_items(fetch_words(url))


if __name__ == '__main__':
    main(sys.argv[1])