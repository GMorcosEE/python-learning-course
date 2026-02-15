# Week 13: Mini Project - Robust File Processor
# Run: python3 week13-error-handling/03_robust_file_processor.py

import os
import json
from typing import Optional, Dict, Any


# Custom exceptions
class FileProcessorError(Exception):
    """Base exception for file processor"""
    pass


class InvalidFileTypeError(FileProcessorError):
    """Raised when file type is not supported"""
    pass


class FileEmptyError(FileProcessorError):
    """Raised when file is empty"""
    pass


class DataValidationError(FileProcessorError):
    """Raised when data validation fails"""
    pass


class FileProcessor:
    """Robust file processor with comprehensive error handling"""
    
    SUPPORTED_TYPES = [".txt", ".json", ".csv"]
    
    def __init__(self, filename: str):
        self.filename = filename
        self.file_type = self._get_file_type()
        self.data: Optional[Any] = None
    
    def _get_file_type(self) -> str:
        """Get and validate file type"""
        _, ext = os.path.splitext(self.filename)
        if ext.lower() not in self.SUPPORTED_TYPES:
            raise InvalidFileTypeError(
                f"Unsupported file type: {ext}. Supported: {', '.join(self.SUPPORTED_TYPES)}"
            )
        return ext.lower()
    
    def read(self) -> Any:
        """Read file with error handling"""
        try:
            # Check if file exists
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"File not found: {self.filename}")
            
            # Check if file is readable
            if not os.access(self.filename, os.R_OK):
                raise PermissionError(f"No read permission: {self.filename}")
            
            # Check if file is empty
            if os.path.getsize(self.filename) == 0:
                raise FileEmptyError(f"File is empty: {self.filename}")
            
            # Read based on file type
            if self.file_type == ".txt":
                self.data = self._read_text()
            elif self.file_type == ".json":
                self.data = self._read_json()
            elif self.file_type == ".csv":
                self.data = self._read_csv()
            
            print(f"✅ Successfully read {self.filename}")
            return self.data
            
        except FileNotFoundError as e:
            print(f"❌ File Error: {e}")
            raise
        except PermissionError as e:
            print(f"❌ Permission Error: {e}")
            raise
        except FileEmptyError as e:
            print(f"❌ Empty File: {e}")
            raise
        except json.JSONDecodeError as e:
            print(f"❌ JSON Error: Invalid JSON format - {e}")
            raise
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            raise
    
    def _read_text(self) -> str:
        """Read text file"""
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()
    
    def _read_json(self) -> Dict:
        """Read JSON file"""
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def _read_csv(self) -> list:
        """Read CSV file (simple implementation)"""
        with open(self.filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                return []
            
            # Parse CSV
            data = []
            headers = lines[0].strip().split(",")
            for line in lines[1:]:
                values = line.strip().split(",")
                row = dict(zip(headers, values))
                data.append(row)
            return data
    
    def write(self, data: Any) -> None:
        """Write data to file with error handling"""
        try:
            # Check write permission for directory
            directory = os.path.dirname(self.filename) or "."
            if not os.access(directory, os.W_OK):
                raise PermissionError(f"No write permission in directory: {directory}")
            
            # Write based on file type
            if self.file_type == ".txt":
                self._write_text(data)
            elif self.file_type == ".json":
                self._write_json(data)
            elif self.file_type == ".csv":
                self._write_csv(data)
            
            print(f"✅ Successfully wrote to {self.filename}")
            
        except PermissionError as e:
            print(f"❌ Permission Error: {e}")
            raise
        except TypeError as e:
            print(f"❌ Type Error: Invalid data type for {self.file_type} - {e}")
            raise
        except Exception as e:
            print(f"❌ Write Error: {e}")
            raise
    
    def _write_text(self, data: str) -> None:
        """Write text file"""
        if not isinstance(data, str):
            raise TypeError("Text file requires string data")
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(data)
    
    def _write_json(self, data: Dict) -> None:
        """Write JSON file"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    
    def _write_csv(self, data: list) -> None:
        """Write CSV file"""
        if not isinstance(data, list) or not data:
            raise TypeError("CSV file requires non-empty list of dictionaries")
        
        with open(self.filename, "w", encoding="utf-8") as f:
            # Write headers
            headers = data[0].keys()
            f.write(",".join(headers) + "\n")
            
            # Write rows
            for row in data:
                values = [str(row.get(h, "")) for h in headers]
                f.write(",".join(values) + "\n")
    
    def validate_data(self, schema: Dict) -> bool:
        """Validate data against schema"""
        if self.data is None:
            raise DataValidationError("No data loaded. Call read() first.")
        
        try:
            if self.file_type == ".json":
                return self._validate_json_schema(schema)
            else:
                print("⚠️  Validation not implemented for this file type")
                return True
        except Exception as e:
            raise DataValidationError(f"Validation failed: {e}")
    
    def _validate_json_schema(self, schema: Dict) -> bool:
        """Simple JSON schema validation"""
        for key, expected_type in schema.items():
            if key not in self.data:
                raise DataValidationError(f"Missing required field: {key}")
            if not isinstance(self.data[key], expected_type):
                raise DataValidationError(
                    f"Field '{key}' has wrong type. Expected {expected_type.__name__}"
                )
        return True


# Demo the file processor
def main():
    print("=== Robust File Processor Demo ===\n")
    
    # Test 1: Text file
    print("--- Test 1: Text File ---")
    try:
        processor = FileProcessor("sample.txt")
        processor.write("Hello, World!\nThis is a test file.")
        content = processor.read()
        print(f"Content: {content[:50]}...\n")
    except FileProcessorError as e:
        print(f"Error: {e}\n")
    
    # Test 2: JSON file
    print("--- Test 2: JSON File ---")
    try:
        processor = FileProcessor("data.json")
        data = {
            "name": "Alice",
            "age": 30,
            "email": "alice@example.com"
        }
        processor.write(data)
        loaded_data = processor.read()
        print(f"Data: {loaded_data}")
        
        # Validate
        schema = {"name": str, "age": int, "email": str}
        processor.validate_data(schema)
        print("✅ Data validation passed\n")
    except FileProcessorError as e:
        print(f"Error: {e}\n")
    
    # Test 3: CSV file
    print("--- Test 3: CSV File ---")
    try:
        processor = FileProcessor("users.csv")
        data = [
            {"name": "Alice", "age": "30", "city": "New York"},
            {"name": "Bob", "age": "25", "city": "London"},
            {"name": "Charlie", "age": "35", "city": "Paris"}
        ]
        processor.write(data)
        loaded_data = processor.read()
        print(f"Loaded {len(loaded_data)} rows")
        for row in loaded_data:
            print(f"  {row}\n")
    except FileProcessorError as e:
        print(f"Error: {e}\n")
    
    # Test 4: Error cases
    print("--- Test 4: Error Handling ---")
    
    # Unsupported file type
    try:
        processor = FileProcessor("file.pdf")
    except InvalidFileTypeError as e:
        print(f"✅ Caught: {e}")
    
    # Non-existent file
    try:
        processor = FileProcessor("missing.txt")
        processor.read()
    except FileNotFoundError as e:
        print(f"✅ Caught: File not found")
    
    # Empty file
    try:
        open("empty.txt", "w").close()  # Create empty file
        processor = FileProcessor("empty.txt")
        processor.read()
    except FileEmptyError as e:
        print(f"✅ Caught: {e}")
    
    # Invalid JSON
    try:
        with open("invalid.json", "w") as f:
            f.write("{invalid json}")
        processor = FileProcessor("invalid.json")
        processor.read()
    except json.JSONDecodeError:
        print(f"✅ Caught: Invalid JSON format")
    
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    main()


# TODO: Add support for XML files
# TODO: Implement file backup before writing
# TODO: Add compression support (gzip)
# TODO: Create a file watcher that monitors changes
# TODO: Add encryption/decryption for sensitive files
