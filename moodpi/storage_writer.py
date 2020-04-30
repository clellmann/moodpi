from datetime import datetime
import os


def write_csv_line_to_daily_usb_file(usb_path, header, csv_line):
    """Writes or appends a csv line to a csv file with header

    Args:
        usb_path (str): Path to USB storage
        header (str): csv header line
        csv_line (str): csv data line
    """
    current_day = datetime.now().strftime("%Y_%m_%d")
    filepath = f"{usb_path}/{current_day}.csv"
    if not os.path.exists(filepath):
        with open(filepath, "w+") as csv_file:
            csv_file.write(f"{header}\n")
    with open(filepath, "a+") as target_file:
        target_file.write(f"{csv_line}\n")