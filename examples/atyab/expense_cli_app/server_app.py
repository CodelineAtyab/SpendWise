import subprocess

res = subprocess.run(["python", "main_app.py", "view-amount"], capture_output=True, text=True)
print(res.stdout)