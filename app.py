from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecret'

def calculate_bmr(weight, height, age, gender, bfp, exercise_freq):
    def mifflin_st_jeor(w, h, a, g):
        return 66 + (6.23 * w) + (12.7 * h) - (6.8 * a) if g == 'male' else 655 + (4.35 * w) + (4.7 * h) - (4.7 * a)

    def harris_benedict(w, h, a, g):
        return 88.362 + (13.397 * w) + (4.799 * h) - (5.677 * a) if g == 'male' else 447.593 + (9.247 * w) + (3.098 * h) - (4.330 * a)

    def katch_mcardle(w, bfp):
        return 370 + (4.536 * (1 - bfp) * w)

    total = (
        mifflin_st_jeor(weight, height, age, gender) +
        harris_benedict(weight, height, age, gender) +
        katch_mcardle(weight, bfp)
    )
    base_bmr = total / 3
    multiplier = [1.2, 1.375, 1.55, 1.725, 1.9][exercise_freq - 1]
    return round(base_bmr), round(base_bmr * multiplier)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmr', methods=['GET', 'POST'])
def bmr():
    bmr = None
    adjusted_bmr = None

    if request.method == 'POST':
        weight = int(request.form['weight'])
        height_ft = int(request.form['height_ft'])
        height_in = int(request.form['height_in'])
        age = int(request.form['age'])
        gender = request.form['gender']
        exercise = int(request.form.get('exercise', 1))

        height_total = (height_ft * 12) + height_in
        bmi = (weight * 703) / (height_total ** 2)
        bfp = ((1.20 * bmi) + (0.23 * age) - (10.8 if gender == 'male' else 0) - 5.4) / 100

        bmr, adjusted_bmr = calculate_bmr(weight, height_total, age, gender, bfp, exercise)

    return render_template('bmr.html', bmr=bmr, adjusted_bmr=adjusted_bmr)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
