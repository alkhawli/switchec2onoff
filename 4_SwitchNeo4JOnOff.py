import requests
import json
import time
import argparse
API_ENDPOINT='https://0lne38t4g3.execute-api.eu-west-1.amazonaws.com/Production1'

def switchMachineOn():
    global API_ENDPOINT
    status=checkStatus()
    timeout=10 #minutes
    i=0
    if (status!='running'):
        data = {
                "httpMethod": "POST",
                "body": "{\"instance_neo4j\": 1}"
            }
        r = requests.post(url = API_ENDPOINT, json=data)
        while (status!='running'):
            time.sleep(60)
            status=checkStatus()
            i=i+1
            if (i>timeout):
                print("Timout Reached, Machine cant be started")
                break
        
        print ("Machine is Now Ready")
    else:
        print("Machine is aleady On")

def switchMachineOff():
    global API_ENDPOINT
    status=checkStatus()
    timeout=10 #minutes
    i=0
    if (status!='stopped'):
        data = {
                "httpMethod": "POST",
                "body": "{\"instance_neo4j\": 0}"
            }
        r = requests.post(url = API_ENDPOINT, json=data)
        while (status!='stopped'):
            time.sleep(60)
            status=checkStatus()
            i=i+1
            if (i>timeout):
                print("Timout Reached, Machine cant be stopped")
                break
        print ("Machine is Now Off")
    else:
        print("Machine is aleady Off")


def checkStatus():
    global API_ENDPOINT
    data = {
            "httpMethod": "GET"
           }
    r = requests.get(url = API_ENDPOINT, json=data)
    output = json.loads(r.text)
    instancesstatus=json.loads(output['body'])['instance_neo4j']
    print("Current Status is: {0}, please wait!".format(instancesstatus))
    return instancesstatus

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--switch', help="--switch either ON or OFF")
    args=parser.parse_args()


    if args.switch=='ON':
        switchMachineOn()
    elif args.switch=="OFF":
        switchMachineOff()
    else:
        print("Invalid parameters, check help!")
    #switchMachineOff()
    