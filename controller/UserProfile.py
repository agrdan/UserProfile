from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response
from service.ApplicationService import ApplicationService
from service.UserService import UserService

users = Blueprint('users', __name__)


@users.route('/registration', methods=['POST'])
def userRegistration():
    if request.method == 'POST':
        user = request.json
        return UserService.create(user)


@users.route('/update/<id>', methods=['PUT'])
def updateUser(id):
    token = request.headers.get('auth-token')
    status, response = UserService.updateUser(token, id, request.json)
    return response


@users.route('/users', methods=['GET'])
def getAllUsers():
    token = request.headers.get('auth-token')
    status, response = UserService.getAllUsers(token)
    return response

@users.route('/users/<id>', methods=['GET'])
def getUserByID(id):
    token = request.headers.get('auth-token')
    status, response = UserService.getUserById(token, id)
    return response

@users.route('/password-change/<id>', methods=['PATCH'])
def changeUserPassword(id):
    token = request.headers.get('auth-token')
    password = request.args.get('password')
    status, response = UserService.changeUserPasword(token, id, password)
    return response

@users.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        login = request.json
        status, response = UserService.login(login)
        return response



