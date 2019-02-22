"""Test use of tabula-py."""

from inspect import currentframe, getframeinfo
from pathlib import Path
import tabula


COUNTDOWN_INVOICE_PATH = '../examples/countdown/countdown-nz-invoice.pdf'
NEW_WORLD_INVOICE_PATH = '../examples/new-world/new-world-invoice.pdf'


def get_script_directory():
    """Get this script's directory for relative path assignments."""
    filename = getframeinfo(currentframe()).filename
    directory = Path(filename).resolve().parent
    return directory

# Confirm Java and core tabula functions are installed correctly.
# print(tabula.environment_info())

def basic_table_identification(filename, num_pages):
    """Test basic table identification."""

    for page in list(range(1, num_pages+1)):
        pdf = tabula.read_pdf(filename, pages=page)
        if pdf is not None:
            print(pdf.head(20))
        else:
            print('No table identified')


SCRIPT_DIR = get_script_directory()
basic_table_identification(filename=SCRIPT_DIR / COUNTDOWN_INVOICE_PATH, num_pages=3)
basic_table_identification(filename=SCRIPT_DIR / NEW_WORLD_INVOICE_PATH, num_pages=3)
