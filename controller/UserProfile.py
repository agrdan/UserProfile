from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response, send_file
from service.ApplicationService import ApplicationService
from service.UserService import UserService

users = Blueprint('users', __name__)

@users.route('/create-application', methods=['POST'])
def createApplication():
    if request.method == 'POST':
        name = request.args['appName']
        return ApplicationService.createApplication(name)



@users.route('/application/<string:name>', methods=['GET'])
def getApplication(name):
    if request.method == 'GET':
        return ApplicationService.getAppByName(name)


@users.route('/token', methods=['GET'])
def getApplicationByToken():
    if request.method == 'GET':
        token = request.args['token']
        return ApplicationService.getAppByToken(token)



@users.route('/registration', methods=['POST'])
def userRegistration():
    if request.method == 'POST':
        user = request.json
        return UserService.create(user)



@users.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        login = request.json
        status, response = UserService.login(login)
        return response
    

@users.route("/", methods=['GET'])
def getAllUsers():
    return UserService.getAllUsers()


@users.route("/get-mqtt-client", methods=['GET'])
def getMqttClient():
    path = "mqtt.txt"
    return send_file(path, as_attachment=True)
