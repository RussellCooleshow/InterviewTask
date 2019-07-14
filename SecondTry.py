import requests


# So I want to make a basic commandline script which allows us to do the following in Teamcity:
# 1. setup VCS root
# 2. Configure VCS root
# 3. create project
# 4. add dependencies for this project (for example snapshot dependency)

eyJ0eXAiOiAiVENWMiJ9.cGNiQ0JqSmVLMHhqNzBjaTZNOUhEMHlBWDRZ.MGRjNmJjYmMtZGE2OC00NDgwLThlMWEtMDMyZjEyZjYyYTAw

# Authorization part
auth_token = input('Please provide your auth token: ')
myurl = input('Please provide your TeamCity Server address and port: ')


def connect():
    auth = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'xml/application',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    # hed = {'Authorization': 'Bearer ' + auth_token}
    url = ('http://{}/app/rest/latest/projects'.format(myurl))
# response = requests.get(url, data=raw_data, headers=hed)
#     response = requests.get(url, headers=hed)
#     session.verify = False
    print(url)
    print(auth)
    response = requests.get(url=url, headers=auth)
    print(response)



def createProject():
    hed2 = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/xml',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = " http://{}/app/rest/latest/projects".format(myurl)
    projectname = input("Name your project: ")
    dat = "<newProjectDescription name='{}'></newProjectDescription>".format(projectname)
    # "<newProjectDescription name='test3Consoleeee' ></newProjectDescription>"
    response = requests.post(url, data=dat, headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your project " + projectname + " has been created successfully")
# Here we are requesting project name and then send post request in order to create project
# that would be great to create a check whether such project already exsists or not
    print(response)




if __name__ == '__main__':
    connect()
    createProject()
