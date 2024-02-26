from flask import Blueprint, jsonify
from ..services.data_service import get_data

views = Blueprint('views', __name__)

@views.route('/index', methods=['GET'])
def index():
    data = get_data()
    return jsonify(data)
