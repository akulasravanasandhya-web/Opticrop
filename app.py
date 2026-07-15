from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to OptiCrop</h1><p>Smart Agricultural Production Optimization Engine</p>"

if __name__ == "__main__":
    app.run(debug=True)
