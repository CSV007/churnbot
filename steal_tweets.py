import twitter
import keys
import json

# in a file called keys.py, input all these keys and things
api = twitter.Api(consumer_key=keys.consumer_key,
                  consumer_secret=keys.consumer_secret,
                  access_token_key=keys.access_token,
                  access_token_secret=keys.access_token_secret)

# verify your twitter credentials
# print api.VerifyCredentials()

"""Pulls tweets from @shitbethsaid"""
statuses = api.GetUserTimeline(screen_name="shitbethsaid")
shit_beth_said_list = []
for status in statuses:
    shit_beth_said_list.append(status.text)

shit_beth_said_json = json.dumps(shit_beth_said_list)

print shit_beth_said_json