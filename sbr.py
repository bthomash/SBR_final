## Brian Herrick
## NYU DigitalForensics Spring 2019
## /SBR.py

from app import app, db
from app.models import User, Requests

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Requests': Requests}
