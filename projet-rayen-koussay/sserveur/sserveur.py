import socket
import json
from gestionnaire import GestionnaireTaches

HOST = "0.0.0.0"
PORT = 5000

gest = GestionnaireTaches()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[SERVEUR] En écoute sur {HOST}:{PORT}")

while True:
    client_sock, addr = server.accept()
    print(f"[+] Client connecté : {addr}")

    data = client_sock.recv(4096).decode()

    try:
        req = json.loads(data)
    except json.JSONDecodeError:
        client_sock.send(b"Requete invalide")
        client_sock.close()
        continue

    action = req.get("action")

    if action == "add":
        t = gest.ajouter_tache(
            req.get("titre", ""),
            req.get("description", ""),
            req.get("auteur", "")
        )
        client_sock.send(json.dumps(t.to_dict()).encode())

    elif action == "list":
        client_sock.send(json.dumps(gest.lister_taches()).encode())

    elif action == "del":
        ok = gest.supprimer_tache(req.get("id"))
        client_sock.send(json.dumps({"deleted": ok}).encode())

    elif action == "status":
        ok = gest.changer_statut(req.get("id"), req.get("statut"))
        client_sock.send(json.dumps({"status_changed": ok}).encode())

    else:
        client_sock.send(b"Action inconnue")

    client_sock.close()
