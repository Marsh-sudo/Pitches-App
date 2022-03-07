from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db
import app
from models import Pitch, User

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User,Pitch = Pitch)
if __name__ == '__main__':
    manager.run()