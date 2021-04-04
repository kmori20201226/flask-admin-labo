# coding: utf-8
"""flask-admin-labo 用のモデル
"""
import os

from sqlalchemy import Boolean, CHAR, Column, Date, DateTime, Float, ForeignKey, Integer, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
metadata = Base.metadata

def session():
    databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flask-admin-labo.db')
    engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
    sess = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
    _init_db(sess)
    return sess

def _init_db(sess):
    try:
        rs = sess.query(Department).all()
    except Exception as ex:
        model.metadata.create_all(bind=engine)


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True, comment='部署名')
    description = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime)

    def __repr__(self):
        return self.name

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(64), nullable=False, comment='名前')
    last_name = Column(String(64), nullable=False, comment='苗字')
    department_id = Column(ForeignKey('department.id', ondelete='SET NULL', onupdate='CASCADE'))
    gender = Column(String(1), nullable=True, comment='性別')
    birth_date = Column(Date, nullable=True, comment="生年月日")
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime)

    department = relationship('Department')

    def __repr__(self):
        return "%s, %s" % (last_name, first_name)
