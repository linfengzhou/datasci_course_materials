import sys
import json
from operator import itemgetter


def main():
    tweet_file = open(sys.argv[1])
    
    stats = {}
    
    for line in tweet_file:
        tweet = json.loads(line)  ## parse JSON text line
        
        if "entities" in tweet:
            for tag in tweet["entities"]["hashtags"]:
                tag_text = tag["text"]
                if tag_text in stats:
                    stats[tag_text] += 1
                else:
                    stats[tag_text] = 1
    
    stat = stats.items()
    stat.sort(key=itemgetter(1), reverse=True)
    
    for i in range(10):
        print stat[i][0], stat[i][1]

if __name__ == "__main__":
    main()