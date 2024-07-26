from flask import Flask
from flask import request
from flask import jsonify
import asyncio
import time

app = Flask("Minimal Rate Limiter")

@app.route("/streamer", methods=["GET"])
def streaming_api():
	def generate():
		for x in range(5):
			time.sleep(0.5)
			yield "\nTime elapsed: " + str(x)
	return app.response_class(generate())

@app.route('/limited', methods=['GET'])
def rate_limited():
	return jsonify({"ip": request.remote_addr})

@app.route("/unlimited", methods=["GET"])
def unlimited():
	return "No rate-limiting on this API.\n"

if __name__ == '__main__':
	app.run(debug=True)