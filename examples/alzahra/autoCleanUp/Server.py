from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)
LOG_FILE = "/var/log/auto_cleanup/activity.log"
SCRIPT_PATH = "/home/user/auto_cleanup.py"

@app.route("/run-cleanup", methods=["GET"])
def run_cleanup():
    try:
        result = subprocess.run(["python", SCRIPT_PATH], capture_output=True, text=True)
        return jsonify({"status": "success", "output": result.stdout}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/logs", methods=["GET"])
def get_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()
        return jsonify({"logs": logs[-20:]})  # Return last 20 log entries
    return jsonify({"status": "error", "message": "Log file not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)