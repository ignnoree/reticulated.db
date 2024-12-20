from flask import request, render_template, jsonify
from cs50 import SQL
import os

from app.bots import create_key,check_filename
from app.emailsend import create_email_verify_request
from flask import Blueprint, render_template
from flask_wtf import FlaskForm,RecaptchaField
from app.Config import Config


bp = Blueprint('getkey', __name__)



class MyForm(FlaskForm):
    
    recaptcha = RecaptchaField()



@bp.route('/getkey',methods=['POST','GET'])
def home():
    form=MyForm()
    if request.method=='POST':
        print(f' {form.validate_on_submit()}')
        if not form.validate_on_submit():
            return jsonify({"error": "Invalid reCAPTCHA"}), 400
        email=request.form.get('email')
        verification_code = request.form.get('verification_code')
        file=request.files['file']
        if email and not verification_code and not file:
            result=create_email_verify_request(email)
            return jsonify({"msg":result})
            

        elif email and verification_code and file:
            db=SQL('sqlite:///reticulated.db')
            verify_code=db.execute('select verification_code from email_verifications where email=? and verification_code = ?',email,verification_code)
            if verify_code:
                print(file.filename)
                cfilename=check_filename(file.filename)
                if cfilename:
                    key = create_key(50)
                    filename=f'{email}_{file.filename}'
                    
                    try:
                        db_path = os.path.join(Config.UPLOAD_FOLDER,filename)
                        file.save(db_path)
                        db.execute('insert into reti_databases (database_key,database_path,email)VALUES(?,?,?)',key,db_path,email)
                    except Exception as e:
                        print(e)

                    response = {
                
                    "msg": "Database inserted into the servers. You have 1 hour to make changes to your database, then download the edited version. It will be removed after 1 hour from servers.",
                    "key": key}
                    return jsonify(response)
                else:
                    return jsonify({"error": ".db file is required"})
            else:
                return jsonify({"msg":"verification code is wrong "})
       

    return render_template('getkey.html',form=form)
    