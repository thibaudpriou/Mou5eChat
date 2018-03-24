from flask import Flask, request, jsonify
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

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
