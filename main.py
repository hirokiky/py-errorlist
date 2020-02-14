import csv
import subprocess
from pathlib import Path


def call(path: Path):
    with path.open() as f:
        c = f.read()
    proc = subprocess.run(["python", str(path)], capture_output=True)
    r = proc.stderr.decode()
    return c, r


def show(path: Path):
    p = str(path)
    print(p)
    print("=" * len(p))
    content, result = call(path)

    print("code\n----")
    print(content)

    print("result\n------")
    print(result)
    print("")


def showall(paths):
    for path in paths:
        showall(path)


def save_csv(paths):
    with open("./result.csv", mode="w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "ファイル", "コード", "実行結果",
        ])
        for path in paths:
            content, result = call(path)
            writer.writerow([str(path), content, result])


def main():
    save_csv(Path(".").glob("*/*.py"))


if __name__ == "__main__":
    main()
