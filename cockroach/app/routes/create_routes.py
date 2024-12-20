from flask import  request, render_template, jsonify

from app.bots import create_rety_tables
from flask import Blueprint, render_template




bp = Blueprint('create_tables', __name__)

@bp.route('/create',methods=['POST','GET'])
def createtables():
    if request.method=='POST':
        key=request.form.get('key')
        userinput=request.form.get('input')
        result=create_rety_tables(userinput, key=key)
        if result:
            return jsonify({"msg":"succsessfull",
                            "msg":result})
        else :
            return jsonify({"error":" key is not valid !"})
    return render_template('create.html')