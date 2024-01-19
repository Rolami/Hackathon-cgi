#!/usr/bin/python3

import requests # Requers you to run "pip install requests"
import json 

baseURL = 'http://X.X.X.X:XXXX'
apiKey = 'token'

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

def game_solver(game):
    best_action = {}
    game_actions = game["actions"]
    # Sort and use the action that gives biggest multiplyer
    for action in game_actions:
        if best_action == {}:
            best_action = action
        elif best_action["pointMultiplyer"] < action["pointMultiplyer"]:
            best_action = action
    print("Best action: " + str(best_action))

    actionActivityList = []
    # Uses the best action on so many activities we can without going over the energy limit
    actionActivityObject = {
        "action": best_action["action"],
        "activity": game["activitys"][0]["activity"]
    }
    actionActivityList.append(actionActivityObject)

    return actionActivityList
    

# Fetch game and print out the Json

game = fetch_json(baseURL + "/game")
print("Game:")
print(game)
print("----")

# A solution that just try to take the best action and do as many tasks it can
solution = game_solver(game)

# Create a body, post the solution and print out the score
body = {
    "gameMove": solution
}
print(body)
score = post_json(baseURL + "/game/v2/submit/", body)
print(score)
