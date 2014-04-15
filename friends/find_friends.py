# from __future__ import print_function
from twython import Twython, TwythonError
twitter = Twython('PVRb7LmKFwBctrLKvULQTnSqi', access_token='AAAAAAAAAAAAAAAAAAAAAPaPWwAAAAAAkiazdF9EzC%2FtcilOFW0S7kYxh94%3DtI84ctlH9V3fZ4Cia3BX0jUmUWkQp2ERtTFfajoFherjwMJJrl')
for line in open("217189228_follows"):
	listid = line.split(", ")
# print listid
num_attempt=0
for a in listid:
	try:
		num_attempt+=1;
		if num_attempt>=14:
			print "sleep"
			time.sleep(15*60)
			num_attempt=0
		ids1 = twitter.get_friends_ids(id = a)
		target = open(a+"_follows",'w')
		for id in ids1['ids']:
			target.write(str(id)+', ')
			# target.write('\n')
	except TwythonError as e:
		print e

# print(ids1['ids'],file = target)
# print ids1['ids']
# for line in open("followee_217189228"):
# 	listid = line.split(", ")
# for a in listid:
# 	user_timeline=twitter.get_user_timeline(user_id=a, count=200)
# 	target = open(a,'a')
# 	for tweet in user_timeline:
# 		target.write(tweet['text'].encode('utf-8')+'\n')
# user_timeline=twitter.get_user_timeline(user_id='1541474484', count=200)
# target = open('1541474484','a')
# for tweet in user_timeline:
# 	target.write(tweet['text'].encode('utf-8')+'\n')