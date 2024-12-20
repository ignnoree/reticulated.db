from flask import request, render_template,jsonify

from cs50 import SQL
import os
from app.bots import get_schema

from flask import Blueprint, render_template



bp = Blueprint('getschema', __name__)




@bp.route('/getschema', methods=['GET','POST'])
def get_data():
    if request.method=='POST':
       
        key=request.form.get('key')
        if  key :
            db=SQL('sqlite:///reticulated.db')
            db_path=db.execute('select database_path from reti_databases where database_key = ?',key)[0]['database_path']
            if db_path:
                result=get_schema(db_path)
                return jsonify({
                    "schema":result
                })
            else:
                return jsonify({
                    "msg":"key or email invalid"
                })
        else:
            return jsonify({
                "msg":"key and email required"})
    return render_template('getschema.html')