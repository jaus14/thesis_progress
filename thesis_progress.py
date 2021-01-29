#!/usr/bin/env python3
import PyPDF2
import argparse
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

def get_progressBar(percentage):
    progressBar = "| "
    for i in range(20):
        if i < int(percentage/5):
            progressBar = progressBar + '#'
        else:
            progressBar = progressBar + '-'
    progressBar = progressBar + " | " + '{:.1f}'.format(percentage) + '%'
    return progressBar

def tweet(percentage, custom="%BAR%"):
    twitter = OAuth1Session(CK, CS, AT, ATS)
    url = "https://api.twitter.com/1.1/statuses/update.json"

    params = {"status" : custom.replace("%BAR%", get_progressBar(percentage))}
    res = twitter.post(url, params = params)

    if res.status_code == 200:
        print("Tweet Success.")
    else:
        print("Tweet Failed. : %d"% res.status_code)

def update_profile(percentage, custom="%BAR%"):
    twitter = OAuth1Session(CK, CS, AT, ATS)
    url = "https://api.twitter.com/1.1/account/update_profile.json"
    
    params = {"description" : custom.replace("%BAR%", get_progressBar(percentage))}
    res = twitter.post(url, params = params)

    if res.status_code == 200:
        print("Profile Update Success.")
    else:
        print("Profile Update Failed. : %d"% res.status_code)

def print_progress(percentage, custom="%BAR%"):
    print(custom.replace("%BAR%", get_progressBar(percentage)))

def handler(args):
    if args.file == None:
        print("need -f FILE")
        return
    pdf = PyPDF2.PdfFileReader(open(args.file, "rb"))
    if args.customize == None:
        args.handler(pdf.getNumPages()*100/args.goal)
    else:
        args.handler(pdf.getNumPages()*100/args.goal, args.customize)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Thesis Progress')
    subparsers = parser.add_subparsers()

    parser_tweet = subparsers.add_parser('tweet', help='see `tweet -h`')
    parser_tweet.add_argument('-c', '--customize', action='store', type=str, help='customize tweet. put `%%BAR%%` where you want to put the progress bar.')
    parser_tweet.add_argument('-f', '--file', action='store', type=str, help='file name')
    parser_tweet.add_argument('-g', '--goal', action='store', type=int, help='goal page')
    parser_tweet.set_defaults(handler=tweet)
    parser_tweet.set_defaults(goal=50)

    parser_print = subparsers.add_parser('print', help='print `print -h`')
    parser_print.add_argument('-c', '--customize', action='store', type=str, help='customize text. put `%%BAR%%` where you want to put the progress bar.')
    parser_print.add_argument('-f', '--file', action='store', type=str, help='file name')
    parser_print.add_argument('-g', '--goal', action='store', type=int, help='goal page')
    parser_print.set_defaults(handler=print_progress)
    parser_print.set_defaults(goal=50)

    parser_update_profile = subparsers.add_parser('update_profile', help='see `update_profile -h`')
    parser_update_profile.add_argument('-c', '--customize', action='store', type=str, help='customize profile description. put `%%BAR%%` where you want to put the progress bar.')
    parser_update_profile.add_argument('-f', '--file', action='store', type=str, help='file name')
    parser_update_profile.add_argument('-g', '--goal', action='store', type=int, help='goal page')
    parser_update_profile.set_defaults(handler=update_profile)
    parser_update_profile.set_defaults(goal=50)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        handler(args)
    else:
        parser.print_help()