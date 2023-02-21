import requests

url = 'https://example.com/file.zip'  # change to your file name / API
filename = 'file.zip' # change to your file name

headers = {'User-Agent': 'P2C CRYPTO'}

verify = True

response = requests.get(url, headers=headers, verify=verify)

if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
else:
    print('Error: ' + str(response.status_code))
