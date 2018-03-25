from flask import Flask, request, jsonify, send_file
import json, audioop, wave

app = Flask(__name__)
port = 8000

# to modify according to your ngrok address
baseUrl = 'https://1e7fc766.ngrok.io'

class Deserializer(object):
  def __init__(self,j):
    self.__dict__=j


@app.route('/<instrument>/<int:sample_id>', methods=['GET'])
def get_sample(instrument, sample_id):
    filename = 'demo_samples/' + str(instrument) + '/' + str(instrument) + '_' + str(sample_id) + '.wav'
    return send_file(filename, mimetype='audio/x-wav')

@app.route('/<instrument>', methods=['POST'])
def get_sample_choices(instrument):
  # print(json.loads(request.get_data()))
  return jsonify(
    status=200,
    replies=[{
      'type': 'video',
      'content': baseUrl+'/'+ str(instrument) +'/1',
    }, {
      'type': 'video',
      'content': baseUrl+'/'+ str(instrument) +'/2',
    }, {
      'type': 'video',
      'content': baseUrl+'/'+ str(instrument) +'/3',
    }]
  )

@app.route('/preview', methods=['POST'])
def get_preview():
  data = request.get_data()
  payload = Deserializer(json.loads(data))
  conversation = Deserializer(payload.conversation)
  memory = Deserializer(conversation.memory)
  bass = None
  drums = None
  keys = None
  guitar = None

  if hasattr(memory, 'bass'):
    filename = 'demo_samples/bass/bass_' + str(memory.bass) + '.wav'
    bass = wave.open(filename, 'r')

  if hasattr(memory, 'drums'):
    filename = 'demo_samples/drums/drums_' + str(memory.drums) + '.wav'
    drums = wave.open(filename, 'r')

  if hasattr(memory, 'keys'):
    filename = 'demo_samples/keys/keys_' + str(memory.keys) + '.wav'
    keys = wave.open(filename, 'r')

  if hasattr(memory, 'guitar'):
    filename = 'demo_samples/guitar/guitar_' + str(memory.guitar) + '.wav'
    guitar = wave.open(filename, 'r')

  preview = None
  for instrument in [bass, drums, keys, guitar]:
    if (not instrument is None):
      if preview is None:
        preview = instrument
      else:
        # TODO merge audio with audioop
        # TODO WARNING : some samples are 4sec long, others 2sec long, duplicate the small ones before mixing
        # preview =
        foo = 'foo' #TODO remove this line, I wanted to test something, do not care


  # TODO write preview in a wav file ('wave.writeframesraw(preview)', I guess)
  # TODO save this file in a dedicated folder
  # TODO return an endpoint for Recast.AI
  # TODO do the same for the '/mix' endpoint, but with 4 times the samples (you could even make a 'drop' after 4 periods, or 8, 12, ...)

  return jsonify({

  })

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
