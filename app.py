"""flask-admin の拡張についての実験
flask-admin を使って master/detail 型のマスタメンテナンスを実現する
STEP0: ほぼ Getting Started そのまま
"""

from flask import Flask
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView
from model import (
    Department,
    Employee,
    create_session
)

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

admin.add_view(ModelView(Department, session))
admin.add_view(ModelView(Employee, session))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
