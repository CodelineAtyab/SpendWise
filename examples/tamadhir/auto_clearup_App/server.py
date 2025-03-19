from flask import Flask, jsonify
from auto_clearup import organize_files, archive_old_files, delete_old_archives
from asgiref.wsgi import WsgiToAsgi  
# Initialize Flask app
app = Flask(__name__)

# Endpoint to organize files
@app.route('/organize', methods=['GET', 'POST'])
def organize():
    message, status = organize_files()
    return jsonify({"message": message}), status

# Endpoint to archive old files
@app.route('/archive', methods=['GET', 'POST'])
def archive():
    message, status = archive_old_files()
    return jsonify({"message": message}), status

# Endpoint to delete old archives
@app.route('/delete_archives', methods=['GET', 'POST'])
def delete_archives():
    message, status = delete_old_archives()
    return jsonify({"message": message}), status

# Wrap the Flask app with WSGI-to-ASGI adapter
asgi_app = WsgiToAsgi(app)

# Run the server using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=5001, reload=True)