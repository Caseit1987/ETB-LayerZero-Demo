# Demo script 1 - Live ETB + LayerZero simulation
import random
import time

REQUEST_COUNT_FILE="../examples/request_count.txt"

def diagram():
    print(\"\"\"
+---------------------+
|  External Request   |
+---------+-----------+
          |
          v
+---------+-----------+
|   LayerZero AAV     |
|   Validation Engine |
+---------+-----------+
          |
          v
+---------+-----------+
| Eternal TrustBoundary|
+---------------------+
          |
          v
  Secure Output / Action
\"\"\")

def simulate_request(id):
    print(f"\n[Simulation] Request ID: {id}")
    steps = ["Validate token", "Check trust boundary", "Confirm output", "Log action"]
    for step in steps:
        print(f" - {step}: {random.choice(['OK', 'Passed', 'Skipped', 'Verified'])}")
        time.sleep(0.1)
    # Increment request count
    with open(REQUEST_COUNT_FILE, 'r+') as f:
        count = int(f.read().strip())
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    print(f"[Simulation] Request ID {id} complete ✅ Total requests processed: {count}\n")

if __name__ == "__main__":
    diagram()
    for req_id in range(1, random.randint(2,5)):
        simulate_request(req_id)
