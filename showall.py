import glob
import subprocess


for path in sorted(glob.glob("*/*.py")):
    print(path)
    print("=" * len(path))

    print("code\n----")
    with open(path) as f:
        print(f.read())

    print("result\n------")
    subprocess.run(["python3.7", path])
    print("")
