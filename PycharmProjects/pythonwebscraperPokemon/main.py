import requests
from bs4 import BeautifulSoup

url = 'https://pokemondb.net/pokedex/all'


def fetch_pokemon_data():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='data-table')
        pokemon_data = {}
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            number = columns[0].text.strip()
            name = columns[1].text.strip()
            type_1 = columns[2].text.strip()
            type_2 = columns[3].text.strip() if len(columns) > 3 else ""
            hp = columns[5].text.strip()
            if number not in pokemon_data:
                pokemon_data[number] = (name, type_1, type_2, hp)
        return pokemon_data
    else:
        print("Failed to retrieve data from the website.")
        return {}


def display_pokemon_list(pokemon_data):
    print("Pokémon List:")
    for number, info in pokemon_data.items():
        name, _, _, _ = info
        print(f"{number}: {name}")


def display_pokemon_stats(pokemon_data, pokemon_number):
    if pokemon_number in pokemon_data:
        name, type_1, type_2, hp = pokemon_data[pokemon_number]
        print(f"\nName: {name}")
        print(f"Number: {pokemon_number}")
        print(f"Type: {type_1} {type_2}")
        print(f"HP: {hp}")
    else:
        print("Pokémon not found.")


def main():
    pokemon_data = fetch_pokemon_data()
    if pokemon_data:
        display_pokemon_list(pokemon_data)
        while True:
            pokemon_number = input(
                "\nEnter the number of a Pokémon to get more information (or type 'exit' to quit): ").strip()
            if pokemon_number.lower() == 'exit':
                break
            display_pokemon_stats(pokemon_data, pokemon_number)


if __name__ == "__main__":
    main()
