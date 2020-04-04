from app import create_app
from app.models import User, Helper, Service

app = create_app()

"""
The following function  creates a shell context that adds the
database instance and models to the shell session. Which means that they
will be imported by default when "flask shell" is started. Useful for debugging
in interactive shell
"""


@app.shell_context_processor
def make_shell_context():
    return {'User': User, 'Helper': Helper, 'Service': Service}
