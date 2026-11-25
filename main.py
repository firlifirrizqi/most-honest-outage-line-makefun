"""Most Honest Outage Line — Make.fun entry (stdlib only).

Writes a single status page line, at most 160 characters, to
/output/entry.txt. That is the whole program.
"""

import os

LINE = (
    "All systems down. The status page is the only thing still up, "
    "so I cannot check anything behind it. "
    "No ETA \u2014 there is nothing to measure it with."
)


def verify(path: str = "/output/entry.txt") -> None:
    """Re-read the written file and assert the gate: 1-160 chars,
    not only whitespace, byte-identical to the chosen line."""
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == LINE, "entry.txt is not byte-identical to the chosen line"
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert text.strip(), "line must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    verify()


if __name__ == "__main__":
    main()
