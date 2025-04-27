from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Nécessaire pour utiliser session

# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname="chatbot_users",
    user='postgres',
    password="sofya",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_message = request.form['user_message']
        bot_response = generate_bot_response(user_message)

        # Sauvegarder la conversation
        cur.execute("""
            INSERT INTO conversations (user_id, user_message, bot_response)
            VALUES (%s, %s, %s)
        """, (session['user_id'], user_message, bot_response))
        conn.commit()

        return redirect(url_for('chat'))

    # Récupérer les conversations existantes
    cur.execute("""
        SELECT user_message, bot_response, timestamp
        FROM conversations
        WHERE user_id = %s
        ORDER BY timestamp ASC
    """, (session['user_id'],))
    conversations = cur.fetchall()

    return render_template('chat.html', conversations=conversations)

def generate_bot_response(user_message):
    # Ici tu mets ton intelligence du bot, pour l'instant réponse simple
    return "Bot: réponse à \"" + user_message + "\""

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO users (first_name, last_name, email, password_hash)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, email, hashed))
        conn.commit()

    return redirect(url_for('login'))  # Après inscription, redirige vers login

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password'].encode('utf-8')

    cur.execute("SELECT id, password_hash FROM users WHERE email = %s", (email,))
    result = cur.fetchone()

    if result and bcrypt.checkpw(password, result[1].encode('utf-8')):
        session['user_id'] = result[0]  # Enregistre l'id utilisateur en session
        return redirect(url_for('chat'))
    else:
        return "Email ou mot de passe incorrect."

if __name__ == '__main__':
    app.run(debug=True)
