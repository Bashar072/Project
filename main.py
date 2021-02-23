import pymysql
from app import app
from Config import mysql
from flask import jsonify
from flask import flash,request

@app.route('/adduser', methods=['POST'])
def add_User():
    try:
        _json = request.json
        _Email = _json['Email']
        _Role = _json['Role']
        Is_active = _json['Is_active']
        if _Email and _Role and Is_active and request.method == 'POST':
            sqlQuery = "INSERT INTO User(Email, Role, Is_active) VALUES(%s, %s, %s)"
            bindData = (_Email, _Role, Is_active)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/users')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT Id, Email, Role, Is_active FROM User")
        userRows = cursor.fetchall()
        respone = jsonify(userRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/user/<int:id>')
def user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT Id, Email, Role, Is_active FROM User WHERE id =%s", id)
        userRow = cursor.fetchone()
        respone = jsonify(userRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/addstudent', methods=['POST'])
def add_student():
    try:
        _json = request.json
        _Pid = _json['Pid']
        _Email = _json['Email']
        _Dept_name = _json['Dept_name']
        _Course_Name = _json['Course_Name']
        _Date_of_birth = _json['Date_of_birth']
        _CGPA = _json['CGPA']
        _Semester = _json['Semester']
        _Description = _json['Description']
        if _Pid and _Email and _Dept_name and _Course_Name and _Date_of_birth and _CGPA and _Semester and _Description and request.method == 'POST':
            sqlQuery = "REPLACE INTO Students(Pid, Email, Dept_name, Course_Name, Date_of_birth, CGPA, Semester, Description) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            bindData = (_Pid, _Email, _Dept_name, _Course_Name, _Date_of_birth, _CGPA, _Semester, _Description)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('student added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/students')
def students():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT Pid, Email, Dept_name, Course_Name, Date_of_birth, CGPA, Semester, Description FROM Students")
        studentRows = cursor.fetchall()
        respone = jsonify(studentRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/student/<int:id>')
def student(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT Pid, Email, Dept_name, Course_name, Date_of_birth, CGPA, Semester, Description FROM Students WHERE Pid =%s", id)
        studentRow = cursor.fetchone()
        respone = jsonify(studentRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run(debug=True)