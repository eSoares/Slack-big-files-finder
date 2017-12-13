import json
import requests
import argparse


def find_files(token, channel=None, number_of_files_to_print=5):
    url = "https://slack.com/api/files.list?token={}".format(token)
    if channel:
        url = url + "&channel={}".format(channel)

    a = requests.get(url)
    b = a.json().get("files")
    total_pages = int(a.json().get("paging").get("pages"))
    count = 1
    while (total_pages - count) >= 0:
        a = requests.get(url + "&page=" + str(count))
        b = b + a.json().get("files")
        count += 1

    b.sort(key=lambda x: int(x.get('size')))
    for i in b[-1*number_of_files_to_print:]:
        print("%s (%.2fMB)" % (i.get("permalink"), int(i.get("size")) / (1024.0 * 1024)))

    print("Total size in public files is %.2fMB" % (sum(map((lambda x: int(x.get("size"))), b)) / (1024.0 * 1024)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str)
    parser.add_argument("--c", dest="channel", type=str)
    parser.add_argument("--f", dest="nfiles", type=int, default=5)
    args = parser.parse_args()
    if not args or not args.token:
        parser.print_help()
    else:
        find_files(args.token, args.channel, args.nfiles)
    token = "YOUR TOKEN HERE"
    channel = None
