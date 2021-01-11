import pyyoutube  #run cmd as admin while instaling 'pip install --upgrade python-youtube'
from datetime import datetime

d = datetime.now()

print(d.strftime('%Y-%m-%dT{}+{}').format("00:00:00","00:00"))
api = pyyoutube.Api(api_key='AIzaSyBXmobEX1fX31VQk55p6YxJ5qQ5Q7fHYDc')

res = api.get_activities_by_channel(channel_id='UCc4Rz_T9Sb1w5rqqo9pL1Og',return_json=True,after=d.strftime('%Y-%m-%dT{}+{}').format("00:00:00","00:00"))
if len(res['items']) != 0:
    print("Last video:::https://www.youtube.com/watch?v={}".format(res['items'][0]['contentDetails']['upload']['videoId']))
else:
    print("No video") #
