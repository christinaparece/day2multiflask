from flask import render_template, request
import requests
from app import app
from .forms import LoginForm, PokemonForm 


@app.route("/")
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():  #what appears on navbar
    form= PokemonForm()
    if request.method== 'POST':
        pokemon = request.form.get('pokemon')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(url)
        if response.ok:  ##means it worked
            if not response.json():
                return "We had an error loading your data, please try again"
            data = response.json()
            my_pokemon=[]
            for pokemon in data:
                pokemon_dict= {
                "name": data["forms"][0]["name"],
                "ability_name": data["abilities"][0]["ability"]["name"],
                "base_experience": data["base_experience"],
                'sprite': data["sprites"]["front_shiny"],
                }
            my_pokemon.append(pokemon_dict)
            print(my_pokemon)
            return render_template("pokemon.html.j2", pokemons=my_pokemon)     
        else:
            return "Please try your search again"

    return render_template("pokemon.html.j2")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST': #and form.validate_on_submit():
        email = request.form.get("email").lower()
        password = request.form.get("password")
        if email in app.config.get('REGISTERED_USERS') and \
            password== app.config.get('REGISTERED_USERS').get(email).get('password'):
            return f"Login Success Welcome {app.config.get('REGISTERED_USERS').get(email).get('name')}" 
        error_string = "Incorrect Email/Password Combo"
        return render_template("login.html.j2", error=error_string)

    return render_template("login.html.j2", form=form)