from app.models.database_model import User
from app.postgres_db.session_maker import session_maker

def create_user(user_id: str):
    try:
        session = session_maker()
        new_user = User(id=user_id)
        session.add(new_user)
        session.commit()
        return True
    except:
        session.rollback()
        return False
    