import csv
import requests

def is_reachable(url):
    try:
        response = requests.get(url.replace(' ', '%20'))
        return response.status_code == 200
    except (requests.exceptions.InvalidURL, requests.exceptions.MissingSchema):
        return False

with open('subdomains.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        url = row[0]
        if url != '':
            if is_reachable(url):
                print(f'{url} is reachable')
