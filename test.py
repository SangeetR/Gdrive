from auth import *

service = gauth()
link = "https://drive.google.com/file/d/15cbMtktnfl82PZjl0jVtUqTOoXU_MTZk/view?usp=sharing"
id = get_id(link)

#Get and print
req = service.files().get(fileId = str(id), fields = 'name, size, md5Checksum' ).execute()
print("Name: ",req['name'])
print("Hash: ", req['md5Checksum'])
f = open(os.path.join('Download', req['name']), 'ab')
# print("File Size: ",int(req['size'])/1024,"KB")
print("File Size: ",req['size'],"B")
request = service.files().get_media(fileId=id)

done = False
while done is False:
    #Real Downloading STarts here
    start = os.path.getsize(os.path.join('Download', req['name']))
    print("download Start at: ", start)
    # start = 0
    end   = start+1024*1024*2
    if end > int(req['size']):
        end = req['size']
        done = True
        break
    request.headers['Range'] = "bytes="+str(start)+"-"+str(end)

    print("downloading")
    f.write(request.execute())
    print("passed Range")
f.close()
Print("Downloaded")
