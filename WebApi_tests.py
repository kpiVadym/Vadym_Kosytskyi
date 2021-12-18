import requests
import json
import re

upload_parameters = {"url" : "https://api.dropboxapi.com/2/files/upload",
                         "payload" : "Some_text",
                         "headers": {
                                  'Dropbox-API-Arg': '{"path": "/File.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
                                  'Content-Type': 'application/octet-stream',
                                  'Authorization': 'Bearer 2VrJ3gDCL3oAAAAAAAAAAf5sZTo0Tx5EcuwzSSHRyJGYxescRRmt_B4b4SukVOQJ'
                                  }}
    
get_metadata_parameters = {"url" : "https://api.dropboxapi.com/2/files/get_metadata",
                         "payload" : json.dumps({
                                          "path": "/File.txt"
                                      }),
                         "headers": {
                                      'Content-Type': 'application/json',
                                      'Authorization': 'Bearer 2VrJ3gDCL3oAAAAAAAAAAf5sZTo0Tx5EcuwzSSHRyJGYxescRRmt_B4b4SukVOQJ'
                                        }}


delete_parameters = {"url" : "https://api.dropboxapi.com/2/files/delete_v2",
                         "payload" : json.dumps({
                                          "path": "/File.txt"
                                        }),
                         "headers": {
                                      'Content-Type': 'application/json',
                                      'Authorization': 'Bearer 2VrJ3gDCL3oAAAAAAAAAAf5sZTo0Tx5EcuwzSSHRyJGYxescRRmt_B4b4SukVOQJ'
                                    }}

    
class DropBoxApp:
    
    def __init__(self, upload_parameters, get_metadata_parameters, delete_parameters  ):
        self.upload_parameters = upload_parameters
        self.get_metadata_parameters = get_metadata_parameters
        self.delete_parameters = delete_parameters 
        
    def get_parameters(self, parameters):
        return parameters["url"], parameters["payload"], parameters["headers"]

    def upload_file(self):
        url, payload, headers = self.get_parameters(self.upload_parameters)
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
    
    def get_metadata_file(self):
        url, payload, headers = self.get_parameters(self.get_metadata_parameters)
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
    
    def delete_file(self):
        url, payload, headers = self.get_parameters(self.delete_parameters)
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
    
    
app1 = DropBoxApp(upload_parameters, get_metadata_parameters, delete_parameters   )


response_upload = app1.upload_file()
if  response_upload.ok:
    print("Uploading is done")
else:
    raise Exception(f"Uploading is not done.\n ERROR:  {response_upload.status_code}")
    
response_get_metadata_file = app1.get_metadata_file()
if  response_upload.ok:
    print("Geting metadata is done")
else:
    raise Exception(f"Geting metadata is not done.\n ERROR:  {response_upload.status_code}")
    

response_delete_file = app1.delete_file()
if  response_upload.ok:
    print("Deleting is done")
else:
    raise Exception(f"Deleting  is not done.\n ERROR:  {response_upload.status_code}")
    




