from flask import Flask, request,session, flash, url_for, make_response, redirect, abort, render_template
from flask.wrappers import Response
from flask_bootstrap import Bootstrap
from formularz import NameForm

import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "ksiadzwojciechcejrowski"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("entered /")
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name !=form.name.data:
            flash('Wygląda na to że nazywasz się inaczej')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',name=session.get('name'), form=form)

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()
    print(content)
    return uuid

print(app.url_map)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)