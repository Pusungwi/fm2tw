#!/usr/bin/env python
import os
from twitter import *

def main(filename='config.yaml'):
	CONSUMER_APP_NAME = "fm2tw"
	CONSUMER_KEY = "7eRve9CnBu9zngpU9ILBg"
	CONSUMER_SECRET = "ar7ow7RL6kkJnaFaJm3dKVHzTghBidzRarR9GNASOc"
	
	tmpCredentialFile = os.path.expanduser('~/.tmpcred')
	oauth_dance(CONSUMER_APP_NAME, CONSUMER_KEY, CONSUMER_SECRET, tmpCredentialFile)
	ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET = read_token_file(tmpCredentialFile)
	os.remove(tmpCredentialFile)
	lastfm = input("LASTFM ID? ").strip()
	LASTFM_FEED = \
		"http://ws.audioscrobbler.com/2.0/user/%s/recenttracks.rss" % lastfm
	f = open(filename, "w")
	f.write("CONSUMER_KEY: {0}\n".format(CONSUMER_KEY))
	f.write("CONSUMER_SECRET: {0}\n".format(CONSUMER_SECRET))
	f.write("ACCESS_TOKEN_KEY: {0}\n".format(ACCESS_TOKEN_KEY))
	f.write("ACCESS_TOKEN_SECRET: {0}\n".format(ACCESS_TOKEN_SECRET))
	f.write("LASTFM_FEED: {0}\n".format(LASTFM_FEED))

if __name__ == "__main__":
        main()
