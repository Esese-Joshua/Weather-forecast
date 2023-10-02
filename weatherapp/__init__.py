from flask import Flask

def create_app():  
    """keep all imports that may cause conflict within this function so that anytime we write "from fapp.. import.. none of these import statement will be executed"""
    app=Flask(__name__,instance_relative_config=True)
   # from bookapp import config
    app.config.from_pyfile("config.py",silent=True) 
    return app

app = create_app()
from weatherapp import weather_routes


#Load the routes, forms, models (everything you will want to access any other place just by typing "from fapp import...")
