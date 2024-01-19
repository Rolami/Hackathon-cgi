#!/usr/bin/python3

import requests # Requers you to run "pip install requests"
import json 

baseURL = 'http://16.171.230.96:8080/'
apiKey = 'a66035b6-96c5-4b24-afd6-2a22e2fd25c6'

def fetch_json(url):
    res = requests.get(url)
    if res.status_code == 200:
        response = json.loads(res.text)
        return response
    else:
        print("Faild to fetch game, status code: " + str(res.status_code))

def post_json(url, body):
    Headers = { "Content-type": "application/json; charset=UTF-8","Authorization" : apiKey }
    req = requests.post(url, json = body, headers=Headers)
    return req.text

# def game_solver(game):
    # best_action = {}
    # game_actions = game["actions"]
    # # Sort and use the action that gives biggest multiplyer
    # for action in game_actions:
    #     if best_action == {}:
    #         best_action = action
    #     elif best_action["pointMultiplyer"] < action["pointMultiplyer"]:
    #         best_action = action
    # print("Best action: " + str(best_action))
    
    
    ##Testa en aktivitet

    
    # actionActivityList = []
    # # Uses the best action on so many activities we can without going over the energy limit
    # actionActivityObject = {
    #     "action": best_action["action"],
    #     "activity": game["activitys"][0]["activity"]
    # }
    # actionActivityList.append(actionActivityObject)

    return actionActivityList

def game_solver(game):
    selected_action = game["actions"][0]
    total_energy = game["maxEnergy"]
    activityNumber = 0
    actionActivityList = []
    
    ## BARA SNARES
    while total_energy >= selected_action["energyCost"]:
        # Check if activityNumber is within the valid range
        if activityNumber < len(game["activitys"]):
            action_activity_object = {
                "action": selected_action["action"], 
                "activity": game["activitys"][activityNumber]["activity"]
            }
            actionActivityList.append(action_activity_object)
            total_energy -= selected_action["energyCost"]
            activityNumber += 1
        else:
            break  # Exit the loop if activityNumber is out of range

    return actionActivityList


# Fetch game and print out the Json

game = fetch_json(baseURL + "/game")
print("Game:")
print(game)
print("---------------------------------------------------------------------")

# A solution that just try to take the best action and do as many tasks it can
solution = game_solver(game)

# Create a body, post the solution and print out the score
body = {
    "gameMove": solution
}
print(body)
score = post_json(baseURL + "/game/v2/submit/", body)
print("Your score is: " + score)

def maxScorePoints(activityList):

    maxScore = 0;

    for activity in activityList:
       if maxScore < activity.points:
           maxScore = activity.points
    
    return maxScore
    
    
    