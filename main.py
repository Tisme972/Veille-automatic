import requests
import json
from datetime import datetime
import os
from datetime import datetime
import ujson
import time


def sleep_1_day():
    # Sleep for 24 hours (86400 seconds)
    time.sleep(86400)

def run(webhook):
  date_today = datetime.today().strftime('%Y-%m-%d')



  url = "https://networkingsupport.hpe.com/graphql/?FileIndexList"
  headers = {
      "Host": "networkingsupport.hpe.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
      "Accept": "*/*",
      "Accept-Language": "en-US",
      "Accept-Encoding": "",
      "Referer": "https://networkingsupport.hpe.com/downloads;search=6000;fileTypes=SOFTWARE;softwareGroups=AOS-CX",
      "Content-Type": "application/json",
      #"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InByaW1hcnlBY2NvdW50Ijp7ImlkIjoiUVdOamIzVnVkRG80WkdGaE1XVTNNaTFsWVdZMkxURXhaV1l0WVRVNVppMHpaakEwT0RNek1UUXlZMkU9IiwiZGlzcGxheU5hbWUiOiJ4eHhsZXRyaXh4eHgiLCJhY3RpdmUiOnRydWUsInZhbGlkYXRlZCI6ZmFsc2UsImlzR2xvYmFsVHJhZGVDb21wbGlhbnQiOnRydWV9LCJpc0VudGl0bGVkIjpmYWxzZSwiaXNDb3BFbmFibGVkIjpmYWxzZSwiaWQiOiJWWE5sY2pvMU9ESTJaR05qTWkxbFlXWTJMVEV4WldZdFlqWTBNeTA0WWpFNU9XWmlNVFl3TURFPSIsIm5hbWUiOiJsaXlhZGU4Nzk5QGludGFkeS5jb20iLCJmaXJzdE5hbWUiOiJEYW1pZW4iLCJsYXN0TmFtZSI6IkR1cGFydCIsImhhbmRsZSI6ImxpeWFkZTg3OTkiLCJ2ZXJpZmllZCI6dHJ1ZSwiYWN0aXZlIjp0cnVlLCJjb3VudHJ5Q29kZSI6IlRGIiwiaHBlVXVpZCI6IjAwdTFoN2RjMHM3d2s2dWNZMzU4IiwidHlwZSI6IkNVU1RPTUVSIn0sImlhdCI6MTczOTU1NDEyNSwiZXhwIjoxNzM5NTU0MTQ1fQ.ASmwDegFui7VUBJDMbqJTghr5EiaM0xozdKWNwwEiWA",
      #"X-Refresh-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI1ODI2ZGNjMi1lYWY2LTExZWYtYjY0My04YjE5OWZiMTYwMDEiLCJpYXQiOjE3Mzk1NTQxMjUsImV4cCI6MTc0MDE1ODkyNX0.WyclojdFyM3cWAHB6l1L5EymoeiVzl4XW27QBg5bxNQ",
      "Origin": "https://networkingsupport.hpe.com",
      "Dnt": "1",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Priority": "u=4",
      "Te": "trailers"
  }


  payload = {
      "operationName": "FileIndexList",
      "variables": {
          "fileFilterBy": {
              "active": True,
              "visible": True,
              "releaseDate_lte": date_today+"T16:28:45.813Z",
              "fileTypes": ["SOFTWARE"],
              "products": [],
              "productSeries": [],
              "softwareGroups": ["AOS-CX"],
              "softwareMajorVersions": [],
              "softwareMajorVersionReleaseTypes": [],
              "softwarePatchVersions": [],
              "softwareReleaseTypes": [],
              "fileContents": []
          },
          "fileOrderBy": ["RELEVANCE", "RELEASEDATE_DESC"],
          "fileAfter": "YXJyYXljb25uZWN0aW9uOi0x",
          "fileFirst": 20,
          "fileSearch": "6000"
      },
      "query": """
      query FileIndexList($fileAfter: String, $fileFirst: Int, $fileFilterBy: FileIndexFilterByInput, $fileOrderBy: [FileIndexOrderBy!], $fileSearch: String, $fileAggregations: FileIndexAggregationsInput) {
        entities: fileIndexes(
          after: $fileAfter
          first: $fileFirst
          filterBy: $fileFilterBy
          orderBy: $fileOrderBy
          search: $fileSearch
          aggregations: $fileAggregations
        ) {
          edges {
            node {
              ...FileIndexBase
              _score
              _highlights
              _explanation
              __typename
            }
            __typename
          }
          totalCount
          took
          aggregations
          __typename
        }
      }

      fragment FileIndexBase on FileIndex {
        id
        name
        fileName
        mimeType
        active
        size
        documentUrl
        type
        fileContent
        softwareReleaseType
        softwareMajorVersions
        softwareMajorVersionReleaseTypes
        softwarePatchVersion
        products
        productSeries
        softwareGroups
        requiresTracking
        requiresEntitlement
        requiresDeviceRegistration
        releaseDate
        releaseStatus
        requiresCop
        __typename
      }
      """
  }

  if os.path.exists('old_output.txt') and os.path.exists('new_output.txt'):
    os.remove('new_output.txt')
  with open('new_output.txt', 'w') as f:
    pass 
  with requests.post(url, headers=headers, data=json.dumps(payload)) as response:  # Enable streaming mode
      for chunk in response.iter_content(chunk_size=1000000024):  # Process chunks of 1 KB
          with open('new_output.txt', 'ab') as f:
              f.write(chunk + "\n".encode('utf-8'))
          #print(chunk.decode('utf-8'))




  with open('new_output.txt', 'r') as f:
      data1 = ujson.load(f)

  with open('old_output.txt', 'r') as y:
      data2 = ujson.load(y)
      
  if data1['data']['entities']['edges'][0]['node']['name'] == data2['data']['entities']['edges'][0]['node']['name']:
      print("No new data")
      
         

      

  else:
    print("New data found")

    data1_list = []
    data2_list = []
    new_data_list = []
    for i in range(20):
      data1_list.append(data1['data']['entities']['edges'][i]['node']['name'])
      data2_list.append(data2['data']['entities']['edges'][i]['node']['name'])
    for i in range(20):
      value = data1_list[i]
      if value not in data2_list:
         print("New data found")
         print(value)
         new_data_list.append(value)



    json_data = {
      "embeds": [
      {
      "title": "New firmware found",
      "description": "\n".join(new_data_list),
      "fields": [
        {
          "name": "Last versions",
          "value": "\n".join(
            [edge['node']['name'] for edge in data1['data']['entities']['edges'][len(new_data_list):20]]
          )
        }
      ],
      "color": 0x00ff00
      }
      ]
    }
    headers = {"Content-Type": "application/json"}
    requests.post(webhook, headers=headers, json=json_data)
    os.replace('new_output.txt', 'old_output.txt')
         

  sleep_1_day()

while True:
    webhook = "https://discord.com/api/webhooks/1364300507249774622/sQwomrCtUiKUb_oyoarzOOQEqO8anYj8S2qt3L7piRecJ5oDUxgNNhPbEWoLZmOjCf0i"
    try:
      run(webhook)
    except Exception as e:
      print("error:",str(e))
      headers = {"Content-Type": "application/json"}
      json_data = {
          "embeds": [
          {
          "title": "Error",
          "description": str(e),
          "color": 0xff0000
          }
          ]
      }
      requests.post(webhook, headers=headers, json=json_data)
