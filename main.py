from auth import *
import hashcalculate
import pyperclip

def main():
    service = gauth()
    id = get_id(pyperclip.paste())
    last_file = open("Download/last_file.json",'r')
    last_detail = json.load(last_file)
    last_file.close()
    if id is None:
        print("You want to resume your last download if not completed")
        print("Your last download was: '", last_detail['Name'],"'")
        print("Enter y/n")
        ans = input()
        if ans == 'y':
            dwnld(service, last_detail['id'])
            last_file = open("Download/last_file.json",'r')
            last_detail = json.load(last_file)
            last_file.close()
            hashcalculate.calhash("Download/"+str(last_detail['Name']), str(last_detail['hash']))
        else :
            print("Sayonara")
    else:
        dwnld(service, id)
        last_file = open("Download/last_file.json",'r')
        last_detail = json.load(last_file)
        last_file.close()
        hashcalculate.calhash("Download/"+str(last_detail['Name']), str(last_detail['hash']))

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(Exception)