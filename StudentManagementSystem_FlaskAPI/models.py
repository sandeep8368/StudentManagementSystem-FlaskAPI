from database import db

class StudentModel(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone = db.Column(db.Integer, nullable = False, unique = True)
    
    def to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "phone" : self.phone
        }