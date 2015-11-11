import sys
import json
import re

def hw(sent_file,tweet_file):
	new_scores = compute_new_scores(sent_file,tweet_file)
	for t,(key,value) in enumerate(new_scores.iteritems()): # iteritems is generator
		print "%s %s" %(key,value)


def lines(fp):
    print str(len(fp.readlines()))

def parse_sent_file(file):
	#generate sentiment dictionary from tab seperated text file
	
	scores = {} # initialize an empty dictionary
	for line in file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	return scores

def parse_tweet_file(file):
	#extract text from tweet file
	for line in file:
		data = json.loads(line)
		text = data.get('text','').encode('utf-8')
		split_regex = r'\W+'		
		text_list_raw = re.split(split_regex,text)
		text_list= map(lambda a:a.lower(),filter(None,text_list_raw))
		yield text_list

def compute_new_scores(sent_file,tweet_file):
	new_scores={}
	new_words=[]
	scores = parse_sent_file(sent_file)
	for text_list in parse_tweet_file(tweet_file):
		sum = 0 
		for string in text_list:
			val = scores.get(string,'not_exist')
			if val == "not_exist":
				new_words.append(string)
			else:
				sum +=val

		for word in new_words:
			new_scores[word] = new_scores.get(word,0) + sum

	return new_scores


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
