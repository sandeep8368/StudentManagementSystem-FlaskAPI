from flask import Flask, request, jsonify
from database import db
from models import StudentModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    
    

#CREATE.............
@app.route('/student/', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = StudentModel(name = data['name'],
                           email = data['email'],
                           phone = data['phone'])
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201



#READ ALL
@app.route('/student/', methods=['GET'])
def all_students():
    student = StudentModel.query.all()
    return jsonify([s.to_dict() for s in student])



#READ ONE
@app.route('/student/<int:id>', methods = ['GET'])
def get_student(id):
    student = StudentModel.query.get(id)
    if student:
        return jsonify(student.to_dict())
    return jsonify({"error" : "Student not found"}), 404



#DELETE STUDENT
@app.route('/student/<int:id>', methods = ['DELETE'])
def delete_student(id):
    student = StudentModel.query.get(id)
    if not student:
        return jsonify({"error" : "student not found"})
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message" : "student deleted"})




#UPDATE STUDENT
@app.route('/student/<int:id>', methods = ['PUT'])
def update_student(id):
    student = StudentModel.query.get(id)
    if not student:
        return jsonify({"error" : "student not found"}), 404
    data = request.get_json()
    student.name = data['name']
    student.email = data['email']
    student.phone = data['phone']
    db.session.commit()
    return jsonify(student.to_dict())


app.run(debug=True)