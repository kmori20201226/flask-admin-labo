"""flask-admin の拡張についての実験
flask-admin を使って master/detail 型のマスタメンテナンスを実現する
"""

import os
from datetime import datetime
from flask import Flask, url_for, render_template, redirect
from flask_admin import Admin, expose
from flask_admin.base import expose, AdminIndexView

from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.model.template import TemplateLinkRowAction
import model

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = 'XH[chp??0hfdklxhQddsx'

admin = Admin(
    app,
    name='Flask-admin laboratory',
    #base_template='master.html',
    #template_mode='bootstrap4',
    #index_view=MyAdminIndexView()
)

session = model.session()
admin.add_view(ModelView(model.Department, session))
admin.add_view(ModelView(model.Employee, session))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
