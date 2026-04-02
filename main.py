from fastapi import FastAPI
from listaPokemon import pokemon_list
from pydantic import BaseModel

app = FastAPI() 

# READ
@app.get("/pokemons")
def get_pokemons():
    return pokemon_list



class Pokemon(BaseModel):
    name: str
    type: str


@app.post("/pokemons")
def create_pokemon(pokemon: Pokemon):
    new_id = len(pokemon_list) + 1
    
    new_pokemon = {
        "id": new_id,
        "name": pokemon.name,
        "type": pokemon.type
    }
    
    pokemon_list.append(new_pokemon)
    return new_pokemon



@app.delete("/pokemons/{pokemon_nome}")
def delete_pokemon(pokemon_nome : str):
    for index, pokemon in enumerate(pokemon_list):
        if  pokemon_nome == pokemon["name"]:
            return  pokemon_list.pop(index)
    return {"error": "Pokemon não encontrado"}
    




@app.put("/pokemons/{pokemon_id}")
def update_pokemon(pokemon_id: int, updated: Pokemon):
    for pokemon in pokemon_list:
        if pokemon["id"] == pokemon_id:
            pokemon["name"] = updated.name
            pokemon["type"] = updated.type
            return pokemon
    return {"error": "Pokemon não encontrado"}
    