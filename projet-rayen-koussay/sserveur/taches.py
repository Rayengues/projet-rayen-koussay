class Tache:
    def __init__(self, id, titre, description, auteur, statut="TODO"):
        self.id = id
        self.titre = titre
        self.description = description
        self.statut = statut
        self.auteur = auteur

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "description": self.description,
            "statut": self.statut,
            "auteur": self.auteur
        }
