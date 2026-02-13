import os
import json
from datetime import datetime

def read_file(file_path):
    """Read content from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def write_json(data, output_path):
    """Write data to a JSON file."""
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=2)

def main():
    """Main function."""
    sample_data = {
        "name": "One Piece",
        "timestamp": datetime.now().isoformat(),
        "items": ["Item1", "Item2", "Item3"]
    }
    
    output_file = "output.json"
    write_json(sample_data, output_file)
    print(f"Data written to {output_file}")

if __name__ == "__main__":
    main()
    print("Luffy will become King of the Pirates!")