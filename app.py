from flask import Flask, render_template, jsonify

app = Flask(__name__)

DATA = [
  {
    'id':1 ,
    'title':'data 1',
    'point':'pint 1',
    'color': 'red'
  },
  {
    'id':2 ,
    'title':'data 2',
    'point':'pint 2',
    'color': 'green'
  },
  {
    'id':3 ,
    'title':'data 3',
    'point':'pint 3',
    'color': 'red 3'
  },
  {
    'id':4 ,
    'title':'data 4',
    'point':'pint 4',
    'color': 'green 4'
  },
]

@app.route("/")
def hello_brandingtech():
  return render_template('home.html',
                         data=DATA)

@app.route("/api/data")
def list_data():
  return jsonify(DATA)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
