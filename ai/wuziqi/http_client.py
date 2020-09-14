from flask import Flask, request, jsonify, render_template
from config import *
from common import *
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
    board_id = str(uuid.uuid1()).replace('-', '')

    board = Board(player_color=PieceColor.parse(param['player_type']))
    db[board_id] = board

    resp = {
        'board_id': board_id
    }
    if not board.player_color == BLACK:
        row, col = 7, 7
        board.put(row, col, WHITE)
        resp['row'] = row
        resp['col'] = col
    return jsonify(resp)

@app.route('/put', methods=['POST'])
def put():
    param = request.form

    board_id = param['board_id']
    player_row = int(param['row'])
    player_col = int(param['col'])

    board = db[board_id]

    status, ai_row, ai_col = board.proceed(player_row, player_col)

    resp = {
        'status': status,
        'row': ai_row,
        'col': ai_col
    }
    return jsonify(resp)

app.run()