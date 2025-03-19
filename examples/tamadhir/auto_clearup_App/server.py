from flask import Flask, jsonify # Import the Flask class from the flask module

from auto_clearup import organize_files, archive_old_files, delete_old_archives

app = Flask(__name__)

@app.route('/organize', methods=['POST'])
def organize():
    message, status = organize_files()
    return jsonify({"Files Organaize Successfully": message}), status

@app.route('/archive', methods=['POST'])
def archive():
    message, status = archive_old_files()
    return jsonify({"Files archive Successfully": message}), status

@app.route('/delete_archives', methods=['POST'])
def delete_archives():
    message, status = delete_old_archives()
    return jsonify({"Files delete_archives Successfully": message}), status

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=5001, reload=True)  # Use uvicorn to run the app