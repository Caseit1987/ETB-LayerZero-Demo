# Demo script 3 - ETB + LayerZero simulated live checks
import random
import time

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
    print(f"[Simulation] Request ID {id} complete ✅\n")

if __name__ == "__main__":
    diagram()
    for req_id in range(1, random.randint(2,5)):
        simulate_request(req_id)
