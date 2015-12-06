import feedparser

## d = feedparser.parse('http://www.reddit.com/r/python/.rss')

d = feedparser.parse('https://azure.microsoft.com/en-us/updates/feed/')
## print(d.version)
## print(d.feed.title)
## print(d['feed']['title'])
## d.entries[0].content[0].type
print d.entries[2]
##print(d['feed']['title'])

## print(d['feed']['tags'])

## print d.entries.title

##for post in d.entries:
##    print post.title + ":" + post.published

 ##   + ":" + post.summary

##for post in d.feed:
##    print post.tags

    ##+ ":" + post.published + ":" + post.type


## "\n"
