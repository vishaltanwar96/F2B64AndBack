import os
import sys
import base64
import argparse
from typing import Union

import filetype

# Module Level Constants
EMPTY_FILE = 'EMPTY FILE'
FILE_NOT_FOUND = 'FILE NOT FOUND'
INCORRECT_FLAG = 'INCORRECT FLAG SPECIFIED'


class F2B64AndBack(object):
    """
    Utility for Converting Files to Base64 Strings and Vice-Versa
    """

    @staticmethod
    def from_file2b64(filepath: str, **kwargs: dict) -> Union[str, None]:
        """Convert File to Base64 String"""

        try:
            with open(filepath, 'rb') as f:
                file_data = f.read()
                if not file_data:
                    return
                b64_data = base64.b64encode(file_data).decode()
        except Exception as exc:
            tc, te, tb = sys.exc_info()
            print(f'CLASS: {tc}, ERROR: {exc}, LINE_NO: {tb.tb_lineno}')
            b64_data = ''

        return f'{b64_data}\n'

    @staticmethod
    def from_b642file(filepath: str, outputfile: str, **kwargs: dict) -> Union[str, None]:
        """Convert Base64 String to File"""

        try:
            file_dir = os.path.dirname(filepath)
            with open(filepath, 'r') as f:
                file_data = f.read()
                if not file_data:
                    return
                file_bytes = base64.b64decode(file_data)
                ext = filetype.guess_extension(file_bytes)

            output_file_path = os.path.join(file_dir, f'{outputfile}.{ext}')

            with open(output_file_path, 'wb') as f:
                f.write(file_bytes)
        except Exception as exc:
            tc, te, tb = sys.exc_info()
            print(f'CLASS: {tc}, ERROR: {exc}, LINE_NO: {tb.tb_lineno}')
            output_file_path = ''

        return f'{output_file_path}\n'


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Utility for Converting Files to Base64 Strings and Vice-Versa')
    parser.add_argument('flag', help='Set 0 for F2B64 and 1 for B642F', type=int)
    parser.add_argument('filepath', help='Raw File/File containing Base64 String', type=str)
    parser.add_argument('--outputfile', '-of', help='Output filename', default='b64decoded', type=str)

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        sys.exit(FILE_NOT_FOUND)

    f2b64_and_back = F2B64AndBack()

    args_func_mapping = {
        0: f2b64_and_back.from_file2b64,
        1: f2b64_and_back.from_b642file,
    }
    flag = args.flag

    if flag not in args_func_mapping:
        sys.exit(INCORRECT_FLAG)
    else:
        data = args_func_mapping[flag](**vars(args))
        if data:
            sys.stdout.write(data)
        else:
            sys.exit(EMPTY_FILE)
