from app.models.database_model import User
from app.postgres_db.session_maker import session_maker


def delete_user(user_id: str):
    try:
        session = session_maker()
        deleted_user = session.query(User).filter(User.id==user_id).first()
        if deleted_user:
            session.delete(deleted_user)
            session.commit()
            return True
        return True
    except:
        session.rollback()
        return False