#!/usr/bin/env python3
"""
Validate the agency_bureau_codes.csv file for consistency and format.
"""

import csv
import re
from pathlib import Path

def validate_csv(csv_path):
    """Validate the agency/bureau codes CSV file."""
    if not Path(csv_path).exists():
        print(f"Error: CSV file not found: {csv_path}")
        return False
    
    print(f"Validating {csv_path}...")
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        expected_headers = ['Agency Code', 'Bureau Code', 'Agency Name', 'Bureau Name']
        if reader.fieldnames != expected_headers:
            print(f"Error: Incorrect headers. Expected: {expected_headers}")
            print(f"Found: {reader.fieldnames}")
            return False
        
        row_count = 0
        errors = []
        
        for i, row in enumerate(reader, start=1):
            row_count += 1
            
            # Check Agency Code format (3 digits)
            if not re.match(r'^\d{3}$', row['Agency Code']):
                errors.append(f"Row {i}: Invalid Agency Code '{row['Agency Code']}' (must be 3 digits)")
            
            # Check Bureau Code format (2 digits)
            if not re.match(r'^\d{2}$', row['Bureau Code']):
                errors.append(f"Row {i}: Invalid Bureau Code '{row['Bureau Code']}' (must be 2 digits)")
            
            # Check for empty fields
            for field, value in row.items():
                if not value.strip():
                    errors.append(f"Row {i}: Empty value for '{field}'")
    
    print(f"Total rows processed: {row_count}")
    
    if errors:
        print(f"\nFound {len(errors)} validation errors:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
        return False
    else:
        print("✓ CSV file is valid!")
        return True

if __name__ == "__main__":
    validate_csv("agency_bureau_codes.csv")