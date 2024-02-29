from flask import Flask, request

app = Flask("Minimal Rate Limiter")

@app.route('/test', methods=['GET'])
def test_api():
	return 'Test API WAI :)\n'

if __name__ == '__main__':
	app.run(debug=True)