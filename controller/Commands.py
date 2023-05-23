from flask import request, jsonify, Blueprint
import json

commands = Blueprint('commands', __name__)

@commands.route('/list', methods=['GET'])
def getCommands():
    if request.method == 'GET':
        model = {
            "commands": ["iot/lights;on", "iot/lights;off", "iot/general;get"],
            "lightsOn": "iot/lights;on",
            "lightsOff": "iot/lights;off",
            "readInfo": "iot/general;get"
        }
        return json.dumps(model)