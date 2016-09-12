#! /usr/bin/python
print "X-COMP-490: bah16519"
print "Content-type: text/html"
print

import cgitb,cgi,urllib,urllib2,os

cgitb.enable()
form = cgi.FieldStorage()
# parse the query string (acquired by an os system call) into pairs 
pairs = cgi.parse_qs(os.environ["QUERY_STRING"])

#parse the first and last name directly from QUERY_STRING pairs
first_name = pairs["first_name"][0]
last_name = pairs["last_name"][0]

print '<link rel="stylesheet" type ="text/css" href = "../style/mystyle.css">'
print "<h1>Hello %s %s! I searched you on twitter and found this: <h1>" % (first_name, last_name)
print "<br/>"


query_args = {'q':'%s %s' % (first_name, last_name)}
encoded_args = urllib.urlencode(query_args)

request = urllib2.Request('https://twitter.com/search?' + encoded_args + '&src=typd')
response = urllib2.urlopen(request) 

