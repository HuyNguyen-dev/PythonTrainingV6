from flask import jsonify,request,json
from app.models.models import User
from sqlalchemy import text,insert
from sqlalchemy.exc import DataError
from app import db

def getalldata():
    
    if request.args.get('query_type') == "nativequery":
        with db.engine.connect() as conn:
            rows = conn.execute(text("SELECT * FROM mydb.user"))
            
            # Get all the column names of the table in order to iterate through
            column_keys = User.__table__.columns.keys()
            # Temporary dictionary to keep the return value from table
            rows_dic_temp = {}
            rows_dic = []
            # Iterate through the returned output data set
            for row in rows:
                for col in column_keys:
                    rows_dic_temp[col] = getattr(row, col)
                rows_dic.append(rows_dic_temp)
                rows_dic_temp= {}
            return jsonify(rows_dic)
    else:
        users = User.query.all()
        users_list = []
        for user in users:
            user_json = {
                'id': user.id,
                'username': user.username,
                'full_name': user.full_name,
                'email': user.email,
                'phone_number': user.phone_number,
                'report_access': user.report_access,
                'view_costs': user.view_costs,
                'last_login_date': user.last_login_date,
                'enabled': user.enabled,
                'is_corporated': user.is_corporated,
                'created_on': user.created_on,
                'modified_on': user.modified_on,
            }
            users_list.append(user_json)
        return jsonify(users_list)
 

def insertdata():
    try:
        user = User(
            username = request.json['username'],
            full_name = request.json.get('full_name'),
            email = request.json['email'],
            phone_number = request.json.get('phone_number'),
            report_access = request.json.get('report_access'),
            view_costs = request.json.get('view_costs'),
            last_login_date = request.json.get('last_login_date'),
            enabled = request.json.get('enabled') if request.json.get('enabled') != None else True,
            is_corporated = request.json.get('is_corporated') if request.json.get('is_corporated') != None else False,
            created_on = request.json.get('created_on'),
            modified_on = request.json.get('modified_on'))

        if 'nativequery' not in request.path:
                db.session.add(user)
                db.session.commit()
                return jsonify({'status': 200,'message': 'User created successfully!'}), 200
        else:
            with db.engine.connect() as conn:
                statement = text("""INSERT INTO mydb.user(username,full_name, email,phone_number,report_access,view_costs,last_login_date,enabled,is_corporated,
                                 created_on,modified_on) VALUES(:username,:full_name,:email,:phone_number,:report_access,:view_costs,:last_login_date,:enabled,
                                 :is_corporated,:created_on,:modified_on)""")
                conn.execute(statement,user.__dict__)
                conn.commit()
                               
            return jsonify({'status': 200,'message': 'User created successfully!'}), 200
    except Exception as error:
        # import pdb
        # pdb.set_trace()
        return jsonify({'status': 400,'message': str(error.orig)}), 400

def updatedata(user_id):

    try:
        user = User.query.get(user_id)
        sqlStr = ""
        if user is None:
            return jsonify({'status': 404, 'message': 'User not found!'}), 404
        if "username" in request.json:
            user.username = request.json.get('username')
            sqlStr += "username=:username"
        if "full_name" in request.json:
            user.full_name = request.json.get('full_name')
            sqlStr += ", full_name=:full_name"
        if "email" in request.json:
            user.email = request.json.get('email')
            sqlStr += ", email=:email"
        if "phone_number" in request.json:
            user.phone_number = request.json.get('phone_number')
            sqlStr += ", phone_number=:phone_number"
        if "report_access" in request.json:
            user.report_access = request.json.get('report_access')
            sqlStr += ", report_access=:report_access"
        if "view_costs" in request.json:
            user.view_costs = request.json.get('view_costs')
            sqlStr += ", view_costs=:view_costs"
        if "last_login_date" in request.json:
            user.last_login_date = request.json.get('last_login_date')
            sqlStr += ", last_login_date=:last_login_date"
        if "enabled" in request.json:
            user.enabled = request.json.get('enabled')
            sqlStr += ", enabled=:enabled"
        if "is_corporated" in request.json:
            user.is_corporated = request.json.get('is_corporated')
            sqlStr += ", is_corporated=:is_corporated"
        if "created_on" in request.json:
            user.created_on = request.json.get('created_on')
            sqlStr += ", created_on=:created_on"
        if "modified_on" in request.json:
            user.modified_on = request.json.get('modified_on')
            sqlStr += ", modified_on=:modified_on"
            
        if 'nativequery' not in request.path:
            db.session.commit()
            return jsonify({'status': 200,'message': 'User updated successfully'}), 200
        else:
            with db.engine.connect() as conn:
                sqlStr = "UPDATE mydb.user set " + sqlStr + " WHERE id =:id"
                # import pdb
                # pdb.set_trace()
                statement = text(sqlStr)
                conn.execute(statement,user.__dict__)
                conn.commit()
            return jsonify({'status': 200,'message': 'User updated successfully'}), 200
    
    except Exception as error:
        return jsonify({'status': 400, 'message': str(error.orig)}), 400