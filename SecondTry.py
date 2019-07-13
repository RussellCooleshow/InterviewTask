import requests

# So I want to make a basic commandline script which allows us to do the following in Teamcity:
# 1. setup VCS root
# 2. Configure VCS root
# 3. create project
# 4. add dependencies for this project (for example snapshot dependency)



# Authorization part
auth_token = input('Please provide your auth token: ')

def connect():
    hed = {'Authorization': 'Bearer ' + auth_token}
    url = ' http://myteamcityserver.com:8111/app/rest/projects/'
# response = requests.get(url, data=raw_data, headers=hed)
    response = requests.get(url, headers=hed)
    print(response)

# that would be nice to add smth like "Enter your teamcity server address" and then it will be paste in url variable


def createProject():
    url = " http://myteamcityserver.com:8111/app/rest/projects/"
    # hed = {'Authorization': 'Bearer ' + auth_token}
    projectName = input("Please enter project name:")
    hed2 = {'Content-Type': 'text/plain'}
    dat = projectName
    response = requests.post(url, data=dat, headers=hed2)
    if response!=200:
        print("Achtung!")
    else:
        print("Your project " + projectName + " has been created succesfully")
## Here we are requesting project name and then send post request in order to create project
# that would be great to create a check whether such project already exsists or not


if __name__ == '__main__':
    connect()
    createProject()
