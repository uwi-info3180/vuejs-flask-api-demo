from app import app, db
from flask import jsonify, request, g, send_from_directory, url_for
from .models import User, Article
import jwt
from datetime import datetime, timedelta
from functools import wraps
from time import time
import os

# Create a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None)

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/v1/todos")
def todos():
    todos = [
        { "id": 1, "title": "Item 1" },
        { "id": 2, "title": "Item 2" },
        { "id": 3, "title": "Item 3" },
    ]

    return jsonify(todos=todos)


@app.route("/api/v1/todos", methods=['POST'])
def store():
    todos = [
        { "id": 1, "title": "Item 1" },
        { "id": 2, "title": "Item 2" },
        { "id": 3, "title": "Item 3" },
    ]
    todos.append({ "id": 4, "title": request.form["todo"] })

    return jsonify(todos=todos)

@app.route("/api/v1/articles", methods=['GET', 'POST'])
@requires_auth
def articles():
    articles = db.session.execute(db.select(Article)).scalars()
    article_data = []
    for article in articles:
        article_data.append({
           "id": article.id,
           "title": article.title,
           "photo": url_for('getImage', filename=article.photo)
        })
        # article_data.append(article.serialize())

    return jsonify(data=article_data)

@app.route("/api/v1/articles/<int:id>", methods=['GET'])
def article(id):
    article = db.session.execute(db.select(Article).filter_by(id=id)).scalar()

    return jsonify(data=article.serialize())

@app.route("/api/v1/users", methods=['GET', 'POST'])
def users():
    users = db.session.execute(db.select(User)).scalars()

    user_data = []
    for user in users:
        # user_data.append({"id": user.id, "username": user.username })
        user_data.append(user.serialize())

    return jsonify(data=user_data)


@app.route("/api/v1/users/<int:id>", methods=['GET'])
def user(id):
    user = db.session.execute(db.select(User).filter_by(id=id)).scalar()

    return jsonify(data=user.serialize())

@app.route("/api/v1/generate-token")
def generate_token():
    timestamp = datetime.utcnow()
    payload = {
        "sub": 1,
        "iat": timestamp,
        "exp": timestamp + timedelta(minutes=3)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify(token=token)


@app.route("/api/v1/images/<path:filename>")
def getImage(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)