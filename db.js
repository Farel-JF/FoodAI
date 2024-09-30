// Importer MongoClient depuis le package mongodb
const { MongoClient } = require('mongodb');

// URL de connexion (par défaut, MongoDB écoute sur localhost:27017)
const url = 'mongodb://localhost:27017';

// Nom de la base de données
const dbName = 'ma_base_de_donnees';

// Fonction principale pour se connecter à MongoDB et insérer des données
async function main() {
  // Créer un nouveau client MongoDB
  const client = new MongoClient(url);

  try {
    // Se connecter au serveur MongoDB
    await client.connect();
    console.log("Connecté à MongoDB avec succès");

    // Sélectionner la base de données (elle sera créée si elle n'existe pas)
    const db = client.db(dbName);

    // Sélectionner la collection (elle sera créée si elle n'existe pas)
    const collection = db.collection('ma_collection');

    // Insérer un document (équivalent à une ligne dans une base SQL)
    const document = { nom: "Farel", age: 25, profession: "Développeur" };
    const result = await collection.insertOne(document);

    console.log("Document inséré avec succès :", result.insertedId);
  } catch (err) {
    console.error("Erreur lors de la connexion à MongoDB :", err);
  } finally {
    // Fermer la connexion
    await client.close();
  }
}

// Appeler la fonction principale
main().catch(console.error);
