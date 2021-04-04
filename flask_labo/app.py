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

# テーマ切り替え https://bootswatch.com/
app.config['FLASK_ADMIN_SWATCH'] = 'United'
# データを更新する際に必要なキー
app.secret_key = 'XH[chp??0hfdklxhQddsx'

admin = Admin(
    app,
    name='Flask-admin laboratory',
    #base_template='master.html',
    #template_mode='bootstrap4',
    #index_view=MyAdminIndexView()
)

session = model.session()

class DepartmentModelView(ModelView):
    column_labels = dict(
        name = "部署名",
        description = "部署情報",
        created_at = "作成日時",
        updated_at = "更新日時"
    )
    def __init__(self, session):
        super(DepartmentModelView, self).__init__(model.Department, session)

class EmployeeModelView(ModelView):
    column_labels = dict(
        first_name = "名前",
        last_name = "苗字",
        gender = "性別",
        birth_date = "生年月日",
        created_at = "作成日時",
        updated_at = "更新日時"
    )
    def __init__(self, session):
        super(EmployeeModelView, self).__init__(model.Employee, session)

admin.add_view(DepartmentModelView(session))
admin.add_view(EmployeeModelView(session))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
