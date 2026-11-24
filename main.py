#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to /output/entry.txt.
"""
import os

JOKE = "I blocked focus time on my calendar to finally finish my work, and my boss booked over it to ask why I never finish anything."

def main() -> None:
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
