import sys

class Helpers:
    
    def multiline_input():
        print("Enter your text. Press Ctrl + D (Mac/Linux) / Ctrl + Z (Windows) to finish.")
        return sys.stdin.read()