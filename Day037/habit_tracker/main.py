import requests
from datetime import datetime 
import os 

#STEP 1:Creating user account
PIXELA_ENDPOINT="https://pixe.la/v1/users"
TOKEN=os.environ.get('PIXELA_TOKEN')
USERNAME=os.environ.get('PIXELA_USERNAME')

user_parameter={
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=PIXELA_ENDPOINT,json=user_parameter)
# print(response.text)

#STEP 2:Creating graph definition
GRAPH_ENDPOINT=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
ID="graph1"
graph_config={
    "id":ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=GRAPH_ENDPOINT,json=graph_config,headers=headers)
# print(response.text)

#STEP 3:Get the graph Browse https://pixe.la/v1/users/a-know/graphs/test-graph 

#STEP 4:Add pixel to Habit tracker using Post request with date 24/07/2021 in the YYYYMMDD format that pixela API requires and km cycled.

ADD_PIXEL_ENDPOINT=f"{GRAPH_ENDPOINT}/{ID}"
DATE="20210724"
pixel_config={
    "date":DATE,
    "quantity":"9.6"
}
# response=requests.post(url=ADD_PIXEL_ENDPOINT,json=pixel_config,headers=headers)
# print(response.text)

#STEP 5:Browse https://pixe.la/v1/users/a-know/graphs/test-graph, again!

#STEP 6:You can get more information by adding .html to the end of the URL on Step.6 at it in your browser!
# (https://pixe.la/v1/users/a-know/graphs/test-graph.html)


# STEP 7:Lets add a pixel to the Habit tracker for today's date 26/07/21.Normally we would import datetime and would
#need to modify the format according to the date time format that any API needs.But python has a useful
#strftime() method that formats date objects into the format we need. 

today=datetime.now()
# today=datetime(year=2021,month=7,day=26)

today_pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"6.1",
}
# response=requests.post(url=ADD_PIXEL_ENDPOINT,json=today_pixel_config,headers=headers)
# print(response.text)

# STEP 8:Update the pixel on 24/07/2021 and change the value to 2.We will use PUT request.

UPDATE_PIXEL_ENDPOINT=f"{ADD_PIXEL_ENDPOINT}/{DATE}"
update_config={
    "quantity":"2",
}
# response=requests.put(url=UPDATE_PIXEL_ENDPOINT,json=update_config,headers=headers)
# print(response.text)

#Step 9:Delete the pixel on 24/07/2021.We will put DELETE request
DELETE_PIXEL_ENDPOINT=UPDATE_PIXEL_ENDPOINT
response=requests.delete(url=DELETE_PIXEL_ENDPOINT,headers=headers)
print(response.text)
