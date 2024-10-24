// Importer le module mysql2
const mysql = require('mysql2/promise');

// Paramètres de connexion à la base de données MySQL
const connectionConfig = {
  host: 'localhost',
  user: 'root', // Remplace 'root' par ton nom d'utilisateur MySQL
  password: '', // Remplace par ton mot de passe MySQL
  database: 'ma_base_de_donnees' // Nom de la base de données que tu veux utiliser
};

// Fonction principale pour se connecter à MySQL et insérer des données
async function main() {
  let connection;

  try {
    // Se connecter à MySQL
    connection = await mysql.createConnection(connectionConfig);
    console.log("Connecté à MySQL avec succès");

    // Créer une table si elle n'existe pas déjà
    const createTableQuery = `
      CREATE TABLE IF NOT EXISTS ma_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(50),
        age INT,
        profession VARCHAR(50)
      )
    `;
    await connection.execute(createTableQuery);
    console.log("Table 'ma_table' vérifiée/créée avec succès");

    // Insérer un document (équivalent à une ligne dans une table SQL)
    const insertQuery = `
      INSERT INTO ma_table (nom, age, profession)
      VALUES (?, ?, ?)
    `;
    const [result] = await connection.execute(insertQuery, ['Farel', 25, 'Développeur']);

    console.log("Document inséré avec succès, ID :", result.insertId);
  } catch (err) {
    console.error("Erreur lors de la connexion à MySQL :", err);
  } finally {
    // Fermer la connexion
    if (connection) await connection.end();
  }
}

// Appeler la fonction principale
main().catch(console.error);
