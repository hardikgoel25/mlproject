import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    custom_data = CustomData(
        gender=data['gender'],
        race_ethnicity=data['race_ethnicity'],
        parental_level_of_education=data['parental_level_of_education'],
        lunch=data['lunch'],
        test_preparation_course=data['test_preparation_course'],
        reading_score=data['reading_score'],
        writing_score=data['writing_score']
    )
    pred_df = custom_data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return jsonify({'prediction': results[0]})

if __name__ == "__main__":
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
