from json import dumps, loads
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

class CreateUserRequest(Schema):
    email = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    avatar = fields.String(required=True)
    
class UpdateUserRequest(Schema):
    id = fields.Integer(required=True)
    email = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    avatar = fields.String(required=True)