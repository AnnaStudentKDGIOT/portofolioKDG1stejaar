import requests
from bs4 import BeautifulSoup

def get_pokedex_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='data-table block-wide')
        if table:
            pokemon_data = []
            for row in table.find_all('tr')[1:]:
                cells = row.find_all('td')
                if len(cells) > 0:
                    pokemon_number = cells[0].text.strip()
                    pokemon_name = cells[1].find('a').text.strip()
                    pokemon_types = [a.text for a in cells[2].find_all('a')]
                    pokemon_hp = cells[5].text.strip()
                    pokemon_data.append({
                        'number': pokemon_number,
                        'name': pokemon_name,
                        'types': pokemon_types,
                        'hp': pokemon_hp
                    })
            return pokemon_data
        else:
            print("Table not found on the webpage.")
            return None
    else:
        print("Failed to retrieve webpage.")
        return None

def display_pokedex(pokedex_data):
    if pokedex_data:
        for pokemon in pokedex_data:
            print("Number:", pokemon['number'])
            print("Name:", pokemon['name'])
            print("Types:", ', '.join(pokemon['types']))
            print("HP:", pokemon['hp'])
            print("-" * 30)
    else:
        print("No Pokédex data available.")

def main():
    url = "https://pokemondb.net/pokedex/all"
    pokedex_data = get_pokedex_data(url)
    display_pokedex(pokedex_data)

if __name__ == "__main__":
    main()
