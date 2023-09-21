from config.database import db

class user(db.Model):
    __tablename__ = "users";
        
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100), nullable= True)
    avatar = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, email, first_name, last_name, avatar):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar