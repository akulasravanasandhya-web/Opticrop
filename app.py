from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    prediction = "Recommended Crop: Rice"

    return render_template(
        "index.html",
        prediction_text=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)
