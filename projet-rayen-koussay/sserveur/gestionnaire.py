from taches import Tache

class GestionnaireTaches:
    def __init__(self):
        self.taches = {}
        self.next_id = 1

    def ajouter_tache(self, titre, description, auteur):
        t = Tache(self.next_id, titre, description, auteur)
        self.taches[self.next_id] = t
        self.next_id += 1
        return t

    def supprimer_tache(self, id):
        id = int(id)
        if id in self.taches:
            del self.taches[id]
            return True
        return False

    def lister_taches(self):
        return [t.to_dict() for t in self.taches.values()]

    def changer_statut(self, id, statut):
        id = int(id)
        if id in self.taches:
            self.taches[id].statut = statut
            return True
        return False
