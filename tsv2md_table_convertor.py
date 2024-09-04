"""
    Creates markdown table from tsv-file (ex. exported from LO calc)
"""

import sys
import os.path
from typing import List


def md_format_string(words: List[str]) -> str:
    return "| " + " | ".join(words) + " |"


def convert_tsv_md(tsv_filename: str, md_filename: str, sep: str = '\t'):
    is_header_written = False
    with open(tsv_filename, 'r') as f, open(md_filename, 'w') as g:
        for line in f:
            line = line.rstrip()
            if not line:
                continue
            words = line.split(sep)
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
        print("tsv2md_table_convertor <filename> [<separator>]")
        sys.exit()

    input_filename = sys.argv[1]
    sep = sys.argv[2] if len(sys.argv) > 2 else '\t'
    if sep == ' ':
        sep = None
    output_filename = _get_output_filename(input_filename)
    convert_tsv_md(input_filename, output_filename, sep)


if __name__ == "__main__":
    main()
