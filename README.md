## Structure du Projet

projet-chatbot/
├── app.py # Backend Flask
├── templates/
│ └── index.html # Page web principale (HTML)
│  └── login.html 
│ └── register.html 
│ └── chat.html 
├── static/
│ └── style-chat.css 
  └── style-sidebar.css 

## Base de Données (PostgreSQL)
Créez une base de données nommée energy_chatbot:
**Table `users:**  Stocke les informations des utilisateurs.  
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
**Table conversations** Garde l'historique des discussions.
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



