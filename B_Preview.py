import pandas as pd
import glob
import os


def get_csv_files(folder, pattern="*.csv"):
    """Return a list of file paths matching the pattern in the given folder."""
    return glob.glob(os.path.join(folder, pattern))


def get_columns_per_file(files):
    """Return a dict mapping each filename (with folder) to its list of column names."""
    columns_dict = {}
    for f in files:
        df = pd.read_csv(f, nrows=0)  # nrows=0 reads only the header, no data
        folder_name = os.path.basename(os.path.dirname(f))
        file_name = os.path.basename(f)
        key = f"{folder_name}/{file_name}"
        columns_dict[key] = list(df.columns)
    return columns_dict


if __name__ == "__main__":
    folder = r"D:\FULL PROJECT\Olist Dataset\cleaned"

    csv_files = get_csv_files(folder)
    columns_info = get_columns_per_file(csv_files)


def get_csv_files(folder, pattern="*.csv"):
    """Return a list of file paths matching the pattern in the given folder."""
    return glob.glob(os.path.join(folder, pattern))


def get_columns_per_file(files):
    """Return a dict mapping each filename (with folder) to its list of column names."""
    columns_dict = {}
    for f in files:
        df = pd.read_csv(f, nrows=0)  # nrows=0 reads only the header, no data
        folder_name = os.path.basename(os.path.dirname(f))
        file_name = os.path.basename(f)
        key = f"{folder_name}/{file_name}"
        columns_dict[key] = list(df.columns)
    return columns_dict


if __name__ == "__main__":
    folder = r"D:\FULL PROJECT\Olist Dataset\cleaned"

    csv_files = get_csv_files(folder)
    columns_info = get_columns_per_file(csv_files)

    for filepath, cols in columns_info.items():
        print(f"\n{filepath}")
        for c in cols:
            print(f"  - {c}")