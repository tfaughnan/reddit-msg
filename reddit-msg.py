#!/usr/bin/env python

import os
import configparser
import argparse
import praw

config_file = os.path.expanduser('~/.config/reddit-msg.conf')
assert os.path.exists(config_file)

cparser = configparser.ConfigParser()
cparser.read(config_file)

aparser = argparse.ArgumentParser(description=f'send a private message to a reddit user. authentication variables and default arguments sourced from {config_file}')
aparser.add_argument('body', help='body text of message')
aparser.add_argument('-u', '--user', default=cparser.get('Message', 'default_user'), help=f'reddit username of recipient, default is {cparser.get("Message", "default_user")}')
aparser.add_argument('-s', '--subject', default=cparser.get('Message', 'default_subject'), help=f'subject text of message, default is {cparser.get("Message", "default_subject")}')
args = aparser.parse_args()

reddit = praw.Reddit(client_id=cparser.get('Authentication', 'client_id'),
        client_secret=cparser.get('Authentication', 'client_secret'),
        user_agent=cparser.get('Authentication', 'user_agent'),
        username=cparser.get('Authentication', 'username'),
        password=cparser.get('Authentication', 'password'))
reddit.redditor(args.user).message(args.subject, args.body)

