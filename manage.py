from flask_script import Manager,Server
from app import create_app,db
import app
from models import User

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User)
if __name__ == '__main__':
    manager.run()