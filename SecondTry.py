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
vcsrootname = input("Name your VCS root: ")
vcsid = input("Enter your VCSID: ")


## It was done just for sanity Connection Check on early stages.
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


# The whole Create project thing

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

# Here I built separate function in order to assign build parameter to newly created project

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
        print("Your build parameter has been successfully defined in " + projectname)

# Here we are creating VCS Root with desired name and https://github.com/JetBrains/teamcity-rest-client

def createvcs():
    hed2 = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = " http://{}/app/rest/latest/vcs-roots".format(myurl)
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
        print("Your VCS Root {} has been created successfully and edited here".format(vcsrootname))

    return vcsid, vcsrootname

def definingBuilds():
    hed2 = {'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json',
            'Origin': 'http://{}'.format(myurl),
            'Accept': 'application/json'}
    url = " http://{}/app/rest/buildTypes".format(myurl, projectname)


## Here we are creating build A which has:
# -A has the VCS Root attached, has no build step and publishes “README.md” as an artifact

    buildA = 'buildA.json'
    buildAname = input("Give your build A a name: ")
    with open(buildA, 'r') as f:

#This is a block is repeats in almost every build and it must be beautified, but for now - it works.
        dataa = json.load(f)
        dataa['id'] = buildAname
        dataa['name'] = buildAname
        dataa['projectName'] = projectname
        dataa['projectId'] = projectname
        dataa['project']['id'] = projectname
        dataa['project']['name'] = projectname
        dataa['project']['href'] = "/app/rest/projects/id:{}".format(projectname)
        dataa['project']['webUrl'] = "http://myteamcityserver.com:8111/project.html?projectId={}".format(projectname)
        dataa['vcs-root-entries']['vcs-root-entry'][0]['id'] = vcsid
        dataa['vcs-root-entries']['vcs-root-entry'][0]['vcs-root']['id'] = vcsid
        dataa['vcs-root-entries']['vcs-root-entry'][0]['vcs-root']['name'] = vcsrootname
        dataa['vcs-root-entries']['vcs-root-entry'][0]['vcs-root']['href'] = "/app/rest/vcs-roots/id:{}".format(vcsid)
        dataa['parameters']['href'] = "/app/rest/buildTypes/id:{}/parameters".format(buildAname)
        dataa['builds']['href'] = "/app/rest/buildTypes/id:{}/builds/".format(buildAname)
        dataa['investigations']['href'] = "/app/rest/investigations?locator=buildType:(id:{})".format(buildAname)
        dataa['compatibleAgents']['href'] = "/app/rest/agents?locator=compatible:(buildType:(id:{}))".format(buildAname)
    response = requests.post(url, json=dataa, headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your Build {} has been created successfully".format(buildAname))


## Here we are creating Build B which:
# -  has a command line step that generates a delay in the chain by using sleep 10
# -  has an agent requirement, where “teamcity.agent.name” equals “Default Agent”

    buildB = 'buildB.json'
    buildBname = input("Give your build B a name: ")

    with open(buildB, 'r') as f:
        datab = json.load(f)
        datab['id'] = buildBname
        datab['name'] = buildBname
        datab['projectName'] = projectname
        datab['projectId'] = projectname
        datab['project']['id'] = projectname
        datab['project']['name'] = projectname
        datab['project']['href'] = "/app/rest/projects/id:{}".format(projectname)
        datab['project']['webUrl'] = "http://myteamcityserver.com:8111/project.html?projectId={}".format(projectname)
        datab['parameters']['href'] = "/app/rest/buildTypes/id:{}/parameters".format(buildBname)
        datab['builds']['href'] = "/app/rest/buildTypes/id:{}/builds/".format(buildBname)
        datab['investigations']['href'] = "/app/rest/investigations?locator=buildType:(id:{})".format(buildBname)
        datab['compatibleAgents']['href'] = "/app/rest/agents?locator=compatible:(buildType:(id:{}))".format(buildBname)

    response = requests.post(url, json=datab, headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your Build {} has been created successfully".format(buildBname))

## Here we are creating Build C which:
# -  has a snapshot dependency on both A and B, and an artifact dependency “from the same chain” on A
# -  has a build trigger on changes in snapshot dependencies on the VCS Root, only on branch “master”


    buildC = 'buildC.json'
    buildCname = input("Give your build C a name: ")

    with open(buildC, 'r') as f:
        datac = json.load(f)
        datac['id'] = buildCname
        datac['name'] = buildCname
        datac['projectName'] = projectname
        datac['projectId'] = projectname
        datac['project']['id'] = projectname
        datac['project']['name'] = projectname
        datac['project']['href'] = "/app/rest/projects/id:{}".format(projectname)
        datac['project']['webUrl'] = "http://myteamcityserver.com:8111/project.html?projectId={}".format(projectname)
        datac['parameters']['href'] = "/app/rest/buildTypes/id:{}/parameters".format(buildCname)
        datac['builds']['href'] = "/app/rest/buildTypes/id:{}/builds/".format(buildCname)
        datac['investigations']['href'] = "/app/rest/investigations?locator=buildType:(id:{})".format(buildCname)
        datac['compatibleAgents']['href'] = "/app/rest/agents?locator=compatible:(buildType:(id:{}))".format(buildCname)

# Above we can see regular definition of a build according to your Project and VCS name setup. Lower - we setup snapshot dependency.
        datac["snapshot-dependencies"]["snapshot-dependency"][0]["id"] = buildAname
        datac["snapshot-dependencies"]["snapshot-dependency"][0]["source-buildType"]['id'] = buildAname
        datac["snapshot-dependencies"]["snapshot-dependency"][0]["source-buildType"]['name'] = buildAname
        datac["snapshot-dependencies"]["snapshot-dependency"][0]["source-buildType"]['projectName'] = projectname
        datac["snapshot-dependencies"]["snapshot-dependency"][0]["source-buildType"]['projectId'] = projectname
        datac["snapshot-dependencies"]["snapshot-dependency"][0]["source-buildType"]['href'] = "/app/rest/buildTypes/id:{}".format(buildAname)
        datac["snapshot-dependencies"]["snapshot-dependency"][1]["id"] = buildBname
        datac["snapshot-dependencies"]["snapshot-dependency"][1]["source-buildType"]['id'] = buildBname
        datac["snapshot-dependencies"]["snapshot-dependency"][1]["source-buildType"]['name'] = buildBname
        datac["snapshot-dependencies"]["snapshot-dependency"][1]["source-buildType"]['projectName'] = projectname
        datac["snapshot-dependencies"]["snapshot-dependency"][1]["source-buildType"]['projectId'] = projectname
        datac["snapshot-dependencies"]["snapshot-dependency"][1]["source-buildType"]['href'] = "/app/rest/buildTypes/id:{}".format(buildAname)

    response = requests.post(url, json=datac, headers=hed2)
    if response.status_code != 200:
        print("Achtung!")
    else:
        print("Your Build {} has been created successfully".format(buildCname))

if __name__ == '__main__':
    connect()
    createProject()
    buildparameter()
    createvcs()
    definingBuilds()
