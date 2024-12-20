
from flask import request, render_template, jsonify,send_file


from app.bots import find_key_path

from flask import Blueprint, render_template



bp = Blueprint('dawnload', __name__)




@bp.route('/download', methods=['GET','POST'])
def download_file():
    if request.method=='POST':
        key=request.form.get('key')

        filepath=find_key_path(key)
        print(f'ffff = {filepath}')
        if filepath:
            return send_file(filepath, as_attachment=True)
        else :
            return jsonify({"error":"key is not valid"}),400
    return render_template('key_form.html')