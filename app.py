from flask import *
import json
import os
app = Flask(__name__)

@app.route('/')
def home():
  return "HOSTNAME: " + os.environ.get('HOSTNAME', "N/A")

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)