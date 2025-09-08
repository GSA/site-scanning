# Agency/Bureau Codes CSV

This file contains the agency and bureau codes extracted from the OMB Circular A-11 document.

## Source
- **Document**: OMB Circular A-11 
- **URL**: https://www.whitehouse.gov/wp-content/uploads/2025/08/a11.pdf
- **Pages**: 715-726
- **Table**: Federal Agency and Bureau Codes

## File Format
The CSV file `agency_bureau_codes.csv` contains the following columns:
- `Agency Code`: 3-digit federal agency identifier
- `Bureau Code`: 2-digit bureau identifier within the agency
- `Agency Name`: Full name of the federal agency
- `Bureau Name`: Full name of the bureau/office within the agency

## Usage
This data is used for federal website identification and classification in the Site Scanning program.

## Data Extraction Process
1. Download the OMB A-11 PDF document from the White House website
2. Navigate to pages 715-726 containing the agency/bureau code table
3. Extract the table data (manually or via PDF parsing tools)
4. Convert to CSV format with proper headers
5. Validate the data for completeness and accuracy

## Notes
- The agency and bureau codes are standardized identifiers used across the federal government
- These codes are maintained by the Office of Management and Budget (OMB)
- Updates to this list should reference the most current version of OMB A-11