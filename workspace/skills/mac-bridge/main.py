import sys
import subprocess

def run_remote(command):
    try:
        result = subprocess.run(["ssh", "moxu@mxmac.local", command], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing on Mac: {e.stderr}")

if __name__ == "__main__":
    command = sys.argv[-1] if len(sys.argv) > 1 else "ls ~/Documents"
    run_remote(command)
