# reddit-msg

A barebones CLI for sending Reddit messages with [PRAW](https://praw.readthedocs.io). Made this so I can execute scripts with long/unknown runtimes, walk away from my computer, and get notified on my phone when it's done. Email/SMS could work too, but chances are I'd be browsing Reddit anyway while waiting. 

## Requirements

- python3
- configparser
- argparse
- praw

## Setup

1. Download `reddit-msg.py`
2. Create a configuration file, `reddit-msg.conf`, in your `~/.config/` directory. An alternative path can be specified by editing the python script. See `reddit-msg.conf.example` for the configuration schema.
3. Register an app with Reddit and put the relevant authentication variables in the configuration file.
4. Put your default recipient username and message subject in the configuration file.

## Usage

My typical usage: `$ some-script ; reddit-msg "script is done"`

From the `--help` flag:

	usage: reddit-msg.py [-h] [-u USER] [-s SUBJECT] body

	send a private message to a reddit user. authentication variables and default
	arguments sourced from ~/.config/reddit-msg.conf

	positional arguments:
	  body                  body text of message

	optional arguments:
	  -h, --help            show this help message and exit
	  -u USER, --user USER  reddit username of recipient
	  -s SUBJECT, --subject SUBJECT
							subject text of message

