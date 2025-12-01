import socket
import json

def envoyer(req):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 5000))
    s.send(json.dumps(req).encode())
    data = s.recv(4096).decode()
    s.close()
    return data

while True:
    print("\n=== MENU ===")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Supprimer une tâche")
    print("4. Changer statut")
    print("0. Quitter")

    choix = input("Choix: ")

    if choix == "1":
        titre = input("Titre: ")
        desc = input("Description: ")
        auteur = input("Auteur: ")

        req = {"action": "add", "titre": titre, "description": desc, "auteur": auteur}
        print(envoyer(req))

    elif choix == "2":
        print(envoyer({"action": "list"}))

    elif choix == "3":
        id = input("ID: ")
        print(envoyer({"action": "del", "id": id}))

    elif choix == "4":
        id = input("ID: ")
        statut = input("Statut (TODO/DOING/DONE): ")
        print(envoyer({"action": "status", "id": id, "statut": statut}))

    elif choix == "0":
        break
