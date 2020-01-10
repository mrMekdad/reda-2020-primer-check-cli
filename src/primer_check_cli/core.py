"""Core workflow for Primer Check CLI by Red@."""

PROJECT_NAME = "Primer Check CLI"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": "bioinformatics"}
