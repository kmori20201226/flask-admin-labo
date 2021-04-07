"""flask-admin の拡張についての実験
flask-admin を使って master/detail 型のマスタメンテナンスを実現する
STEP1: 部署リストに行アクションとして従業員一覧表示ボタンを追加
"""

from flask import Flask, url_for, redirect
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.template import TemplateLinkRowAction
from model import (
    Department,
    Employee,
    create_session
)
from sqlalchemy import func

app = Flask(__name__)

# テーマ切り替え https://bootswatch.com/
app.config['FLASK_ADMIN_SWATCH'] = 'United'
# データを更新する際に必要なキー
app.secret_key = 'XH[chp??0hfdklxhQddsx'

admin = Admin(
    app,
    name='Flask-admin laboratory',
    template_mode='bootstrap4',
)

session = create_session()

class DepartmentModelView(ModelView):
    "部署マスタビュー"
    list_template = "master_list.html"  # 従業員リストを表示するボタン用
    column_extra_row_actions = [  # Add a new action button
        TemplateLinkRowAction("utils.employee_button", "Detail"),
    ]
    def __init__(self, session):
        super(DepartmentModelView, self).__init__(Department, session)

class EmployeeModelView(ModelView):
    "従業員マスタビュー"

    column_exclude_list = ['department']    # 一覧表示から部署のカラムを撤去
    form_excluded_columns = ['department']  # フォームから部署の欄を撤去

    def __init__(self, session):
        super(EmployeeModelView, self).__init__(Employee, session,
                                                menu_class_name='d-none')

    @expose("/<department_id>", methods=("GET",))
    def view(self, department_id):
        """新設した詳細表示ボタンが押されたときここに入る
        department_id には部署の表示行にhiddenフィールドに入っている
        部署id が入る
        """
        self.department_id = department_id
        return self.index_view()

    def get_query(self):
        "部署IDでフィルタをかけたクエリを行う（行表示用）"
        return self.session.query(Employee) \
                    .filter(Employee.department_id == self.department_id) \
                    .order_by(Employee.first_name,
                              Employee.last_name,
                    )
    
    def get_count_query(self):
        "部署IDでフィルタをかけたクエリを行う（件数表示用）"
        return self.session.query(func.count('*')) \
                    .select_from(Employee) \
                    .filter(Employee.department_id == self.department_id)

    def on_model_change(self, form, model, is_created):
        "モデルの更新(登録)直前に呼び出す"
        model.department_id = self.department_id

admin.add_view(DepartmentModelView(session))
admin.add_view(EmployeeModelView(session))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
