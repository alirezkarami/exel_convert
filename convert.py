# import urllib library
from urllib.request import urlopen

# import json
import json

# import excel

import xlwt


# store the URL in url as
# parameter for urlopen
url = "https://jsonplaceholder.typicode.com/users"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
# print(type(data_json))

# list of city 'Bartholomebury' & 'South Christy'
address = ' '
request_user_of_city = []

for user in data_json:
    address = user['address']
    if address['city'] == 'Bartholomebury':
        request_user_of_city.append(user['name'])

    elif address['city'] == 'South Christy':
        request_user_of_city.append(user['name'])

print(request_user_of_city)


wb = xlwt.Workbook()
sh = wb.add_sheet('my data')

for i in range(len(request_user_of_city)):
    sh.write(i, 0, request_user_of_city[i])
wb.save('names-list.xlsx')
