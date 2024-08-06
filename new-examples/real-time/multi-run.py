import subprocess
import time

# Path to your Python script
script_path = "./rt-2chn-simulated-twiml-pcmu.py"

# Number of times you want to run the script
num_runs = 25

for i in range(num_runs):
    print(f"Launching script instance {i+1}")
    subprocess.Popen(["python", script_path])
    time.sleep(2)

print("All script instances launched.")
