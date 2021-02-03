from main import db, dt
import uuid


class Application(db.Model):
    __tablename__ = 'application'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    require_confirmation = db.Column(db.Boolean, default=False)
    token = db.Column(db.String(8), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.String(20))


    @staticmethod
    def create(name):
        app = Application()
        app.name = name
        app.created = str(int(dt.now().timestamp()))
        app.token = str(uuid.uuid4())[:8]
        return app