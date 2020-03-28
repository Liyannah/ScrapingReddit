# coding: utf-8

import praw
import json

reddit = praw.Reddit(client_id = "9ZPnoeKPkoLnkQ", client_secret = "iAZgqpDqQr8eimDAHnCuLQPB9tY", user_agent="ScrapReddit")
posts = {"title": {}, "id":{}, "url": {}}
i = 0

sub_reddit = reddit.subreddit('EarthPorn')

for post in sub_reddit.hot(limit=10):
    posts["title"][i] = post.title
    posts["id"][i] = post.id
    posts["url"][i] = post.url
    i += 1
    
final_file = json.dumps(posts, indent = 2)
f = open("scraping.json","w")
f.write(final_file)
f.close()