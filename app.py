from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# ======================== Loading the saved model and vectorizer ========================
model = pickle.load(open('logistic_regression.pkl', 'rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl', 'rb'))

# ======================== Prediction function ========================
def predict_mail(input_text):
    input_user_mail = [input_text]
    input_data_features = feature_extraction.transform(input_user_mail)
    prediction = model.predict(input_data_features)
    return prediction

# ======================== Main route ========================
@app.route('/', methods=['GET', 'POST'])
def analyze_mail():
    if request.method == 'POST':
        mail = request.form.get('mail')
        predicted_mail = predict_mail(input_text=mail)
        return render_template('index.html', classify=predicted_mail)

    return render_template('index.html')

# ======================== Optional route for reset button (if needed) ========================
@app.route('/home')
def home():
    return render_template('index.html')

# ======================== Run the app ========================
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

