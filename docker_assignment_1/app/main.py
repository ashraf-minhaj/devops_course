"""
 author : ashraf minhaj
 mail   : ashraf_minhaj@yahoo.com

 date: 22-11-2023
 simple flask app
"""

from flask import Flask

PORT = 80

# Flask constructor takes module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hey man, this is working on your machine too'

# main driver function
if __name__ == '__main__':
	app.run(debug=False, port=PORT, host="0.0.0.0")