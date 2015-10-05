import sys
import json


def get_scores(files):

    scores = {}  # initialize empty dictionary
    for line in files:
        # The file is tab-delimited. "\t" means "tab character"
        term, score = line.split("\t")
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def calcu_score():
    senti_file = open(sys.argv[1])
    #senti_file= open("AFINN-111.txt")
    #tweet_file = open("output.txt")
    #tweet_file = open("problem_1_submission.txt")
    tweet_file = open(sys.argv[2])

    scores = get_scores(senti_file)

    # parse the tweet file line by line
    for line in tweet_file:
        tweet = json.loads(line)  # parse JSON text line
        # get tweet text (or return "" if no text field exists)
        if 'text' in tweet:
            tweet_text = tweet['text']
        else:
            tweet_text = ""
        # get list of words from tweet text
        tweet_words = tweet_text.split(" ")
        # get sum of word scores
        score = 0
        for word in tweet_words:
            if word in scores:
                score += scores[word]

        print score

if __name__ == '__main__':
    calcu_score()
