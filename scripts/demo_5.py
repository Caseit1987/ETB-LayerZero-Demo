# Demo script 5 - ETB + LayerZero ASCII flow
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
if __name__ == "__main__":
    print("Running safe demo script 5")
    diagram()
