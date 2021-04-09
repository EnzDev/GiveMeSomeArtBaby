# Export the generated art to an S3 bucket and a db server


def save_s3(art_data):
    # Use s3cmd to send the file (sensitive data are handled externally)
    import subprocess
    s3cmd = subprocess.run(['s3cmd', 'put', art_data['filename'] + ".jpg", 's3://gmsab/', '-P', '--content-type', 'image/jpeg'])
    return s3cmd.returncode


def save_db(art_data):
    import datetime
    import requests
    import json
    url = open('store.url').readline().replace("\n", "")  # API url is provided via a local token
    payload = dict()
    payload['generated'] = int(datetime.datetime.now().timestamp() * 1000)  # create JS date
    payload['seed'] = art_data['seed']
    payload['size'] = int(art_data['size'])
    payload['url'] = art_data['filename'] + ".jpg"
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.content)

    r.close()
