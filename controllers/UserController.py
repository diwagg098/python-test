from config.configuration import Configuration
from config.database import db
from flask import request
from models.User import user
from utils.response import build_response, build_response_pagination
from request.validation_request import CreateUserRequest, UpdateUserRequest
import requests
from typing import List
from datetime import datetime

configuration = Configuration()
class UserController(object):
      def __init__(self, **kwargs):
          pass
      def create(self):
        try:
          body = request.get_json()
          schema = CreateUserRequest()
          
          validation = schema.load(body)
          new_user = user(
            email=body['email'],
            first_name=body['first_name'],
            last_name=body['last_name'],
            avatar=None
          )
          db.session.add(new_user)
          db.session.commit()
          
          result = {key: getattr(new_user, key) for key in ['id', 'first_name', 'last_name', 'email', 'avatar', 'created_at', 'updated_at']}
          
          return build_response(status=200, message="User successfully created", data=result)
        except Exception as e:
          return build_response(400, str(e), None)
        
      def update(self):
        try:
          body = request.get_json()
          schema = UpdateUserRequest()
            
          validation = schema.load(body)
          findId = user.query.filter(user.id == body['id'], user.deleted_at == None).first()
          if findId is None:
            update = user.query.filter(user.id == body['id'], user.deleted_at == None).update({
              "first_name" : body["first_name"],
              "last_name": body["last_name"],
              "email" : body["email"],
              "avatar": body["avatar"]
            })
            db.session.commit()
            res = build_response(400, "User not found", None)

          res = build_response(200, "user successfully updated", body)
          return res
        except Exception as e:
          raise [{"msg":"error "+e}]
          
      def get_all(self, limit,page):
          try:
            data = user.query.filter(user.deleted_at == None).paginate(page=page, per_page=limit, error_out=False)
            count = user.query.count()
            data_list = [
              {
                "email" : item.email,
                "first_name" : item.first_name,
                "last_name" : item.last_name,
                "avatar" : item.avatar,
                "created_at" : item.created_at,
                "updated_at": item.updated_at,
                "deleted_at": item.deleted_at
              } for item in data]
            
            res = build_response_pagination(
              status=200,
              message="success",
              data=data_list,
              page=page,
              per_page=limit,
              count=count
            )

            return res
          except Exception as e:
              raise [{"msg":"error "+e}]
            
      def findByID(self, id):
        try:
          query = user.query.filter(user.id == id, user.deleted_at == None).first()
          if query:
            data = {key: getattr(query, key) for key in ['id', 'first_name', 'last_name', 'email', 'avatar', 'created_at', 'updated_at']}
            res = build_response(
              status=200,
              message="success",
              data=data
            )
            
            return res
        
        
          res = build_response(
            status=404,
            message="user not found",
            data=None
          )
          return res
        except Exception as e:
          raise {"msg": "error " + e}
        
      def delete(self):
        try:
          body = request.get_json()
          check_user = user.query.filter(user.id == body['id'], user.deleted_at == None).first()
          if check_user:
            delete = user.query.filter(user.id == body['id'], user.deleted_at == None).update({
              "deleted_at": datetime.now()
            })
            db.session.commit()
            res = build_response(
              status=200,
              message="user successfully deleted",
              data=None
            )
            return res
  
          res = build_response(400, "user not found", None)
          return res
        except Exception as e:
          raise {"msg": "error " + e}
          
        
      def fetch_data(self, page):
        api_url = f"https://reqres.in/api/users?page={page}"
        
        api_response = requests.get(api_url)
        
        data: List = []
        
        if api_response.status_code == 200:
          user_data = api_response.json()
          for item in user_data['data']:
            # check duplicate id
            check_duplicate = user.query.filter(user.id==item['id']).first()
            if check_duplicate is None:
              new_user = user(
                email=item['email'],
                first_name=item['first_name'],
                last_name=item['last_name'],
                avatar=item['avatar']
              )

              db.session.add(new_user)
              db.session.commit()
              
              data.append(item)
              
        count_data = len(data)
        return build_response(
          status=200,
          message=f"{count_data} successfully stored",
          data=data
        )
        
        