import json
from flask import Blueprint, request, Response, jsonify
from controllers import UserController
from config.database import db
from models.User import user
from flask import abort
from utils.response import build_response
from werkzeug.exceptions import HTTPException

user_route = Blueprint('UserRoutes', __name__, url_prefix="/user")
UserController = UserController()

@user_route.route("/fetch", methods=["GET"])
def fetch_user():
   try:
      page = request.args.get('page')
      if page is None:
         return build_response(400, "missing query parameter page", None)

      response = UserController.fetch_data(page)
      return response
   except Exception as e:
      return jsonify({"error": str(e)}), 500
      

@user_route.route("/", methods=["POST"])
def create_user():
   try:
      response = UserController.create()
      return response
   except Exception as e:
      return jsonify({"error": str(e)}), 500
      
      
@user_route.route("/", methods=["GET"])
def get_all():
       try:
          limit = request.args.get('limit', default=10, type=int)
          page = request.args.get('page', default=1, type=int)
          response = UserController.get_all(limit,page)
          return response
       except Exception as e:
          return jsonify({"error": str(e)}), 500
       
@user_route.route("/<id>", methods=["GET"])
def find_by_id(id):
   try:
      response = UserController.findByID(id)
      return response
   except Exception as e:
      return jsonify({"error" : str(e)}), 500

@user_route.route("/", methods=["PUT"])
def update_user():
   try:
      response = UserController.update()
      return response
   except Exception as e:
      return jsonify({"error": str(e)}), 500
   
@user_route.route("/", methods=["DELETE"])
def delete_user():
   try:
      response = UserController.delete()
      return response
   except Exception as e:
      return jsonify({"error": str(e)}), 500
