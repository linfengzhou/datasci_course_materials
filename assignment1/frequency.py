import json
import sys
import string

def format_text(text):
    
    
    letter = [] 
    for i in text:
        if i in string.letters:
            letter.append(i)
        else:
            letter.append(" ")

    text = "".join(letter)
        
    # change everything to lowercase and return
    return text.lower()

def main():
    tweet_file = open(sys.argv[1])

    words_stat = {}
        
    # parse the tweet file line by line
    # and build positive and negative word counts
    for line in tweet_file:
        tweet = json.loads(line)  # parse JSON text line

        if 'text' in tweet:
            tweet_text = tweet['text']
        else:
            tweet_text = ""
        tweet_text = format_text(tweet_text)    

        tweet_words = tweet_text.split(" ")
        
        for word in tweet_words:
            if word in words_stat:
                words_stat[word] += 1
            else:
                words_stat[word] = 1
        
    # remove "" from list
    words_stat.pop("", 0)
    
    # get sum of all terms
    total_words = sum([words_stat[word] for word in words_stat])
    
    # print out all key:value pairs
    for word in words_stat:
        print word, float(words_stat[word])/total_words

if __name__ == "__main__":
    main()