from flask import (
    Blueprint, request, jsonify
)
from library.errors import APIError
from library.models import Request, Book, User
from library.schemas import RequestSchema

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/requests', methods=['POST'])
def post_requests():
    email = request.json.get('email')
    title = request.json.get('title')

    user = User.query.filter_by(email=email).first()
    if not user:
        raise APIError('Permission Denied', 401)
    book = Book.query.filter_by(title=title).first()
    if not book:
        raise APIError('Book does not exist', 401)

    _request = Request.create(book_id=book.id, user_id=user.id)

    return RequestSchema().jsonify(_request), 201


@api_bp.route('/requests/<int:id>', methods=['GET'])
def get_request(id):
    _request = Request.query.get(id)
    if not _request:
        return RequestSchema(many=True).jsonify(Request.query.all()), 201
    return RequestSchema().jsonify(_request), 201


@api_bp.route('/requests/<int:id>', methods=['DELETE'])
def delete_request(id):
    _request = Request.query.get(id)
    if not _request:
        raise APIError('Request does not exist', 401)
    Request.delete(_request)
    return jsonify({}), 201
