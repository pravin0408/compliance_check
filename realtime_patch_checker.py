import sys
import argparse
import requests
from datetime import datetime

# Map common user terms to the exact API product identifiers
def normalize_product_name(vendor, os_name):
    combined = f"{vendor} {os_name}".lower()
    if "windows server" in combined: return "windows-server"
    if "windows" in combined: return "windows"
    if "red hat" in combined or "rhel" in combined: return "redhat"
    if "ubuntu" in combined: return "ubuntu"
    if "oracle" in combined: return "oracle-linux"
    if "amazon" in combined: return "amazon-linux"
    if "debian" in combined: return "debian"
    if "esxi" in combined or "vsphere" in combined: return "vmware-vsphere"
    
    # Fallback to guessing based on the OS name with dashes
    return os_name.lower().replace(" ", "-")

def check_compliance(vendor, os_name, os_version=None, current_build=None):
    product_id = normalize_product_name(vendor, os_name)
    url = f"https://endoflife.date/api/{product_id}.json"
    
    print(f"\n[!] Fetching real-time data for: {vendor} {os_name} (API ID: {product_id})...")
    
    try:
        response = requests.get(url, headers={"Accept": "application/json"}, timeout=10)
        if response.status_code == 404:
            print(f"Error: Product not found in database. Checked API identifier '{product_id}'.")
            return
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Network error retrieving data: {e}")
        return
        
    print("-" * 50)
    target_cycle = None
    
    # If the user gave a version, search the API for that specific version lifecycle
    if os_version:
        for cycle in data:
            if cycle.get("cycle") == str(os_version):
                target_cycle = cycle
                break
                
    if target_cycle:
        latest_version = target_cycle.get("latest")
        eol_date = target_cycle.get("eol")
        release_date = target_cycle.get("latestReleaseDate")
        
        print(f"Target OS Version : {os_version}")
        print(f"Actual Latest Build: {latest_version}")
        print(f"Latest Patch Date : {release_date}")
        print(f"Actual EOL Date   : {eol_date}")
        
        print("\n--- COMPLIANCE RESULT ---")
        now = datetime.now()
        is_eol = False
        
        # 1. EOL Check
        if eol_date and isinstance(eol_date, str):
            try:
                eol_dt = datetime.strptime(eol_date, "%Y-%m-%d")
                if now > eol_dt:
                    is_eol = True
            except ValueError:
                pass
                
        if is_eol:
            print(f"[NON-COMPLIANT] x Reason: EOL Date ({eol_date}) has expired.")
        else:
            # 2. Build Patch Check
            if current_build:
                if str(current_build) == str(latest_version):
                    print("[COMPLIANT] OK Reason: System is running the exact latest security patch.")
                else:
                    print(f"[NON-COMPLIANT] x Reason: System build ({current_build}) differs from actual latest ({latest_version}).")
            else:
                print(f"[INFO] No Build Version provided. Please verify your system has patch: {latest_version}")
    else:
        # Fallback if specific version isn't specified or found: Show the top 3 latest cycles
        print(f"Specific OS Version '{os_version}' not found (or omitted). Showing the Latest Supported Versions overall:\n")
        print(f"{'Version (Cycle)':<20} | {'Actual Latest Patch':<20} | {'EOL Date'}")
        print("-" * 65)
        for cycle in data[:5]:
            c_ver = str(cycle.get('cycle'))
            c_lat = str(cycle.get('latest'))
            c_eol = str(cycle.get('eol'))
            print(f"{c_ver:<20} | {c_lat:<20} | {c_eol}")

if __name__ == "__main__":
    # If arguments are passed via CLI:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Real-Time Patch Checker")
        parser.add_argument("--vendor", required=True, help="Vendor Name (e.g., Microsoft)")
        parser.add_argument("--os-name", required=True, help="OS Name (e.g., Windows Server)")
        parser.add_argument("--os-version", help="OS Version (e.g., 2019)")
        parser.add_argument("--os-build", help="Current Build")
        args = parser.parse_args()
        
        check_compliance(args.vendor, args.os_name, args.os_version, args.os_build)
        
    # Interactive mode if clicked/run without args:
    else:
        print("=== Real-Time OS Patching & EOL Validator ===")
        print("Leave Version or Build blank to see general latest releases.")
        v = input("Enter Vendor Name (e.g., Microsoft, Red Hat, Ubuntu): ").strip()
        o = input("Enter OS Name (e.g., Windows Server, RHEL): ").strip()
        ver = input("Enter OS Version (e.g., 2019, 8.4, 22.04): ").strip()
        b = input("Enter Current OS Build (e.g., 17763.5576): ").strip()
        
        if not v or not o:
            print("Vendor and OS Name are required.")
            sys.exit(1)
            
        check_compliance(v, o, ver if ver else None, b if b else None)
