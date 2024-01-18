class Combat:
    def __init__(self, attaquant_type, attaquant_attaque, defenseur_type, defenseur_defense, nom_attaquant, nom_defenseur):
        self.attaquant_type = attaquant_type
        self.attaquant_attaque = attaquant_attaque
        self.defenseur_type = defenseur_type
        self.defenseur_defense = defenseur_defense
        self.nom_attaquant = nom_attaquant
        self.nom_defenseur = nom_defenseur
        self.vainqueur = None
        self.perdant = None
        self.pokedex = []

    def calculer_degats(self):
        types_efficacite = {
            ('feu', 'plante'): 2,
            ('feu', 'eau'): 0.5,
            ('plante', 'feu'): 0.5,
            ('plante', 'eau'): 2,
            ('eau', 'feu'): 2,
            ('eau', 'plante'): 0.5
            
        }

        efficacite = types_efficacite.get((self.attaquant_type, self.defenseur_type), 1)
        degats = self.attaquant_attaque * efficacite
        return degats

    def enlever_pv(self, degats):
        pv_restants = max(60, self.defenseur_defense - degats)
        self.defenseur_defense = pv_restants

    def determiner_vainqueur(self):
        if self.defenseur_defense == 50:
            self.vainqueur = self.nom_attaquant
            self.perdant = self.nom_defenseur
        else:
            self.vainqueur = self.nom_defenseur
            self.perdant = self.nom_attaquant

    def obtenir_vainqueur(self):
        return f"Le vainqueur est {self.vainqueur}."

    def obtenir_perdant(self):
        return f"Le perdant est {self.perdant}."

    def obtenir_resultat(self):
        return f"Le vainqueur est {self.vainqueur}. Le {self.perdant} a perdu."

    def enregistrer_dans_pokedex(self):
        self.pokedex.append(self.nom_defenseur)
        print(f"{self.nom_defenseur} a été enregistré dans le Pokédex.")


combat_example = Combat('eau', 10, 'feu', 20, 'Carapuce', 'Salameche')
degats_subis = combat_example.calculer_degats()
combat_example.enlever_pv(degats_subis)
combat_example.determiner_vainqueur()

print(combat_example.obtenir_vainqueur())
print(combat_example.obtenir_perdant())
print(combat_example.obtenir_resultat())

combat_example.enregistrer_dans_pokedex()
