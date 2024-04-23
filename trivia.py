import requests as rq

response = rq.get("https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=boolean")
#print(response.json()["results"][0])

print(response.json())


   

# currentQuestion = response.json()["results"][i]["question"]

# print(currentQuestion)

# for question in response.json()["results"]:
        #print(question["question"])