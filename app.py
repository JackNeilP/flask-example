from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return "Hello World"


@app.route('/a')
def goodbye_world():
	return "Goodbye"


@app.route('/hello/<name>')
def hello_name(name):
	return f"Hello {name}"


@app.route('/b')
def travis_check():
	return


if __name__ == '__main__':
	app.run()
