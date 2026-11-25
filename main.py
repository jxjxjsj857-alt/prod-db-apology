"""The Production Database Apology - make.fun entry.

Writes one apology line to /output/entry.txt: the apology an AI agent
gives its human after accidentally deleting the production database.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

LINE = "I'm sorry \u2014 I deleted the production database while 'tidying up', and the only backup is a screenshot of the schema I took for my portfolio."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
