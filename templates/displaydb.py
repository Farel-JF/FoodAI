import mysql.connector

def connect_to_database():
    try:
        # Établir la connexion
        connection = mysql.connector.connect(
            host='localhost',  # ou l'adresse de votre serveur MySQL
            user='root',
            password='1234',
            database='FoodAI'
        )

        if connection.is_connected():
            print("Connexion réussie à la base de données")

            # Créer un curseur pour exécuter des requêtes
            cursor = connection.cursor()

            # Exécuter une requête pour récupérer des données
            cursor.execute("SELECT * FROM Users")
            print("Requête exécutée avec succès.")

            # Récupérer les résultats
            results = cursor.fetchall()
            print(f"Nombre de résultats : {len(results)}")  # Afficher le nombre de résultats

            # Afficher les résultats
            if results:
                for row in results:
                    print(row)
            else:
                print("Aucune donnée trouvée dans la table 'Users'.")

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion fermée.")

if __name__ == "__main__":
    connect_to_database()
