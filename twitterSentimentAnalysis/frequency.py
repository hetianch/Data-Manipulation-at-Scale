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

def display_frequency(term_dict,total_count):
	for key,val in term_dict.iteritems():
		print "%s %0.4f" %(key, val/total_count)

def parse_tweet_file(file):
	#extract text from tweet file
	for line in file:
		data = json.loads(line)
		text = data.get('text','').encode('ascii',"ignore") # ignore non-ascii terms
		split_regex = r'\W+'		
		text_list_raw = re.split(split_regex,text)
		text_list= map(lambda a:a.lower(),filter(None,text_list_raw))
		yield text_list


def main():
    tweet_file = open(sys.argv[1])
    term_dict,total_count=get_frequency(tweet_file)
    display_frequency(term_dict,total_count)


if __name__ == '__main__':
    main()
