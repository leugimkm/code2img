from urllib.parse import quote


def parse_str(s: str) -> str:
    return quote(s)


def read_file(path: str) -> str:
    data = []
    with open(path, "r") as f:
        return f.read()


def split_path(path: str) -> list:
    return path.split("/")[-1][:-3]

def job_done(filename: str) -> None:
    print("Done!")
    print(f"Image created in current directory: {filename}.png")
    print()