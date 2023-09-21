from flask import jsonify

def build_response(status,message, data):
    response = {
        'status_code' : str(status),
        'message' : message,
        'data': data
    }
    return jsonify(response), status

def build_response_pagination(status,message, data, per_page, page, count):
    response = {
        'status_code' : str(status),
        'message' : message,
        'data': data,
        'pagination' : {
            'per_page' : per_page,
            'page': page,
            'count' : count
        }
    }
    return jsonify(response), status