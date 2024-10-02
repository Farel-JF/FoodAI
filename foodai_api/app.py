from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Remplacez par une clé secrète

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'foodai_db'
}

# Route pour afficher le formulaire d'inscription
@app.route('/signup')
def signup():
    if 'user_id' in session:
        # Si l'utilisateur est déjà connecté ou enregistré, on le redirige vers la page d'accueil ou tableau de bord
        return redirect(url_for('dashboard'))  # Changez vers la route appropriée
    return render_template('signup.html')

# Route pour traiter le formulaire d'inscription
@app.route('/signup_process', methods=['POST'])
def signup_process():
    email = request.form['email']
    password = request.form['password']

    # Connexion à la base de données
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Vérifier si l'utilisateur existe déjà
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        return "User already exists. Please <a href='/login'>login</a>."

    # Hachage du mot de passe
    hashed_password = generate_password_hash(password)

    # Insertion des données dans la table users
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
        conn.commit()

        # Ajouter l'utilisateur à la session pour qu'il soit considéré comme connecté
        session['user_id'] = cursor.lastrowid
        return redirect(url_for('dashboard'))
    except mysql.connector.Error as err:
        return f"Erreur: {err}"
    finally:
        cursor.close()
        conn.close()

# Route pour afficher la page de connexion
@app.route('/login')
def login():
    return render_template('login.html')

# Tableau de bord après connexion
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return "Bienvenue sur votre tableau de bord !"

# Route pour déconnexion
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
