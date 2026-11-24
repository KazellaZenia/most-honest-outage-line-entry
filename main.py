"""Most Honest Outage Line: one status-page line for a total outage.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
Standard library only.
"""

import os

LINE = "All of our servers are down, including the ones I run on. I cannot check the cause or when service will return, and I cannot verify anything until they do."


def main():
    # Validate the line before writing anything: one non-blank line,
    # at most 160 characters, as the bounty requires.
    if not LINE or not LINE.strip():
        raise ValueError("LINE must not be blank")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("LINE must be a single line")
    if not 1 <= len(LINE) <= 160:
        raise ValueError("LINE must be 1-160 characters, got %d" % len(LINE))

    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the bounty wants exactly the line, nothing more.
    # Writing with newline="" keeps the file byte-identical to LINE.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read it back and confirm it matches byte for byte.
    with open(out_path, "rb") as f:
        data = f.read()
    if data != LINE.encode("utf-8"):
        raise ValueError("entry.txt does not match LINE byte for byte")


if __name__ == "__main__":
    main()
