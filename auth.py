from __future__ import print_function
import pickle
import os.path
import io
import pyperclip
import time
import re
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

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
    # If there are no (valid) credentials available, let the user log in
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
    req = service.files().get(fileId = str(id), fields = 'name, size, md5Checksum' ).execute()
    print("Name: ",req['name'])
    print("Hash: ", req['md5Checksum'])
    print("File Size: ",(int(req['size'])/1024)/1024,"MB")
    f = open(os.path.join('Download', req['name']), 'ab')
    request = service.files().get_media(fileId=id)
    start = os.path.getsize(os.path.join('Download',req['name']))
    # createPart(8)
    last_detail = {"Name": req['name'],"id": str(id), "hash": req['md5Checksum']}
    lf = open(os.path.join('Download','last_file.json'),'w')
    json.dump(last_detail, lf, indent= 6)
    lf.close()
    if start == int(req['size']):
        print("File has downloaded already")
        return

    done = False
    while done is False:
        end = start+1024*1024*int(chunk_size)
        #careful about range, start and end if there is overlap there will be a glitch 
        if end >= int(req['size']):
            end = int(req['size'])
            done = True
            if end == start:
                break
        request.headers['Range'] = "bytes="+str(start)+"-"+str(end)
        start_time = time.time()
        f.write(request.execute())
        start = end+1
        download_status = "Download: {:.2f}%".format((int(end)/int(req['size']))*100)
        speed_status = "Speed: {:.2f}KBPS".format(2048/(time.time()-start_time)) 
        print(download_status,"\t", speed_status, '\t', end = '\r')
        
    f.close()
    print("Downloaded\n")

def get_id(expr = pyperclip.paste()):
    """
    This Function check whether link supported or not 
    
    #TODO clipboard support  --done
    #TODO LINK SUPPORT TRY today folder support will come 

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