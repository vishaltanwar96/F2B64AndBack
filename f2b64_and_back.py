import os
import sys
import base64
import argparse

import filetype

# Module Level Constants
EMPTY_FILE = 'EMPTY FILE'
FILE_NOT_FOUND = 'FILE NOT FOUND'


class F2B64AndBack(object):
    """
    Utility for Converting Files to Base64 Strings and Vice-Versa
    """

    @classmethod
    def from_file2b64(cls, file_path: str) -> None:
        """Convert File to Base64 String"""

        try:
            with open(file_path, 'rb') as f:
                file_data = f.read()
                if not file_data:
                    sys.exit(EMPTY_FILE)
                b64_data = base64.b64encode(file_data).decode()
        except Exception as exc:
            tc, te, tb = sys.exc_info()
            print(f'CLASS: {tc}, ERROR: {exc}, LINE_NO: {tb.tb_lineno}')
            b64_data = ''
        sys.stdout.write(f'{b64_data}\n')

    @classmethod
    def from_b642file(cls, file_path_bytes: str, file_name: str) -> None:
        """Convert Base64 String to File"""

        try:
            file_dir = os.path.dirname(file_path_bytes)
            with open(file_path_bytes, 'r') as f:
                file_data = f.read()
                if not file_data:
                    sys.exit(EMPTY_FILE)
                file_bytes = base64.b64decode(file_data)
                ext = filetype.guess_extension(file_bytes)

            output_file_path = os.path.join(file_dir, f'{file_name}.{ext}')
            with open(output_file_path, 'wb') as f:
                f.write(file_bytes)
        except Exception as exc:
            tc, te, tb = sys.exc_info()
            print(f'CLASS: {tc}, ERROR: {exc}, LINE_NO: {tb.tb_lineno}')
            output_file_path = ''
        sys.stdout.write(f'{output_file_path}\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Utility for Converting Files to Base64 Strings and Vice-Versa')
    parser.add_argument('flag', help='Set 0 for F2B and 1 for B2F', type=int)
    parser.add_argument('filepath', help='Raw File/File containing Base64 String', type=str)
    parser.add_argument('--output', '-o', help='Output filename', default='b64decoded', type=str)
    args = parser.parse_args()
    if not os.path.exists(args.filepath):
        sys.exit(FILE_NOT_FOUND)
    if args.flag == 0:
        F2B64AndBack.from_file2b64(args.filepath)
    if args.flag == 1:
        F2B64AndBack.from_b642file(file_name=args.output, file_path_bytes=args.filepath)
