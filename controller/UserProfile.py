from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response
from service.ApplicationService import ApplicationService

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



