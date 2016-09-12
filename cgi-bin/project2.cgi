#! /usr/bin/python
print "X-COMP-490: bah16519"
print "Content-type: text/html"
print

import cgitb,cgi,urllib,urllib2,os

# parse the query string (acquired by an os system call) into pairs 
pairs = cgi.parse_qs(os.environ["QUERY_STRING"])

#parse the first and last name directly from QUERY_STRING pairs
first_name = pairs["first_name"][0]
last_name = pairs["last_name"][0]

query_args = {'q':'%s %s' % (first_name, last_name)}
encoded_args = urllib.urlencode(query_args)

request = urllib2.Request('https://twitter.com/search?' + encoded_args + '&src=typd')
response = urllib2.urlopen(request) 
print '<script src = "../style/mystyle.css"></style>'



# for line in response:
# 	print line.rstrip()

print ("Hello %s %s! I searched you on twitter and found this: " % (first_name, last_name))  
print response.read()