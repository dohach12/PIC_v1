## Structure du Projet
```

projet-chatbot/
├── app.py                 # Backend Flask principal
├── templates/
│   ├── index.html         # Page d'accueil
│   ├── login.html         # Page de connexion
│   ├── register.html      # Page d'inscription
│   └── chat.html          # Interface de discussion
└── static/
    └── css/
        ├── style-chat.css      # Styles du chat
        └── style-sidebar.css   # Styles de la sidebar
```

---
**Base de Données (PostgreSQL)**:

Créez une base de données nommée energy_chatbot:

# Guide de création de la base de données PostgreSQL

## 1. Connexion à PostgreSQL

Ouvre ton terminal et connecte-toi à PostgreSQL avec la commande suivante :

```bash
psql -U postgres
```

## 2. Création de la base de données

Crée une nouvelle base de données appelée chatbot_users :

```sql
CREATE DATABASE chatbot_users;
```
## 3. Connexion à la base de données

Connecte-toi à la base de données que tu viens de créer :

```sql
\c chatbot_users
```


**Table users:**  Stocke les informations des utilisateurs. 
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---
**Table conversations** Garde l'historique des discussions.

```sql

CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```








