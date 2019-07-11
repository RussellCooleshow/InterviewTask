import requests


auth_token = input('Please provide your auth token: ')

def connect():
    hed = {'Authorization': 'Bearer ' + auth_token}

    url = ' http://myteamcityserver.com:8111/app/rest/projects/'
# response = requests.get(url, data=raw_data, headers=hed)
    response = requests.get(url, headers=hed)
    print(response)



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


if __name__ == '__main__':
    connect()
    createProject()
