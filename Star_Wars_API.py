import requests
import json
def features():
    

    hairColor = input("What your hair color? ")
    eyeColor = input("What is your eye color? ")
    gender = input("What is your gender? ")
   
    

   #hairColor
    i = 1
    person1 = " "
    
    while i < 10:
        movie_number = i
        base_url = "https://swapi.dev/api/people/"
        full_url = f"{base_url}{movie_number}/"
       
       # print(full_url)
        response = requests.get(full_url)
        data = response.json()
       # print(data)

        
        
        if data["hair_color"] == hairColor.lower():
            personName = data["name"]
           # person1.append(personName)
            person1 = personName
        
         
        i += 1


#eyeColor
    i = 1
    person2 = "."
    
    while i < 10:
        movie_number = i
        base_url = "https://swapi.dev/api/people/"
        full_url = f"{base_url}{movie_number}/"
       
       # print(full_url)
        response = requests.get(full_url)
        data = response.json()
       # print(data)

        
        
        if data["eye_color"] == eyeColor.lower():
            personName = data["name"]
           # person1.append(personName)
            person2 = personName
        
         
        i += 1


    #gender
    i = 1
    person3 = ","
    
    while i < 10:
        movie_number = i
        base_url = "https://swapi.dev/api/people/"
        full_url = f"{base_url}{movie_number}/"
       
       # print(full_url)
        response = requests.get(full_url)
        data = response.json()
       # print(data)

        
        
        if data["gender"] == gender.lower():
            personName = data["name"]
           # person1.append(personName)
            person3 = personName
        
         
        i += 1
    
   

    #determining person

    if (person1 == person2) or (person2 == person3):
        return f"Your starwars lookalike is{person2}"
    
    elif (person1 == person3) or (person1 == person2):
        return f"Your starwars lookalike is {person1}"

    elif (person1 == person3) or (person2 == person3): 
        return f"Your starwars lookalike is {person3}"
    
    else:
        return "You don't have a starwars lookalike. sorry :("
    
     



            
    
    
    
print(features())
