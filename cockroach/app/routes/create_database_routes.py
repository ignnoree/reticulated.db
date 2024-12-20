from flask import request, render_template, flash, jsonify
from app.emailsend import code_is_valid

from app.emailsend import create_email_verify_request


from flask import Blueprint, render_template

bp = Blueprint('createdb', __name__)


from .getkey_routes import MyForm

@bp.route('/createdatabase', methods=['GET', 'POST'])
def getkeys():
    form=MyForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            return jsonify({"error": "Invalid reCAPTCHA"}), 400
        email = request.form.get('email')
        verification_code = request.form.get('verification_code')
        if email and not verification_code:
            
            result=create_email_verify_request(email)
            return jsonify({"msg":result})
        
        
        elif email and verification_code:
            
            key=code_is_valid(email,verification_code)
            if key:

                return render_template('createdatabase.html',key=key,email=email)
                
            else:
                flash("Invalid verification code. Please try again.", "error")         

        else:
            flash("Email is required!", "error")
    return render_template('createdatabase.html',form=form)