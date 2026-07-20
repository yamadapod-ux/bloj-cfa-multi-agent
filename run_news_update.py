import subprocess, sys
result = subprocess.run([sys.executable, r"C:\Users\user\Desktop\บลจ\บลจ CFA\update_news.py"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
