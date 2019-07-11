from urllib import request,parse
import sys

myUrl = "http://www.google.com/search?"
val = {'q': 'Andesa soft'}


myheader = {}
myheader['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"




try:

    mydata = parse.urlencode(val)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)

except Exception:
    print("Error occured during web request")
    print(sys.exc_info()[1])




# myUrl = "http://teamcity:8111/app/rest/server"


#
# print(mytest1)
#
# xml = """<?xml version='1.0' encoding='utf-8'?>
# <a></a>"""
# headers = {'Content-Type': 'application/xml'} # set what your server accepts
# print requests.post('http://httpbin.org/post', data=xml, headers=headers).text
#
#
#
# POST Request
#
# curl -v -u USER:PASSWORD http://teamcity:8111/app/rest/projects
# --header "Content-Type: application/xml" --data-binary
# "<newProjectDescription name='EnterProjectName' id='enterProjectID'><parentProject locator='id:project1'/></newProjectDescription>"
# curl -v -u USER:PASSWORD
# http://teamcity:8111/app/rest/vcs-roots
# "<vcsRootLocator>"
# <vcs-root id="SetID" name="auto-generated-1" vcsName="jetbrains.git">
# <property name="branch" value="master"/>





# def authorization:
# curl --header "Authorization: Bearer tokenValue" http://teamcity:8111/app/rest/builds
#
#
