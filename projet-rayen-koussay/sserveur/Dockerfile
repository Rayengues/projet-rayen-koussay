# Utiliser Python 3 slim comme image de base
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tous les fichiers du serveur dans le conteneur
COPY . .

# Installer les dépendances si requirements.txt existe
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Exposer le port du serveur
EXPOSE 5000

# Lancer le serveur
CMD ["python3", "sserveur.py"]
