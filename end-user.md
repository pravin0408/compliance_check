# 👥 End-User Operations Guide: Patching Compliance

Welcome to the Patching Compliance Dashboard operations guide. This portal is used by infrastructure administrators, vulnerability management teams, and auditors to track the security patching baseline of devices that traditional IT scanners (like Tenable) cannot authenticate against.

---

## 📊 1. Navigating the Dashboard

The dashboard automatically checks the internet every 24 hours for new vendor security releases (like Microsoft Patch Tuesday or Redhat Errata updates). 

### How to read the alarms:
* **🟩 Compliant**: The device's *Current Build* perfectly matches the vendor's latest real-time security release, and the software framework is safely supported. No action required.
* **🟥 Non-Compliant (Missing Patch)**: The vendor's API proves a newer patch exists than what is deployed on the asset. The IT team must schedule a maintenance window to upgrade this device.
* **🟥 Non-Compliant (EOL Expired)**: The Operating System or Appliance is officially End-of-Life (End of Support). It receives no further security patches and presents an extreme risk to the environment.
* **🟨 Manual Check Required**: Proprietary appliances (e.g., BeyondTrust, Dell OpenManage, Kemp Load Balancers) do not publish automated lifecycle endpoints for robots. An infrastructure admin must manually verify these against the vendor's portal offline.

---

## 📝 2. Updating the Dashboard (Applying Patches & New Devices)

All UI dashboard data is populated exclusively by updating the `devices.csv` inventory file in GitHub. **You do not need to write any code to update the dashboard.**

### I just patched a server. How do I clear the alarm?
When you successfully update a firewall, Linux server, or application appliance during your maintenance window:
1. Open the repository and edit `devices.csv`.
2. Find the row for your device (e.g., `SRV-LINUX-01`).
3. Update the far-right **Current Build** column to the brand-new version you just installed.
4. Click **Commit Changes**. 
5. The dashboard will automatically cross-reference your new version with the vendor API and turn the system back to **🟩 Compliant** within ~60 seconds.

### I deployed a new un-scannable appliance. How do I track it?
1. Open `devices.csv`.
2. Add a new row strictly adhering to this format (no extra spaces around commas):
   ```csv
   Device-Name,Vendor,OS Name,OS Version,Current Build
   ```
   *Example: `RTR-01,Cisco,IOS XE,17.6,17.6.6`*
3. Click **Commit Changes**. 
4. The dashboard will auto-generate a new tracking line for your asset.