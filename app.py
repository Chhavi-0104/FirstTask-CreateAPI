from fastapi import FastAPI #webframework
from pydantic import BaseModel
# Pydantic : enforces type hints at runtime. It provides user-friendly errors, allowing us to catch any invalid data.
class Student(BaseModel) :
    name: str
    age: int
app = FastAPI()
students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]
# ****************To Get All Students List******************
@app.get('/students')
def user_list():
    return {'students': students}

# *********** To ADD Student ********************
@app.post('/students')
def user_add(student: Student):
    students.append(student)
    return {'student': students[-1]}
    
# ************** To UPDATE Student*****************
@app.put('/students/{student_id}')
def user_update(student: Student, student_id: int):
    students[student_id].update(student)
    return {'student': students[student_id]}

# ************* To DELETE Student ****************
@app.delete('/students/{student_id}')
def user_delete(student_id: int):
    del students[student_id]
    return {'students': students}
