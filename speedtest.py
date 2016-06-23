#!/usr/bin/env python
import json
import subprocess
import requests

cmd = ["speedtest"]

output = subprocess.check_output(cmd)

speed_output = str(output).split('\\n')

upload = [s for s in speed_output if 'Upload' in s][0]
download = [s for s in speed_output if 'Download' in s][0]

print(upload)
print(download)

upload_speed = upload.split(' ')[1]
download_speed = download.split(' ')[1]

#upload_f = float(upload_speed)
#download_f = float(download_speed)

#print(upload_f < 17)
#print(download_f < 50)

#if upload_f < 17:
  ## POST UPLOAD TOO SLOW
#  pass
#if download_f < 50:
#  pass

r = requests.post(
    "https://hooks.slack.com/services/T02AQEVPE/",
    json.dumps({
        "channel": "#",
        "username": "speedtester",
        "text": str(output),
        "icon_emoji": ":ghost:"
    }), headers={'Content-type':'application/json'})
print(r.text)
