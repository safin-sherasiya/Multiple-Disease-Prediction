from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load the models
working_dir = os.path.dirname(os.path.abspath(__file__))

heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')



@app.route('/heart', methods=['GET','POST'])

def heart():
    heart_prediction = None
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['Sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        heart_prediction = heart_model.predict
        ([
            [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal
            ]
        ])
        
        if heart_prediction == 1:
            heart_prediction = "Positive"
            return render_template('heart.html', result=heart_prediction)
        else:
            heart_prediction = "Negative"
            return render_template('heart.html', result=heart_prediction)
    else:
        return render_template('heart.html', prediction=heart_prediction)
   
    
@app.route('/diabetes', methods=['GET','POST'])

def diabetes():
    diabetes_prediction = None
    if request.method == 'POST':
        Pregnancies = int(request.form['pregnancies'])
        Glucose = int(request.form['glucose'])
        BloodPressure = int(request.form['blood_pressure'])
        SkinThickness = int(request.form['skin_thickness'])
        Insulin = int(request.form['insulin_level'])
        BMI = float(request.form['bmi'])
        DiabetesPedigreeFunction = float(request.form['diabetes_pedigree'])
        Age = int(request.form['age'])
        
        diabetes_prediction = diabetes_model.predict
        ([
            [
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age
            ]
        ])
    
        if diabetes_prediction == 1:
            diabetes_prediction = "Positive"
            return render_template('diabetes.html', result=diabetes_prediction)
        else:
            diabetes_prediction = "Negative"
            return render_template('diabetes.html', result=diabetes_prediction)
    else:
        return render_template('diabetes.html', prediction=diabetes_prediction)


if __name__ == '__main__':
    app.run(debug=True)
