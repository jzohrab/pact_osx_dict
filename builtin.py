import sys
import subprocess

def lookup(word):
    args = ['open', f"dict://{word}"]
    subprocess.Popen(args)
    return None

if __name__ == '__main__':
    word = sys.argv[1]
    d = lookup(word)
    print('---')
    print(d)
