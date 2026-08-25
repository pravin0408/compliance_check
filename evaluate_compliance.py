import csv
from datetime import datetime

def evaluate_compliance(input_csv, output_csv):
    current_date = datetime.now()

    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        # Ensure our expected output columns match plus the ones we will modify
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            compliance_status = "Compliant"
            notes = []

            # 1. Check EOL / EOS Date
            eol_date_str = row.get('EOL/EOS Date', '').strip()
            if eol_date_str:
                try:
                    eol_date = datetime.strptime(eol_date_str, '%Y-%m-%d')
                    if current_date > eol_date:
                        compliance_status = "Non-Compliant"
                        notes.append(f"EOL Expired ({eol_date_str})")
                except ValueError:
                    notes.append("Invalid EOL Date format (use YYYY-MM-DD)")

            # 2. Check if Current Build/Version matches Latest Build/Version
            current_build = row.get('Operating Build Version', '').strip()
            latest_build = row.get('Latest Vendor Build', '').strip()
            
            # If not already non-compliant due to EOL, check patches
            if compliance_status != "Non-Compliant":
                if current_build != latest_build:
                    compliance_status = "Non-Compliant"
                    notes.append(f"Missing latest patch (Current: {current_build}, Latest: {latest_build})")
            
            # Write results back to the row
            row['Compliance Status'] = compliance_status
            row['Notes'] = " | ".join(notes) if notes else "Up to date"
            
            writer.writerow(row)
            
    print(f"Compliance evaluation complete. Results saved to {output_csv}")

if __name__ == "__main__":
    import os
    
    input_file = "patching_matrix_template.csv"
    output_file = "patching_matrix_evaluated.csv"
    
    if os.path.exists(input_file):
        evaluate_compliance(input_file, output_file)
    else:
        print(f"Error: {input_file} not found.")
