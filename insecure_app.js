const express = require('express');
const { exec } = require('child_process');
const crypto = require('crypto');

const app = express();

// Hardcoded secret - should be caught by Semgrep
const JWT_SECRET = "hardcoded-secret-key-123";
const AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE";

// Command injection vulnerability
app.get('/run', (req, res) => {
    const filename = req.query.file;
    // Dangerous: user input directly in exec
    exec('cat ' + filename, (error, stdout, stderr) => {
        if (error) {
            res.status(500).send(error);
            return;
        }
        res.send(stdout);
    });
});

// Another command injection example
app.post('/backup', (req, res) => {
    const backupPath = req.body.path;
    exec(`tar -czf backup.tar.gz ${backupPath}`, (error, stdout) => {
        res.send('Backup created');
    });
});

// Insecure random number generation for security
function generateSessionId() {
    return Math.random().toString(36);
}

// SQL injection in template string
function getUserByEmail(email) {
    const query = `SELECT * FROM users WHERE email = '${email}'`;
    // database.query(query);
    return query;
}

// Weak crypto algorithm
function hashPassword(password) {
    return crypto.createHash('md5').update(password).digest('hex');
}

app.listen(3000);
