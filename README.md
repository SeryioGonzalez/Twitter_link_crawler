# Twitter summary

This tool will show all links contained in relevant tweets for a given set of keywords<br/>
It works for WSL (Windows Subsystem for Linux) and Chrome Browser.
You need to register a twitter app in order to get an API TOKEN

For using it, edit the cretendials.py file with your information:<br/>
```
$ cat credentials.py
# Consume:
CONSUMER_KEY    = 'XXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'YYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Access:
ACCESS_TOKEN  = 'WWWWWWWWWWWWWWWWWWWWWWWWW'
ACCESS_SECRET = 'ZZZZZZZZZZZZZZZZZZZZZZZZ'

MYSELF = 'YOUR_TWITTER_USER'
```
Edit your favorite hashtags to follow:
```
$ cat keywords.py
keywords = ['nfv', 'iot', 'azure', 'telco' , '5g', 'edgecomputing' ]
```

#Install required modules and enjoy
```
$ sudo apt install -y python3-pip
$ pip3 install tweepy
$ python3 twitter_top_links_for_keywords.py 
```

