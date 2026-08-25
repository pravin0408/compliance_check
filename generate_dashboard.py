import csv
import os
import requests
from datetime import datetime

def normalize_product_name(vendor, os_name):
    combined = f"{vendor} {os_name}".lower()
    
    # --- Exact API Mappings Based on common OS/Vendors ---
    
    # Microsoft
    if "windows server" in combined: return "windows-server"
    if "windows" in combined: return "windows"
    
    # Linux distributions
    if "redhat" in combined or "rhel" in combined or "red hat" in combined: return "rhel"
    if "ubuntu" in combined: return "ubuntu"
    if "debian" in combined: return "debian"
    if "suse" in combined: return "sles"
    if "amazon" in combined: return "amazon-linux"
    
    # Networking / Compute Appliances
    if "fortinet" in combined or "fortios" in combined: return "fortios"
    if "cisco" in combined and "ios" in combined: return "cisco-ios-xe"
    
    # VMware (Broadcom)
    if "esxi" in combined: return "esxi"
    if "vcenter" in combined: return "vcenter"
    
    # Default slug conversion
    return os_name.lower().replace(" ", "-")

def fetch_api_data(product_id):
    url = f"https://endoflife.date/api/{product_id}.json"
    try:
        response = requests.get(url, headers={"Accept": "application/json"}, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching {product_id}: {e}")
    return None

def main():
    if not os.path.exists("devices.csv"):
        print("Error: devices.csv not found")
        sys.exit(1)

    # Dictionary to cache API responses so we don't query the same OS multiple times
    api_cache = {}
    
    html_rows = []
    total_devices = 0
    compliant_devices = 0
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Read the devices CSV
    with open("devices.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_devices += 1
            device = row.get("Device Name", "Unknown")
            vendor = row.get("Vendor", "")
            os_name = row.get("OS Name", "")
            os_ver = row.get("OS Version", "")
            current_build = row.get("Current Build", "")

            product_id = normalize_product_name(vendor, os_name)
            
            if product_id not in api_cache:
                api_cache[product_id] = fetch_api_data(product_id)
            
            data = api_cache.get(product_id)
            
            status = "Manual Check Required"
            reason = "No automated API for this vendor"
            classes = "unknown"
            
            actual_latest = "N/A"
            actual_eol = "N/A"

            if data:
                target_cycle = None
                for cycle in data:
                    if cycle.get("cycle") == str(os_ver):
                        target_cycle = cycle
                        break
                
                if target_cycle:
                    actual_latest = target_cycle.get("latest")
                    actual_eol = target_cycle.get("eol")
                    
                    # Compliance Logic
                    now = datetime.now()
                    is_eol = False
                    
                    if actual_eol and isinstance(actual_eol, str):
                        try:
                            eol_dt = datetime.strptime(actual_eol, "%Y-%m-%d")
                            if now > eol_dt:
                                is_eol = True
                        except: pass
                        
                    if is_eol:
                        status = "Non-Compliant"
                        reason = f"EOL Expired ({actual_eol})"
                        classes = "non-compliant"
                    else:
                        if actual_latest and str(current_build) == str(actual_latest):
                            status = "Compliant"
                            reason = "Up to date"
                            classes = "compliant"
                            compliant_devices += 1
                        else:
                            status = "Non-Compliant"
                            reason = "Missing latest patch"
                            classes = "non-compliant"
                else:
                    reason = f"OS Version {os_ver} not found in database"

            html_rows.append(f"""
            <tr class="{classes}">
                <td>{device}</td>
                <td>{vendor} {os_name} {os_ver}</td>
                <td>{current_build}</td>
                <td>{actual_latest}</td>
                <td>{actual_eol}</td>
                <td style="font-weight: bold;">{status}</td>
                <td>{reason}</td>
            </tr>
            """)

    # HTML Template
    compliance_score = int((compliant_devices / total_devices * 100) if total_devices > 0 else 0)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OS & App Patching Compliance Dashboard</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f5f6fa; margin: 0; padding: 20px; color: #333; }}
        .header {{ background-color: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .metrics {{ display: flex; gap: 20px; margin-bottom: 20px; }}
        .metric-card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); flex: 1; text-align: center; }}
        .metric-card h2 {{ margin: 0; font-size: 2em; color: #2c3e50; }}
        table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f8f9fa; font-weight: 600; }}
        .compliant {{ border-left: 5px solid #2ecc71; }}
        .non-compliant {{ border-left: 5px solid #e74c3c; background-color: #fff9f9; }}
        .unknown {{ border-left: 5px solid #f1c40f; }}
        .status-badge {{ padding: 5px 10px; border-radius: 20px; font-size: 0.85em; font-weight: bold; }}
        .badge-compliant {{ background: #d5f5e3; color: #27ae60; }}
        .badge-non-compliant {{ background: #fadbd8; color: #c0392b; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🛡️ Automated Patching Compliance Dashboard</h1>
        <p>Real-time End-of-Life and Patch tracking for Unscannable Devices. Generated dynamically via GitHub Actions.</p>
        <small>Last Updated: {last_updated}</small>
    </div>

    <div class="metrics">
        <div class="metric-card">
            <h2>{total_devices}</h2>
            <p>Total Tracked Devices</p>
        </div>
        <div class="metric-card">
            <h2>{compliant_devices}</h2>
            <p>Fully Compliant</p>
        </div>
        <div class="metric-card">
            <h2 style="color: {'#2ecc71' if compliance_score > 90 else '#e74c3c'};">{compliance_score}%</h2>
            <p>Compliance Score</p>
        </div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Device Name</th>
                <th>OS Name & Version</th>
                <th>Current Build</th>
                <th>Latest Verified Patch</th>
                <th>EOL Date</th>
                <th>Status</th>
                <th>Reason</th>
            </tr>
        </thead>
        <tbody>
            {''.join(html_rows)}
        </tbody>
    </table>
</body>
</html>
    """

    os.makedirs("public", exist_ok=True)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Dashboard generated successfully at public/index.html")

if __name__ == "__main__":
    main()
