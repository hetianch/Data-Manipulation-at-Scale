from __future__ import division
import sys
import re
import json


def get_frequency(tweet_file):
	term_dict = {}
	total_count = 0
	for text_list in parse_tweet_file(tweet_file):
		for text in text_list:
			term_dict[text] = int(term_dict.get(text,0))+1
			total_count += 1

	return (term_dict,total_count)

def display_count(term_dict):
	for t,(key, val) in enumerate(sorted(term_dict.iteritems(), key=lambda (k,v): (v,k), reverse = True)): #sort by val then key
		print "%s %i" %(key, val)
		if t == 9:
			break

def parse_tweet_file(file):
	#extract text from tweet file
	for line in file:
		data = json.loads(line)
		entities = data.get("entities",0)
		if entities != 0 :
			hashtags = entities.get("hashtags",0)
			if hashtags !=0 :
				tag_list = [s.get('text','').encode('utf-8') for s in hashtags]
				if tag_list:
					tag_list= map(lambda a:a.lower(),filter(None,tag_list))
					yield tag_list


def main():
    tweet_file = open(sys.argv[1])
    term_dict,total_count=get_frequency(tweet_file)
    display_count(term_dict)


if __name__ == '__main__':
    main()
