import os
import glob
import pandas as pd

from google.cloud import storage
from google.cloud import bigquery

def csvtobq(event, context):
    filelist = glob.glob('/tmp/*')
    print(filelist)
    
    for filename in filelist:
        try:
            os.remove(filename)
        except:
            print("Error while deleting file : ", filename)

    client = storage.Client()
    source_file_bucket = event['bucket']
    source_path = event['name']

    dest_bucket_name = 'ngatest2'

    # initialize source bucket
    bucket = client.bucket(source_file_bucket)
    print('function triggered')

    # initialize blob object from bucket
    blob = bucket.blob(source_path)
    dest_list = source_path.split('/')

    temp_path = "/tmp/{file_name}".format(file_name = dest_list[-1])
    print('download blob start')

    with open(temp_path, "wb") as file_obj:
        blob.download_to_file(file_obj)
    print('download blob end')
    print(source_path)

    dest_bucket = client.bucket(dest_bucket_name)


    data = pd.read_csv(temp_path)

    print(data.head(5))

    data_dict = data.to_dict(orient='records')

    json_path, extension = os.path.splitext(temp_path)  
    json_file = '{path}.json'.format(path = json_path)
    print(json_file)

    with open(json_file, "w+") as f:
        json.dump(data.to_json(), f, indent=4)

    # dest_path, dest_extension = os.path.splitext(source_path)  
    # dest_file = '{dpath}.json'.format(dpath = dest_path)
    # print(dest_file)

    # blob = dest_bucket.blob(dest_file)

    # blob.upload_from_filename(json_file)
    # os.remove(temp_path)
    # os.remove(json_file)
