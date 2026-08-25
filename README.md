# 🛡️ Automated OS & App Patching Compliance Dashboard

### Overview
This project is an automated, real-time validation matrix designed to track the patching compliance of "unscannable" devices on a network (such as proprietary hardware appliances, Firewalls, Hypervisors, and nodes that cannot be natively authenticated by scanners like Tenable/Nessus).

### ⚙️ How It Works

1. **Inventory Management (`devices.csv`)** 
   * All unscannable devices are documented in the `devices.csv` file. 
   * It tracks your *Device Name, Vendor, OS Name, OS Version,* and your *Current Build*.

2. **Real-Time Data Engine (`generate_dashboard.py`)**
   * The core Python engine reads your device list.
   * It dynamically reaches out to the open-source **[endoflife.date API](https://endoflife.date/)**.
   * It pulls the factual, real-time Latest Security Patch Version and End-of-Life (EOL) date for that specific platform (e.g., Windows Server, Redhat, Cisco IOS, VMware ESXi).

3. **Compliance Validation Logic**
   * **[NON-COMPLIANT] 🟥** : If the OS version is past its End-of-Life (EOL) / End-of-Support (EOS) date.
   * **[NON-COMPLIANT] 🟥** : If the active *Current Build* does not strictly match the *Latest Verified Patch* released by the vendor.
   * **[COMPLIANT] 🟩** : If the software is actively supported and matches the live latest patch.
   * **[MANUAL CHECK] 🟨** : Proprietary vendor appliances (such as BeyondTrust, Dell OpenManage, some Citrix) that lack a public lifecycle API are politely tagged on the dashboard for human verification.

4. **Automated Deployment (GitHub Actions & Pages)**
   * Every day at **midnight (UTC)** OR every time you **update `devices.csv`**, GitHub Actions spins up (`.github/workflows/compliance.yml`).
   * It recalculates your fleet's compliance using live internet API data, turning the metrics into a static HTML visual dashboard.
   * The report is instantly published online securely via **GitHub Pages**.

### 🚀 Managing Your Dashboard

To add or update your own devices to the compliance dashboard:
1. Open the `devices.csv` file inside this repository.
2. Add a new row matching exactly this format:
   ```csv
   Device-Name,Vendor,OS Name,OS Version,Current Build
   ```
3. Commit and push the changes. 
4. The background GitHub Actions will automatically rebuild and refresh your live Dashboard!