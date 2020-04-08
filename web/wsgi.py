"""
The webapp for site selectvity 
"""
from app import app, db

def build_app(*args, **kwargs):
    db.init_app(app)
    # if 'init_db' in kwargs:
    #     with app.app_context():
    #         db.init_db()
    #         print("-- INITIALIZED DATABASE --")
        
    app.config['DEMO'] = kwargs.get('demo', False)

    return app
    