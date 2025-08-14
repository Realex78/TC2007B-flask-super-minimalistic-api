from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
	return jsonify({"message": "something unique"})

if __name__ == "__main__":
	app.run(threaded=True, host='0.0.0.0', port=7878)
