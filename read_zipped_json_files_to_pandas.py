import pandas as pd
import zipfile
import json

def read_files_from_zip(zip_path: str) -> List[Dict]:
    """Function that reads a ZIP file with millions of JSON files in it and returns a list of dictionaries.
    Args:
        zip_path (string): Path of the ZIP file
    Returns:
        List[Dict]: List of JSON files as Dictionary
    """
    dfs = []
    with zipfile.ZipFile(zip_path, 'r') as myzip:
        for filename in myzip.namelist():
            if filename.endswith('.json'):
                with myzip.open(filename) as f:
                    data = f.read()
                    json_data = json.loads(data)
                    dfs.append(json_data)
        return dfs
      
  if __name__ == "__main__":
    data = pd.DataFrame(read_files_from_zip("data.zip"))
