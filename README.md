## Fast composer chatbot

### Installation
* Install python 2.7
* Install pip
* Then install flask
```
pip install flask
```

### Running the server on the local machine
```
python app.py
```

## Create a tunnel to your server
To tunnel the requests made on Recast.AI, download (ngrok)[https://ngrok.com/download], unzip it and start a HTTP tunnel with:
```
./ngrok start 8000
```
Then retrieve the forwarding address (ex : 'https://43ec6d93.ngrok.io' ) and use this address on Recast.AI.
