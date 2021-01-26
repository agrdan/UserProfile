from main import db, dt



class Application(db.Model):
    __tablename__ = 'application'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    created = db.Column(db.String(20))



    @staticmethod
    def create(name):
        app = Application()
        app.name = name
        app.created = str(int(dt.now().timestamp()))
        return app