import os
basedir = os.path.abspath(os.path.dirname(__file__))
DB_CONFIG = 'sqlite:///' + os.path.join(basedir, 'Project_DB.db')