"""
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
"""

# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         [print('-> {} > {}'.format(*attr)) for attr in attrs]
#
# html = '\n'.join([input() for _ in range(int(input()))])
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()




# html=[]
# html.append("<head>")
# html.append("<title>HTML</title>")
# html.append("</head>")
# html.append("<object type=\"application/x-flash\"")
# html.append("data=\"your-file.swf\"")
# html.append("width=\"0\" height=\"0\">")
# html.append("<!-- <param name=\"movie\" value=\"your-file.swf\" /> -->")
# html.append("<param name=\"quality\" value=\"high\"/>")
# html.append("</object>")
# for x in html:
#     if not x.__contains__("<!--"):
#         ls=list(map(str,x.split()))
#         for y in ls:
#             o=y.replace("<","").replace(">","")
#             if y.__contains__("<") and not y.__contains__("</"):
#                 print(o)
#             if "</" not in y and  "/>" not in y:
#                 if(o.__contains__("=")):
#                     print("->"+" > ".join(o.replace("\"","").split("=")))


import re

text = ''
for _ in range(int(input())):
    text = re.sub(r'<!.+-->',r' ',(text+input()))

# html=[]
# html.append("<head>")
# html.append("<title>HTML</title>")
# html.append("</head>")
# html.append("<object type=\"application/x-flash\"")
# html.append("data=\"your-file.swf\"")
# html.append("width=\"0\" height=\"0\">")
# html.append("<!-- <param name=\"movie\" value=\"your-file.swf\" /> -->")
# html.append("<param name=\"quality\" value=\"high\"/>")
# html.append("</object>")
# for x in html:
#     text = re.sub(r'<!.+-->',r' ',(text+x))

# print(text)
for er in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in er:
        for ere in re.findall(r'([a-z]+)? *([a-z-]+)="([^"]+)', er):
            if ere[0]:
                print(ere[0])
            print('-> '+ere[1]+' > '+ere[2])
    else:
        print(er)

