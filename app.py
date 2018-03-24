from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)
port = 8000

@app.route('/', methods=['POST'])
def index():
  print(json.loads(request.get_data()))
  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Roger that',
    }],
    conversation={
      'memory': { 'key': 'value' }
    }
  )

@app.route('/bass/01', methods=['GET'])
def get_bass_1():
    filename = 'samples/bass/bass_01_140bpm.mp3'
    return send_file(filename, mimetype='audio/mpeg')

@app.route('/bass/02', methods=['GET'])
def get_bass_2():
    filename = 'samples/bass/bass_02_140bpm.mp3'
    return send_file(filename, mimetype='audio/mpeg')

@app.route('/bass/03', methods=['GET'])
def get_bass_3():
    filename = 'samples/bass/bass_03_140bpm.mp3'
    return send_file(filename, mimetype='audio/mpeg')


@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
