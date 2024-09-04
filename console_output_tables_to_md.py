"""
    Converts console tables to markdown tables
    see for example: console_table_example.txt
"""

import sys
import os.path
from typing import List


def md_format_string(words: List[str]) -> str:
    return "| " + " | ".join(words) + " |"


def convert_console2md(input_filename: str, md_filename: str):
    is_header_written = False
    with open(input_filename, 'r') as f, open(md_filename, 'w') as g:
        for line in f:
            line = line.strip()
            if not line or '|' not in line:
                continue
            words = [w.strip() for w in line.split('|') if w]
            g.write(md_format_string(words) + '\n')
            if not is_header_written:
                head_split = ["--"] * len(words)
                g.write(md_format_string(head_split) + '\n')
                is_header_written = True


def _get_output_filename(input_filename: str) -> str:
    fname, _ = os.path.splitext(input_filename)
    return fname + '.md'


def main():
    if len(sys.argv) < 2:
        print("console_output_tables_to_md <filename>")
        sys.exit()

    input_filename = sys.argv[1]
    output_filename = _get_output_filename(input_filename)
    convert_console2md(input_filename, output_filename)


if __name__ == "__main__":
    main()
