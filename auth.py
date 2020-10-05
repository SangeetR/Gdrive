from __future__ import print_function
import pickle
import os.path
import io
# import time
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive']

def gauth():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)


def dwnld(service,id,chunk_size = 2):
    ########------------------------------------------###################
    ########------------Clean Up This Code------------###################
    ########------------------------------------------###################
    #TODO add files to download folder "os independent"  --done
    #TODO add print percentage

    
    req = service.files().get(fileId = str(id), fields = 'name, size, md5Checksum' ).execute()
    print("Name: ",req['name'])
    print("Hash: ", req['md5Checksum'])
    print("File Size: ",(int(req['size'])/1024)/1024,"MB")
    f = open(os.path.join('Download', req['name']), 'ab')
    request = service.files().get_media(fileId=id)
    start = os.path.getsize(os.path.join('Download',req['name']))
    # createPart(8)


    done = False
    while done is False:
        end = start+1024*1024*int(chunk_size)
        #careful about range, start and end if there is overlap there will be a glitch 
        if end > int(req['size']):
            end = int(req['size'])
            done = True
            # break  
        request.headers['Range'] = "bytes="+str(start)+"-"+str(end)
        f.write(request.execute())
        start = end+1
        print("Download :", (int(end)/int(req['size']))*100,"%")
    f.close()
    print("Downloaded")

def get_id(expr):
    """
    This Function check whether link supported or not 
    
    #TODO clipboard support
    #TODO LINK SUPPORT TRY

    """

    reg = re.compile(r'https://drive.google.com/file/d/(.*)/')
    otpt = reg.search(expr)
    if otpt != None:
        return otpt.group(1)
    else:
        print("Sorry This link is Not supported yet")

def createPart(number_of_parts):
    for i in range(number_of_parts):
        f = open(os.path.join("Download", "Part"+str(i+1)), 'wb')
        f.close()