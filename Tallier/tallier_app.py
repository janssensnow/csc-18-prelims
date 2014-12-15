from flask import Flask, render_template, request
from tallier.score import Score
from tallier.tallier import Tallier

app = Flask(__name__)
TALLIER = Tallier ()

@app.route('/')
def hello_world():
  return render_template ('index.html')

if __name__ == '__main__':
  app.run(debug=True)