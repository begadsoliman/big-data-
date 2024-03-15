import pandas as pd
import sys
import subprocess

def load_dataset(file_path):
    try:
        # Load the dataset into a Pandas DataFrame
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading the dataset: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python load.py <file_path>")
    else:
        file_path = sys.argv[1]
        df = load_dataset(file_path)
        if df is not None:
            # Call the next Python script (dpre.py)
            subprocess.run(["python3", "dpre.py"])

if __name__ == "__main__":
    main()
