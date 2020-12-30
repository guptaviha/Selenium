import requests
import json
response = requests.get("https://rink.wintervillage.org/include/widgets/events/performancelist.asp?fromDate=&toDate=&venue=0&city=&swEvent=34&category=0&searchString=&searchType=0&showHidden=1&showPackages=0&action=perf&listPageSize=300&listMaxSize=0&page=1")
#print(response.content)


response_dict = json.loads(response.text)

for i in response_dict:
    print("key: ", i, "val: ", response_dict[i])