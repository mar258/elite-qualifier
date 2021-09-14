import random

def generate_response(user_input):
  responses = [
    "How interesting!",
    "Thanks for telling me!",
    "Fascinating!",
    "You don't say!"
  ]
  return random.choice(responses)

def joke_response():
  j_responses = [
    "Why did it get so hot in stadium? There were no fans",
    "What did the traffic light say to the other? Stop looking",
    "Why do actors break legs? Because every play has a cast",
  ]
  return random.choice(j_responses)


name = input("Hi! What's your name? ")
day = input("How's your day going " + name + "? ")
print(generate_response(day)+ "\n")


while(True):
  joke = input("would you like to hear a joke? ")
  if(joke.lower() == 'no'):
    print("ok that's fine")
    break;
  elif (joke.lower()=='yes'):
    print(joke_response())
  else:
    print("I don't understand")
  


print("talk to you soon! :) ")
