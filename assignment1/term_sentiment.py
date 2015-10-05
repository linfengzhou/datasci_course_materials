import sys
import json


def get_scores(files):

    scores = {}  # initialize empty dictionary
    for line in files:
        # The file is tab-delimited. "\t" means "tab character"
        term, score = line.split("\t")
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    senti_file = open(sys.argv[1])
    #senti_file= open("AFINN-111.txt")
    #tweet_file = open("output.txt")
    #tweet_file = open("problem_1_submission.txt")
    tweet_file = open(sys.argv[2])

    # read the file with scores into a dictionary
    scores = get_scores(senti_file)

    # initialize dictionaries for positive and negative word counts
    pos_dic = {}

    # parse the tweet file line by line
    # and build positive and negative word counts
    for line in tweet_file:
        tweet = json.loads(line)  # parse JSON text line

        if 'text' in tweet:
            tweet_text = tweet['text']
        else:
            tweet_text = ""

        tweet_words = tweet_text.split(" ")

        pos_count = 0

        for word in tweet_words:
            if word in scores:
                if scores[word] > 0:
                    pos_count += 1

        for word in tweet_words:
            if word not in scores and len(word) > 2:
                if word in pos_dic:
                    pos_dic[word] += pos_count
                else:
                    pos_dic[word] = pos_count

    for word in pos_dic:
        pos_score = pos_dic[word]
        print word, float(pos_score)


if __name__ == '__main__':
    main()
