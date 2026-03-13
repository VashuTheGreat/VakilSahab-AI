import subprocess
import json
import time

def test_stdio_server():
    print("Starting stdio server...")
    proc = subprocess.Popen(
        ["uv", "run", "api/mcp_server_stdio.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    # Give it a second to start
    time.sleep(2)

    # Check if process is still running
    if proc.poll() is not None:
        print("Server failed to start.")
        print("Stderr:", proc.stderr.read())
        return

    # Send Initialize request
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0.0"}
        }
    }
    
    print("\nSending 'initialize' request...")
    proc.stdin.write(json.dumps(init_request) + "\n")
    proc.stdin.flush()
    
    response = proc.stdout.readline()
    print("Response:", response)

    # Send Initialized notification
    init_notify = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    print("\nSending 'notifications/initialized' notification...")
    proc.stdin.write(json.dumps(init_notify) + "\n")
    proc.stdin.flush()

    # Send List Tools request with a cursor to test validation
    list_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {"cursor": None}
    }
    
    print("\nSending 'tools/list' request...")
    proc.stdin.write(json.dumps(list_request) + "\n")
    proc.stdin.flush()
    
    response = proc.stdout.readline()
    print("Response:", response)

    # Cleanup
    proc.terminate()

if __name__ == "__main__":
    test_stdio_server()
