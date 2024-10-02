import mysql.connector
from mysql.connector import Error

# Paramètres de connexion à la base de données MySQL
connection_config = {
    'host': 'localhost',
    'user': 'root',  # Remplace 'root' par ton nom d'utilisateur MySQL
    'password': '1234',  # Remplace par ton mot de passe MySQL
    'database': 'FoodAI'  # Nom de la base de données que tu veux utiliser
}

def main():
    connection = None

    try:
        # Se connecter à MySQL
        connection = mysql.connector.connect(**connection_config)

        if connection.is_connected():
            print("Connecté à MySQL avec succès")

            cursor = connection.cursor()

            # Créer une table si elle n'existe pas déjà
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(50),
                age INT,
                profession VARCHAR(50)
            )
            """
            cursor.execute(create_table_query)
            print("Table 'users' vérifiée/créée avec succès")

            # Insérer un document (équivalent à une ligne dans une table SQL)
            insert_query = """
            INSERT INTO ma_table (nom, age, profession)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, ('Farel', 25, 'Développeur'))
            connection.commit()
            print("Document inséré avec succès, ID :", cursor.lastrowid)

    except Error as err:
        print("Erreur lors de la connexion à MySQL :", err)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion fermée.")

# Appeler la fonction principale
if __name__ == '__main__':
    main()
