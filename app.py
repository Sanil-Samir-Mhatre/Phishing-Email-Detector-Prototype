#Sanil Samir Mhatre 
from flask import Flask, render_template, request
import os
from email_parser import parse_email
from phishing_detector import detect_phishing

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")
@app.route('/upload', methods=['POST'])
def upload_email():
    if 'email_file' not in request.files:
        return "No file uploaded", 400

    file = request.files['email_file']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded file
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Parse the email
    email_data = parse_email(file_path)  # Correctly call the parse_email function

    # Analyze the email content for phishing
    flags = detect_phishing(email_data["Content"])  # Access "Content" from the parsed data

    # Render the results page with parsed email and flags
    return render_template("results.html", email=email_data, flags=flags)


if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)
