import requests
import pyperclip


url = 'http://dl163.y2mate.com/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyZ1V1ZnNRNGpJQ0wrQUg0OTRPbk5lb0t0OUZJYk5FaU5qMFd2bEI1ekxkYTV1cU93ZWR0NHB0QnlTaXZPSTF2SFR0L0owekVvd21kVjNXbnZIb3BpUjRnd2IzZDVQK0dyWlJKaVVyOFJBb2xuR3doOTNWclJEcnB6YWRza09KYlNZRCtRZ0VNL0xEdXMwWWh6bjBQcWU4ZzRCTG9EYkxwSnhBMXZXaXBBRGl5Kzk3NnZwc1VWRmdacEpZbk1qVDB1Q1k0QlUvMDl4Ty9GVDJwT095QTlBMkU2alZOSHhnUHl3RDdPM3VVaVFOeHl3SThtT3F5YWd3L0d3TWE1OTA0MnFnK09EV2NqZWRRY0Q1WElLN0pPMnFtZFhzN1BOZ3ZVait0ZXpKbTZVU3hscjNkOFQrVXRRYnBYQXp0SzJKNU00Ly9VVzIxQWdKdmJKWmxodkRja2R0R2NkRE5TVUVOUGtvVm41QSs5MnM1TFpvdTVwVWZrWHg1cWc0ZXY5Zy9NaWJrK05QazMzVnBKa3BPUmJBdkNUZEN0eXNERElvOUNWRkJ5dkRSQT09'

r = requests.head(url)
leng =int(r.headers['content-length'])
print(r.headers)
f = open('panjeban.mp4','ab')
start = 0   
done = False
while done is False:
    end = start + 512*1024
    if end > leng:
        if end == leng:
            print("Completed")
            done = True
            break
        end = leng   
        done = True
    print("start:",start,"-",end)
    head = {"Range": "bytes={}-{}".format(start, end)}
    f.write(requests.get(url, headers=head).content)
    print("Downloaded: ",end/leng*100,'\t')
    start = end+1

f.close()
# 53f4b47352be492e8e2836a273492567
# 'Content-Length': '55095924'