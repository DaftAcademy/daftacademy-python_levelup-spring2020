import time

import requests


responses = []

urls_f_name = 'urls'
# urls_f_name = 'urls_2'
start = time.time()
with open(urls_f_name, 'r') as f:
    for line in f.readlines():
        print(f'Checking {line}')
        resp = requests.get(line)
        responses.append(resp)
end = time.time()

print(f'elapsed: {end - start} seconds')