import re

class GetKeywords:

	def __init__(self, tag):
		self.tag = tag

	@staticmethod
	def get(tweet, tag):
		if re.findall(tag, tweet):
			label = 1
		else:
			label = 0

		tweet = re.sub("http://t.co/\w+", "", tweet)
		tweet = re.sub("#[a-zA-Z]+","", tweet)

		return {'words': re.findall("[a-zA-Z]+", tweet), 'label': label}

def main(tag):
	f = open("../data/tweets.txt")
	out = open("../data/keywords.txt","w")
	out = open("../data/keywords.txt","a")

	words = {}

	for line in f:
		line = re.sub("http://.+? ", "", line)
		line = re.sub("#tech","", line)

		for word in re.findall("[a-zA-Z]+", line):
			if word in words:
				words[word] += 1
			else:
				words[word] = 1

	out.write(words.__str__())


if __name__ == '__main__':
	main('tech')