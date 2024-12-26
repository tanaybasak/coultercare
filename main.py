import os
import eel

# Initialize Eel
try:
    eel.init('backend\www')
    print("Eel initialized successfully.")
except Exception as e:
    print(f"Error initializing Eel: {e}")

# Open the browser
try:
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    print("Browser launched successfully.")
except Exception as e:
    print(f"Error launching browser: {e}")

# Start the server
try:
    eel.start("index.html", mode=None, host="localhost", port=8000, block=True)
    print("Eel started successfully.")
except Exception as e:
    print(f"Error starting Eel: {e}")
