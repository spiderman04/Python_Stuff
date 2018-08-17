"""
  A simple Hello World module
"""
import time

def hello_world():
	print('Hello World at ' + time.strftime('%x %I:%M:%S %Z'))


if __name__ == "__main__":
        hello_world()
else:
        print('hello_world.py is being imported into another module.')

