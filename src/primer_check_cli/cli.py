import argparse
from primer_check_cli.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI focused on primer inventory, length sanity checks, and review reports.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
