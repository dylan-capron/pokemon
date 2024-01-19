import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from PIL import Image, ImageTk
import pygame
import subprocess

class PokemonMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokemon Mystic")

        # Initialisation de Pygame
        pygame.init()

        # Chargement du logo
        self.logo_image = Image.open("Pokemon Menu/580b57fcd9996e24bc43c325.png")
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.tk.call('wm', 'iconphoto', self._w, self.logo_image)

        # Chargement de l'image de fond
        self.background_image_original = Image.open("Pokemon Menu/test.png")
        self.background_image = ImageTk.PhotoImage(self.background_image_original)

        # Initialisation de la musique
        pygame.mixer.music.load("Pokemon Menu/Gotta catch 'em all [8-Bit Cover] Pokémon OP 1_OMaNoXrCC9s.mp3")
        pygame.mixer.music.play(-1)

        # Canvas pour afficher l'image de fond
        self.background_canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.background_canvas.pack(fill=tk.BOTH, expand=True)

        # Calculer la position pour centrer l'image de fond
        x_position = (self.winfo_screenwidth() - self.background_image.width()) / 2
        y_position = (self.winfo_screenheight() - self.background_image.height()) / 2

        # Afficher l'image de fond dans le Canvas
        self.background_canvas.create_image(x_position, y_position, anchor=tk.NW, image=self.background_image)

        # Conteneur pour les boutons
        bouton_container = tk.Frame(self, bg="black")
        bouton_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Création des boutons
        start_game_button = tk.Button(bouton_container, text="Lancer une partie", command=self.start_game, bg="red")
        start_game_button.grid(row=0, column=0, padx=10)

        add_pokemon_button = tk.Button(bouton_container, text="Ajouter un Pokémon", command=self.add_pokemon, bg="green")
        add_pokemon_button.grid(row=0, column=1, padx=10)

        pokedex_button = tk.Button(bouton_container, text="Accéder au Pokédex", command=self.access_pokedex, bg="white")
        pokedex_button.grid(row=0, column=2, padx=10)

        self.create_widgets()

        # Écouteur d'événements de redimensionnement
        self.bind("<Configure>", self.on_window_resize)

    def create_widgets(self):
        # Ajoutez ici d'autres éléments d'interface utilisateur si nécessaire
        pass

    def on_window_resize(self, event):
        # Redimensionner l'image de fond lorsque la fenêtre est redimensionnée
        new_width = event.width
        new_height = event.height
        resized_background = self.background_image_original.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(resized_background)
        self.background_canvas.config(width=new_width, height=new_height)
        self.background_canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

    def start_game(self):
        # Exécuter le fichier game.py
        subprocess.run(["python", r"Jeu/game.py"])

        # Vous pouvez également ajouter d'autres actions à effectuer après le lancement du jeu, si nécessaire.
        messagebox.showinfo("Info", "Vous avez choisi de lancer une nouvelle partie.")

    def add_pokemon(self):
        # Dialogue pour saisir les détails du Pokémon
        pokemon_name = simpledialog.askstring("Ajouter un Pokémon", "Nom du Pokémon:")
        pokemon_type = simpledialog.askstring("Ajouter un Pokémon", "Type du Pokémon:")
        pokemon_level = simpledialog.askinteger("Ajouter un Pokémon", "Niveau du Pokémon:")

        # Création d'un dictionnaire avec les détails du Pokémon
        new_pokemon = {"Nom": pokemon_name, "Type": pokemon_type, "Niveau": pokemon_level}

        # Ajout du Pokémon au fichier JSON
        try:
            with open("pokemon-matt-o/pokedex.json", "r") as file:
                pokemon_data = json.load(file)
        except FileNotFoundError:
            pokemon_data = []

        pokemon_data.append(new_pokemon)

        with open("pokemon-matt-o/pokedex.json", "w") as file:
            json.dump(pokemon_data, file)

        messagebox.showinfo("Info", f"Le Pokémon {pokemon_name} a été ajouté au Pokédex!")

    def access_pokedex(self):
        try:
            with open("pokemon-matt-o/pokedex.json", "r") as file:
                pokemon_data = file.read()

            messagebox.showinfo("Pokédex", f"Contenu du Pokédex :\n{pokemon_data}")

        except FileNotFoundError:
            messagebox.showinfo("Pokédex", "Le Pokédex est vide. Ajoutez des Pokémon pour les voir ici.")

if __name__ == "__main__":
    app = PokemonMenu()
    app.geometry("1920x1080")  # Taille initiale
    app.mainloop()
