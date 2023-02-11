from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

user_m2m_task = Table('user_m2m_task', Base.metadata,
                    Column('user_id', String(50), ForeignKey('User.id')),
                    Column('task_id', String(50), ForeignKey('Task.id')),
                    )

class User(Base):
    __tablename__ = "User"
    id = Column(String(50), unique=True, primary_key=True)
    task_id = relationship(
        'Task', secondary=user_m2m_task, backref=backref('User'))

class Task(Base):
    __tablename__ = 'Task'
    id = Column(String(50), unique=True, primary_key=True)