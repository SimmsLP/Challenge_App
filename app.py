# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Using SQLite for simplicity
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, 75 Hard Challenge!"

if __name__ == '__main__':
    app.run(debug=True)




