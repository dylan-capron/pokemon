import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter

# Charger le fichier JSON avec l'encodage UTF-8
with open('pokedex.json', 'r', encoding='utf-8') as file:
    pokedex_data = json.load(file)

# Fonction pour rechercher un Pokémon par nom (insensible à la casse, prenant en compte les caractères spéciaux)
def find_pokemon_by_name(name):
    for pokemon in pokedex_data['pokemons']:
        if pokemon['nom'].casefold() == name.casefold():
            return pokemon
    return None

# Fonction appelée lors de la sélection d'un Pokémon dans le menu
def show_selected_pokemon(event):
    selected_index = pokemon_listbox.curselection()
    if selected_index:
        selected_pokemon_name = pokemon_listbox.get(selected_index)
        selected_pokemon = find_pokemon_by_name(selected_pokemon_name)
        
        if selected_pokemon:
            if selected_pokemon.get('captured', False):  # Vérifiez si le Pokémon a été capturé
                result_label.config(text=f"Informations sur {selected_pokemon_name}\nID: {selected_pokemon['id']}\nType: {selected_pokemon['type']}\nTaille: {selected_pokemon['taille']} m\nPoids: {selected_pokemon['poids']}")
            else:
                result_label.config(text=f"Informations sur {selected_pokemon_name}\nID: ???\nType: ???\nTaille: ??? m\nPoids: ??? kg\n\nDonnées inconnues (non capturé)")

            # Afficher l'image du Pokémon
            show_pokemon_image(selected_pokemon_name)

# ...

# Exemple de modification des données du Pokémon pour indiquer qu'il a été capturé
# Vous pouvez ajuster cela en fonction de votre logique de jeu
# Dans cet exemple, le Pokémon avec le nom 'Pikachu' a été capturé
pokedex_data['pokemons'][0]['captured'] = True

# ...


def show_pokemon_image(pokemon_name):
    # Charger l'image du Pokémon (assurez-vous que le nom de l'image correspond au nom du Pokémon)
    image_path = f"images/{pokemon_name.lower()}.png"  # Vous devez avoir les images stockées dans un dossier 'images'
    
    try:
        pokemon_image = Image.open(image_path)
        pokemon_image.thumbnail((150, 150))
        photo = ImageTk.PhotoImage(pokemon_image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(image=None)


# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Pokédex")

# Créer des widgets
result_label = ttk.Label(window, text="")
image_label = ttk.Label(window)


# Créer une Listbox pour afficher la liste des Pokémon
pokemon_listbox = tk.Listbox(window, selectbackground="yellow", selectmode=tk.SINGLE)
for pokemon in pokedex_data['pokemons']:
    pokemon_listbox.insert(tk.END, pokemon['nom'])

# Associer la fonction show_selected_pokemon à l'événement de clic sur la Listbox
pokemon_listbox.bind("<ButtonRelease-1>", show_selected_pokemon)

# Disposer les widgets dans la fenêtre
pokemon_listbox.pack(pady=10)
result_label.pack(pady=10)
image_label.pack(pady=10)

# Lancer la boucle principale Tkinter
window.mainloop()
