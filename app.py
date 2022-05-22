from flask import Flask, render_template, request
import heart_disease


app = Flask(__name__)

@app.route("/")

def homepage():
    return render_template("home.html")

@app.route("/index", methods=['GET', 'POST'])

def hello():
    mp=0
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        inputs = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        prediction = heart_disease.disease_prediction(inputs)
        mp = prediction

    return render_template("index.html", pred=mp)

            
if __name__ == "__main__":
    app.run(debug=True)