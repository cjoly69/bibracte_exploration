# 🏛️ Dashboard Bibracte — Données archéologiques fictives

Ce projet est une démonstration interactive construite avec [Streamlit](https://streamlit.io/), basée sur un jeu de données **fictif** inspiré des opérations archéologiques menées sur le site de **Bibracte** (Mont Beuvray).  
Les données ont été reconstruites à partir de l’article suivant :

🔗 [Opérations archéologiques à Bibracte (RAE, 2021)](https://journals.openedition.org/rae/17199)

---

## 🚀 Lancer l'application en local

### 1. Cloner le projet ou copier les fichiers
```bash
git clone https://gitlab.com/ton-utilisateur/ton-projet.git
cd ton-projet
```

### 2. (Optionnel) Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
streamlit run app.py
```

---

## 🌐 Déploiement en ligne avec Streamlit Community Cloud

1. Crée un compte gratuit sur [streamlit.io/cloud](https://streamlit.io/cloud)
2. Héberge ton projet sur GitLab ou GitHub dans un dépôt public
3. Clique sur **"New app"** sur le site de Streamlit Cloud
4. Renseigne :
   - Le lien du dépôt
   - Le nom du fichier principal : `app.py`
   - La branche à utiliser (ex. `main`)
5. Clique sur **Deploy**

Streamlit va automatiquement :
- Installer les dépendances (via `requirements.txt`)
- Lancer ton application

---

## 📁 Données

Le fichier `base_bibracte.csv` contient une série d'opérations archéologiques fictives avec les champs suivants :
- `site` : nom de l’intervention ou du secteur
- `type` : type d’intervention (fouille, sondage, relevé topo, etc.)
- `responsable` : institution ou équipe responsable
- `surface_m2` : surface fouillée ou prospectée
- `annee` : année principale de l’intervention
- `description` : résumé synthétique

---

## 📍 Objectif

- Explorer les opérations de terrain sous forme de tableau interactif
- Visualiser les tendances par année et type d’intervention
- Fournir un exemple simple de valorisation de données archéologiques via un outil moderne, responsive, et facilement déployable
- Expérimenter les bases de Streamlit avec des composants interactifs (filtres, graphiques Plotly, bouton de téléchargement)

---

## 📦 Dépendances

Le fichier `requirements.txt` inclut :

```
streamlit
pandas
plotly
```

---

## 👩‍💻 Auteure & mentions

Projet développé par **Catherine Joly** dans le cadre d’un exercice personnel de valorisation de données spatiales et patrimoniales.  
Le jeu de données est entièrement fictif, construit à des fins d’illustration à partir de sources publiques.

🔗 Source documentaire :  
> “Le Mont Beuvray et Bibracte. Chronique des activités archéologiques 2017-2021”,  
> Revue Archéologique de l’Est [En ligne], 70 | 2021, mis en ligne le 01 janvier 2023.  
> [https://journals.openedition.org/rae/17199](https://journals.openedition.org/rae/17199)

---
