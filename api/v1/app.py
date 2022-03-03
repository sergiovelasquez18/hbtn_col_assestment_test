#!/usr/bin/python3
"""flask server"""
from api.v1.views import login, posts, users
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_mysqldb import MySQL
from os import environ



app = Flask(__name__)

app.include_router(login.router, tags=["login"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:amps3300@localhost/orders'

mysql = MySQL(app)

@app.get("/")
async def index():
    return {'message': 'active'}

@app.errorhandler(404)
def not_found(error):
    """ 404 Not Found"""
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == '__main__':
        db.create_all()
        app.run(port=5000, threaded=True, debug=True)
