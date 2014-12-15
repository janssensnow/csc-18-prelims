from flask import Flask, render_template, request
from tallier.score import Score

app = Flask(__name__)
SCORE = Score ()

@app.route('/')
def hello_world():
  return render_template ('index.html')

if __name__ == '__main__':
  app.run(debug=True)