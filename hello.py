# hello_world.py

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print(f"Hello, {name} from Python script running in Jenkins!")
    sys.exit(0) # Exit with success code
