#!/usr/bin/python2
#-*- coding:utf-8 -*-

import sys
import tweepy
import random

###### DO NOT TOUCH THESE STRINGS OR THE SCRIPT WON'T WORK ANYMORE ######
CONKEY = 'LOL'
CONSECRET = 'NOPE'

count = 0
arg = sys.argv[1]

# Random word from a dictionary
randword = open('list').read().splitlines()
randomline =random.choice(randword)
tweetargu = ('%s %s') % (arg, randomline)
# config file test
try:
	conf = open('./.hth.conf')
	conf.close()
except IOError:
	print "Missing config file, creating one now..."
	conf = open('.hth.conf', 'w')
	auth = tweepy.OAuthHandler(CONKEY, CONSECRET)
	auth_url = auth.get_authorization_url()
	print 'Please authorize: ' + auth_url
	verifier = raw_input('PIN: ').strip()
	auth.get_access_token(verifier)
	print "Copy and paste ACCESS_KEY and ACCESS_SECRET in ~/.hth.conf, then you can finally use HackThatHashtag"
	print "ACCESS_KEY = %s" % auth.access_token.key
	print "ACCESS_SECRET = %s" % auth.access_token.secret
	exit()


# Tweet, awwwww yeaaah
# config file parser, thanks to http://www.decalage.info/en/python/configparser
COMMENT_CHAR = '#'
OPTION_CHAR =  '='
filename = '.hth.conf'
def parse_config(filename):
    options = {}
    f = open(filename)
    for line in f:
        # First, remove comments:
        if COMMENT_CHAR in line:
            # split on comment char, keep only the part before
            line, comment = line.split(COMMENT_CHAR, 1)
        # Second, find lines with an option=value:
        if OPTION_CHAR in line:
            # split on option char:
            option, value = line.split(OPTION_CHAR, 1)
            # strip spaces:
            option = option.strip()
            value = value.strip()
            # store in dictionary:
            options[option] = value
    f.close()
    return options

options = parse_config(filename)

auth = tweepy.OAuthHandler(CONKEY, CONSECRET)
auth.set_access_token(options['ACCESS_KEY'], options['ACCESS_SECRET'])
api = tweepy.API(auth)
def increment():
	global count
	count+=1
	
while 1:
	# Random word from a dictionary + tweet
	randword = open('list').read().splitlines()
	randomline =random.choice(randword)
	tweetargu = ('%s %s') % (arg, randomline)
	api.update_status(tweetargu)
	increment()
	print('Sent %i tweets') % (count)
