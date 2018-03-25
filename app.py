from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)
port = 8000

# to modify according to your ngrok address
baseUrl = 'https://1e7fc766.ngrok.io'

@app.route('/bass', methods=['POST'])
def get_bass():
  print(json.loads(request.get_data()))
  return jsonify(
    status=200,
    replies=[{
      'type': 'video',
      'content': baseUrl+'/bass/01',
    }, {
      'type': 'video',
      'content': baseUrl+'/bass/02',
    }, {
      'type': 'video',
      'content': baseUrl+'/bass/03',
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

instrument = 'drums'
@app.route('/'+instrument, methods=['POST'])
def get_bass():
  print(json.loads(request.get_data()))
  return jsonify(
    status=200,
    replies=[{
      'type': 'video',
      'content': baseUrl+'/'instrument'/01',
    }, {
      'type': 'video',
      'content': baseUrl+'/'+instrument+'/02',
    }, {
      'type': 'video',
      'content': baseUrl+'/'+instrument+'/03',
    }],
    conversation={
      'memory': { 'key': 'value' }
    }
  )
@app.route('/'+instrument+'/01', methods=['GET'])
def get_bass_1():
    filename = 'samples/'+instrument+'/drum_01_94bpm.mp3'
    return send_file(filename, mimetype='audio/mpeg')

@app.route('/'+instrument+'/02', methods=['GET'])
def get_drums_2():
    filename = 'samples/'+instrument+'/drum_02_96bpm.mp3'
    return send_file(filename, mimetype='audio/mpeg')

@app.route('/'+instrument+'/03', methods=['GET'])
def get_drums_3():
    filename = 'samples/'+instrument+'/drum_03_97bpm.mp3'
    return send_file(filename, mimetype='audio/mpeg')

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
