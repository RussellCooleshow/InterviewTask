import requests
import json



## So my goal for now was to:
# 1. To ask for a project name
# # 2. to ask for vcs id and name in order to create it
# # 3. defines the “project.branch.spec” build parameter with the value “+:refs/heads/*”
# # # ALL THAT HAS BEEN ACHIEVED
# TO DO LIST IS:

#


# Authorization part
auth_token = input('Please provide your auth token: ')
myurl = input('Please provide your TeamCity Server address and port: ')
projectname = input("Name your project: ")

def connect():
    auth = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'xml/application',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = ('http://{}/app/rest/latest/projects'.format(myurl))
    print(url)
    print(auth)
    response = requests.get(url=url, headers=auth)
    print(response)



def createProject():
    hed2 = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = " http://{}/app/rest/latest/projects".format(myurl)
    filename = 'createproject.json'
    # Here we are opening .json file and then setup id and project name as per your desire
    with open(filename, 'r') as f:
        data = json.load(f)
        data['id'] = str(projectname)
        data['name'] = str(projectname)
    response = requests.post(url, data=json.dumps(data), headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your project " + projectname + " has been created successfully")
# Here we are requesting project name and then send post request in order to create project
# that would be great to create a check whether such project already exists or not
    print(response)
    return projectname

#here I built separate function in order to assign build parameter to newly created project
def buildparameter():
    hed2 = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = ('http://{}/app/rest/latest/projects/{}/parameters'.format(myurl, projectname))
    buildparam = open('buildparameter.json', 'rb').read()
    response = requests.post(url, data=buildparam, headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your build parameter has been succesfully defined in " + projectname)





def createvcs():
    hed2 = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = " http://{}/app/rest/latest/vcs-roots".format(myurl)
    vcsrootname = input("Name your VCS root: ")
    vcsid = input("Enter your VCSID: ")
    filename = 'vcsroot.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        #Setting up the ID and Name of VCS
        data['id'] = str(vcsid)
        data['name'] = str(vcsrootname)
        # Referring it to our newly created project
        data['project']['id'] = projectname
        data['project']['name'] = projectname
    response = requests.post(url, json=data, headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your VCS Root {} has been created succesfully".format(vcsrootname))


if __name__ == '__main__':
    connect()
    createProject()
    buildparameter()
    createvcs()
