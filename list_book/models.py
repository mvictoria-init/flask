from list_book import db
from sqlalchemy import Integer, String, Text, Boolean, DateTime, ForeignKey
from datetime import datetime

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return f'User: {self.username}'
    
class Book(db.Model):
    
    id = db.Column(Integer, primary_key=True)
    created_by = db.Column(Integer, ForeignKey('user.id'), nullable=False)
    title = db.Column(String(100), unique=True, nullable=False)
    author = db.Column(String(50), nullable=False)

    genre = db.Column(String(100), unique=True, nullable=False)
    desc = db.Column(Text)
    
    n_page = db.Column(Integer)  # Optional, can be nullable
    punctuation = db.Column(Integer)
    image = db.Column(String)  # Optional, can be nullable
    created = db.Column(DateTime, nullable=False, default=datetime.utcnow())
    
    state = db.Column(Boolean, default=False)
    
    def __init__(self, created_by, title, author, genre, desc, n_page, punctuation, image, state = False):
        self.created_by = created_by
        self.title = title
        self.author = author
        self.genre = genre
        self.desc = desc
        self.n_page = n_page
        self.punctuation = punctuation
        self.image = image
        self.state = state
