import base64
import requests


def initConnect():

    teamcityaddr = input("enter your Team City URL: ")
    teamcityaddr = str(teamcityaddr + ":8111/app/rest/server")
    print("Your TeamCity server address is: " + teamcityaddr)
    return teamcityaddr


def main():
    print(initConnect())



# if __name__ == '__main_':
#         initConnect()

# headers = {
#     'Content-Type': 'text/plain',
#     'Authorization': 'Basic %s' % base64.b64encode('%s:%s' % (
#             'eyJ0eXAiOiAiVENWMiJ9.cGNiQ0JqSmVLMHhqNzBjaTZNOUhEMHlBWDRZ.MGRjNmJjYmMtZGE2OC00NDgwLThlMWEtMDMyZjEyZjYyYTAw',
#             'sp',
#         ),
#     ),
# }



 curl -u russlekelly:asmodeus13 \
      -X POST \
      -d 'test-project1' \
      -H 'Content-Type: text/plain' \
      http://teamcity:8111/httpAuth/app/rest/projects/
# response = requests.request("GET", url, headers=headers)
#
# print (teamCityaddr)

# def createProject(name):
#     name = input("Enter your project name: ")
#     teamCityaddr = teamCityaddr +
#
#
# def createVCS(link):
#     link = input("Enter you VCS link here ")