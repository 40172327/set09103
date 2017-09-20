from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
  return "hello napier"

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Could not find the page requested", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
