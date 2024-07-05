from flask import *
import json
import os
app = Flask(__name__)

@app.route('/')
def home():
  #return "HOSTNAME: " + os.environ.get('HOSTNAME', "N/A")
  headers = list(request.headers)
  headers.append(["server-hostname", os.environ.get('HOSTNAME', "N/A")])
  return json.dumps(headers)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)
