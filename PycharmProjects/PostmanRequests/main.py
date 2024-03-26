

#importeer de 'requests' bibliotheek
import requests

# stuur een HTTP GET request naar de riddles-api en sla het antwoord op in de variabele 'response'
response = requests.get('https://riddles-api.vercel.app/random')

# interpreteer het antwoord als een JSON string
json_response = response.json()

# haal de waarde van 'riddle' (i.e. het raadsel) uit de JSON string
extracted_riddle = json_response['riddle']

# haal de waarde van 'answer' (i.e. het antwoord) uit de JSON string
extracted_answer = json_response['answer']

# print het raadsel
print(f'Riddle: {extracted_riddle}')


# wacht tot de gebruiker op enter drukt
input()

# print het antwoord
print(f'Answer: {extracted_answer}')
