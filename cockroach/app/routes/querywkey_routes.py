from flask import  request, render_template,  jsonify

from cs50 import SQL
from app.bots import sql_retrieve_bot


from flask import Blueprint, render_template



bp = Blueprint('query_w_key', __name__)




@bp.route('/query_withkey', methods=['GET', 'POST'])
def QUERY_with_key():
    if request.method=='POST':
        key=request.form.get('key')
        userinput=request.form.get('input')
        if key : 
            db=SQL('sqlite:///reticulated.db')
            try:
                db_path=db.execute('select database_path from reti_databases where database_key = ?',key)[0]['database_path']
            except Exception:
                return jsonify({"msg":"key is not valid"})
            print(f'inside 1 ={db_path}')
            if db_path:
                result=sql_retrieve_bot(userinput,db_path)
                return result
            #return jsonify({"error":"invalid key or email"})
        return jsonify({
            "error":"email and key required !"
        })

    return render_template('query2.html')