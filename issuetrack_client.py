#!/usr/bin/env python3

import requests
from collections import defaultdict
import csv

URL = 'http://127.0.0.1:8000/bug_api/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

def test_request_types():
    getbugs = requests.get(URL + 'bugs/', headers=headers, auth=('admin','123456'))
    getbug = requests.get(URL + 'bugs/7/', headers=headers, auth=('admin','123456'))
    getcomms = requests.get(URL + 'comments/', headers=headers, auth=('admin','123456'))
    getcomm = requests.get(URL + 'comments/2/', headers=headers, auth=('admin','123456'))

    print('getbugs', getbugs)
    print('getbug', getbug)
    print('getcomms', getcomms)
    print('getcomm', getcomm)

    bug = {
    "package": "Swift",
    "status": "Closed",
    "version": "9.0",
    "summary": "regular bug" }

    comment = {
    "bug": "7",
    "user": "username",
    "content": "I love this bug"
    }

    postbugs = requests.post(URL + 'bugs/', data=bug, headers=headers, auth=('admin','123456'))
    postcomms = requests.post(URL + 'comments/', data=comment, headers=headers, auth=('admin','123456'))

    print('postbugs', postbugs)
    print('postcomms', postcomms)

    putbug = requests.put(URL + 'bugs/9/', data=bug, headers=headers, auth=('admin','123456'))
    putcomm = requests.put(URL + 'comments/3/', data=comment, headers=headers, auth=('admin','123456'))

    print('putbug', putbug)
    print('putcomm', putcomm)

    delbug = requests.delete(URL + 'bugs/10/', data=bug, headers=headers, auth=('admin','123456'))
    delcomm = requests.delete(URL + 'comments/5/', data=comment, headers=headers, auth=('admin','123456'))

    print('delbug', delbug)
    print('delcomm', delcomm)


def generate_bug_csv(data):
    res = defaultdict(int)
    for bug in data:
        package = bug['package']
        res[package] += 1

    with open('total_bugs_per_package.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        for package, count in res.items():
            writer.writerow([package, count])

def generate_comment_csv(data):
    res = defaultdict(int)
    for comment in data:
        bug = comment['bug']
        res[bug] += 1

    with open('total_comments_per_bug.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        for bug, comments in res.items():
            writer.writerow([bug, comments])

def main():
    #test_request_types()

    # Q2 Part 1
    bugs_response = requests.get(URL + 'bugs/', headers=headers, auth=('admin','123456'))
    data = bugs_response.json()['results']
    next = bugs_response.json()['next']
    
    while next:
        bugs_response = requests.get(next, headers=headers, auth=('admin','123456'))
        data += bugs_response.json()['results']
        next = bugs_response.json()['next']

    generate_bug_csv(data)


    # Q2 Part 2
    comms_response = requests.get(URL + 'comments/', headers=headers, auth=('admin','123456'))
    data = comms_response.json()['results']
    next = comms_response.json()['next']
    
    while next:
        comms_response = requests.get(next, headers=headers, auth=('admin','123456'))
        data += comms_response.json()['results']
        next = comms_response.json()['next']

    generate_comment_csv(data)
    

if __name__ == '__main__':
    main()