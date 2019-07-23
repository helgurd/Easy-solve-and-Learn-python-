import urllib.request
import urllib.parse
import re



url = 'url'
values= {'s':'basics', ' submit':'search'}
data = urllib.parse.urlencode(values)
data=data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData= resp.read()

paragraphs=re.findall(r'<p>(.*)</P>',str(respData))

for eachp in paragraphs:
    print(eachp)





# def read_text():
#     quotes=open('quotes.txt')
#     contents_of_file=quotes.read()
#     print(contents_of_file)
#     quotes.close()
#     check_profanity(contents_of_file)




# def check_profanity(text_to_check):
#     connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check )
#     output =connection.read()
#     print(output)
#     connection.close()
    

    
# print (read_text())