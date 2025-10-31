import sqlite3
import os

# Hardcoded credentials - should be caught by Semgrep
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "SuperSecret123!"

def get_user_data(user_id):
    """Vulnerable function with SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # SQL injection vulnerability - user input directly concatenated
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)

    return cursor.fetchall()

def authenticate_user(username, password):
    """Another SQL injection example"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    return cursor.fetchone()

# Using eval with user input - dangerous
def process_command(user_input):
    result = eval(user_input)
    return result

# Weak random number generation for security purposes
import random
def generate_token():
    token = random.randint(1000000, 9999999)
    return str(token)

# Hardcoded credentials - should be caught by Semgrep
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "SuperSecret123!"

def get_user_data(user_id):
    """Vulnerable function with SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # SQL injection vulnerability - user input directly concatenated
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)

    return cursor.fetchall()

def authenticate_user(username, password):
    """Another SQL injection example"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    return cursor.fetchone()

# Using eval with user input - dangerous
def process_command(user_input):
    result = eval(user_input)
    return result

# Weak random number generation for security purposes
import random
def generate_token():
    token = random.randint(1000000, 9999999)
    return str(token)
