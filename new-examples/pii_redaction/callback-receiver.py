from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Save all non-file fields in the form to the console
    for key, value in request.form.items():
        print(f"{key}: {value}")
    
    # Save any files included in the form
    for key in request.files:
        file = request.files[key]

        if file.filename == '':
            print(f"No file selected for {key}.")
            continue

        save_path = os.path.join("../data/callback", file.filename)
        file.save(save_path)

    return 'Data received and files (if any) have been uploaded!', 200

if __name__ == "__main__":
    app.run(port=8888, debug=True)
