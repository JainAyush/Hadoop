import time
from twython import Twython, TwythonError
twitter = Twython('PVRb7LmKFwBctrLKvULQTnSqi', access_token='AAAAAAAAAAAAAAAAAAAAAPaPWwAAAAAAkiazdF9EzC%2FtcilOFW0S7kYxh94%3DtI84ctlH9V3fZ4Cia3BX0jUmUWkQp2ERtTFfajoFherjwMJJrl')
#ids1 = twitter.get_followers_ids(id = "217189228")
#print ids1['ids']

for line in open("followee_1541474484"):
	listid = line.split(", ")
num_attempt=0
for a in listid:
	try:
		num_attempt+=1;
		if num_attempt>250:
			print "sleep"
			time.sleep(15*60)
			num_attempt=0
		user_timeline=twitter.get_user_timeline(user_id=a, count=200)
		if len(user_timeline)!=0:
			target = open(a,'w')
			for tweet in user_timeline:
				if tweet['lang']=='en':
					target.write(tweet['text'].encode('utf-8')+'\n')
		else:
			print "hi"
	except TwythonError as e:
		print e

# try:
# 	user_timeline=twitter.get_user_timeline(user_id='769965798', count=200)
# 	if len(user_timeline)!=0:
# 		print "hi"
# 		target = open('769965798','w')
# 		for tweet in user_timeline:
# 			if tweet['lang'] == 'en':
# 				target.write(tweet['text'].encode('utf-8')+'\n')
# except TwythonError as e:
# 	print e