from flask import Flask, request, jsonify, render_template
from config import *
import uuid

from board import Board

app = Flask(__name__)


db = {}

@app.route('/')
def board():
    return render_template('board.html')

@app.route('/start', methods=['POST'])
def start():
    param = request.form
    player_type = int(param['player_type'])
    board_id = str(uuid.uuid1()).replace('-', '')
    db[board_id] = Board(player_type=player_type)
    resp = {
        'board_id': board_id
    }
    if player_type == WHITE_VALUE:
        resp['x'] = 1
        resp['y'] = 1
    return jsonify(resp)

@app.route('/put', methods=['POST'])
def put():
    param = request.form
    print(param)
    board_id = param['board_id']
    player_x = int(param['x'])
    player_y = int(param['y'])

    board = db[board_id]
    print(board)

    resp = {
        'x': player_x + 1,
        'y': player_y + 1
    }
    return jsonify(resp)

app.run()