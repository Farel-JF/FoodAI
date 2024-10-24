// server.js
const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// MySQL connection
const db = mysql.createConnection({
    host: 'localhost', // Your database host
    user: 'root', // Your database user
    password: '1234', // Your database password
    database: 'FoodAI', // Your database name
});

db.connect(err => {
    if (err) {
        throw err;
    }
    console.log('MySQL connected...');
});

// Register route
app.post('/signup', (req, res) => {
    const { name, goal, diet, email, password } = req.body;

    // Validate input
    if (!name || !goal || !diet || !email || !password) {
        return res.status(400).json({ error: 'All fields are required' });
    }

    // Insert into Users table
    const query = 'INSERT INTO Users (name, goal, diet, email, password) VALUES (?, ?, ?, ?, ?)';
    db.query(query, [name, goal, diet, email, password], (err, results) => {
        if (err) {
            if (err.code === 'ER_DUP_ENTRY') {
                return res.status(409).json({ error: 'Email already exists' });
            }
            return res.status(500).json({ error: 'Database error' });
        }
        res.status(201).json({ message: 'User registered successfully', userId: results.insertId });
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
