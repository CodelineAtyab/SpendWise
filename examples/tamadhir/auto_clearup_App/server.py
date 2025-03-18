from flask import Flask, jsonify
from auto_clearup import organize_files, archive_old_files, delete_old_archives

app = Flask(__name__)

@app.route('/organize', methods=['POST'])
def organize():
    message, status = organize_files()
    return jsonify({"message": message}), status

@app.route('/archive', methods=['POST'])
def archive():
    message, status = archive_old_files()
    return jsonify({"message": message}), status

@app.route('/delete_archives', methods=['POST'])
def delete_archives():
    message, status = delete_old_archives()
    return jsonify({"message": message}), status

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5001)  # Specify the port here