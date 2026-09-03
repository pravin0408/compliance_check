# 🛡️ Compliance Checker - Sample Test Data

**Time**: 2026-09-03T18:10:02.921Z  
**Purpose**: Comprehensive test cases for the Interactive Real-Time OS Compliance Checker

---

## COPY & PASTE TEST CASES

### ✅ Test Case 1: Microsoft Windows 11 Enterprise (COMPLIANT)

```
Vendor Name: Microsoft
OS or Appliance Name: Windows 11 Enterprise
OS Version: 24H2
Current Patch/Build On Device: 10.0.26100
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2034-10-10

---

### ✅ Test Case 2: Microsoft Windows Server 2022 (COMPLIANT)

```
Vendor Name: Microsoft
OS or Appliance Name: Windows Server 2022
OS Version: 21H2
Current Patch/Build On Device: 10.0.20348
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2031-10-13

---

### ❌ Test Case 3: Microsoft Windows 7 (EOL / NON-COMPLIANT)

```
Vendor Name: Microsoft
OS or Appliance Name: Windows 7 Professional
OS Version: SP1
Current Patch/Build On Device: 7601.24536
```

**Expected Result**:
- ❌ Lifecycle: END-OF-LIFE 🔴
- ❌ Patch: UNSUPPORTED 🔴
- EOL: 2020-01-14 (EXPIRED)

---

### ✅ Test Case 4: Ubuntu 22.04 LTS (COMPLIANT)

```
Vendor Name: Ubuntu
OS or Appliance Name: Ubuntu Server
OS Version: 22.04
Current Patch/Build On Device: 5.15.0-84
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2027-04-23

---

### ✅ Test Case 5: Red Hat Enterprise Linux 8 (COMPLIANT)

```
Vendor Name: Red Hat
OS or Appliance Name: RHEL
OS Version: 8.9
Current Patch/Build On Device: 4.18.0-513
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2029-05-31

---

### ✅ Test Case 6: VMware ESXi 7 (COMPLIANT)

```
Vendor Name: VMware
OS or Appliance Name: ESXi
OS Version: 7.0
Current Patch/Build On Device: 17551050
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2025-10-15

---

### ✅ Test Case 7: Cisco IOS XE (COMPLIANT)

```
Vendor Name: Cisco
OS or Appliance Name: Cisco IOS XE
OS Version: 17.6
Current Patch/Build On Device: 17.06.05
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢

---

### ✅ Test Case 8: Dell PowerStore (COMPLIANT - Proprietary)

```
Vendor Name: Dell EMC
OS or Appliance Name: PowerStore
OS Version: 5.0
Current Patch/Build On Device: 5.0.0.2
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- Source: Internal proprietary dataset

---

### ✅ Test Case 9: Dell Unity (COMPLIANT - Proprietary)

```
Vendor Name: Dell EMC
OS or Appliance Name: Unity
OS Version: 5.5
Current Patch/Build On Device: 5.5.4.0.5.037
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- Source: Internal proprietary dataset

---

### ⚠️ Test Case 10: Amazon Linux 2 (COMPLIANT)

```
Vendor Name: Amazon
OS or Appliance Name: Amazon Linux 2
OS Version: 2
Current Patch/Build On Device: 5.10.184
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2025-06-30

---

### ❌ Test Case 11: Debian 9 (EOL / NON-COMPLIANT)

```
Vendor Name: Debian
OS or Appliance Name: Debian
OS Version: 9
Current Patch/Build On Device: 4.9.0-23
```

**Expected Result**:
- ❌ Lifecycle: END-OF-LIFE 🔴
- ❌ Patch: UNSUPPORTED 🔴
- EOL: 2022-06-30 (EXPIRED)

---

### ✅ Test Case 12: Oracle Linux 8 (COMPLIANT)

```
Vendor Name: Oracle
OS or Appliance Name: Oracle Linux
OS Version: 8.8
Current Patch/Build On Device: 5.15.0-206
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2029-07-01

---

### ✅ Test Case 13: SUSE Linux Enterprise Server 15 (COMPLIANT)

```
Vendor Name: SUSE
OS or Appliance Name: SLES
OS Version: 15
Current Patch/Build On Device: 5.14.21-150400
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2026-12-31

---

### ✅ Test Case 14: Fedora 38 (COMPLIANT)

```
Vendor Name: Fedora
OS or Appliance Name: Fedora
OS Version: 38
Current Patch/Build On Device: 6.2.9-300
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- EOL: 2024-05-21

---

### ✅ Test Case 15: CentOS Stream 9 (COMPLIANT)

```
Vendor Name: CentOS
OS or Appliance Name: CentOS Stream
OS Version: 9
Current Patch/Build On Device: 5.14.0-362
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢

---

## MIXED FORMAT TEST CASES

### Test Case 16: Windows 11 with Complex Build String

```
Vendor Name: Microsoft
OS or Appliance Name: Windows 11
OS Version: 24H2
Current Patch/Build On Device: OS Build 26100.9278 (KB5120998)
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- Note: Build string parser should extract "26100.9278"

---

### Test Case 17: Dell PowerStore with Complex Build String

```
Vendor Name: Dell EMC
OS or Appliance Name: PowerStore
OS Version: 5.0
Current Patch/Build On Device: Build 2761110 (Release 5.0.0.2)
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ✅ Patch: SECURE 🟢
- Note: Parser should extract "5.0.0.2"

---

### Test Case 18: Windows with Shortened Version

```
Vendor Name: Microsoft
OS or Appliance Name: Windows 11 Enterprise
OS Version: 24H2
Current Patch/Build On Device: 26100
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ⚠️ Patch: UNKNOWN 🟡
- Note: Version is newer or equal to baseline

---

## EDGE CASE TEST CASES

### Test Case 19: Empty Build (Optional Field)

```
Vendor Name: Microsoft
OS or Appliance Name: Windows 11
OS Version: 24H2
Current Patch/Build On Device: (leave empty)
```

**Expected Result**:
- ✅ Lifecycle: SUPPORTED 🟢
- ⚠️ Patch: UNKNOWN 🟡
- Note: Build is optional

---

### Test Case 20: Proprietary Appliance (No Public Data)

```
Vendor Name: NetApp
OS or Appliance Name: ONTAP
OS Version: 9.13
Current Patch/Build On Device: 9.13.1
```

**Expected Result**:
- 🟡 Lifecycle: PROPRIETARY 🟡
- 🟡 Patch: UNKNOWN 🟡
- Message: Vendor does not publish open lifecycle APIs

---

## QUICK TEST CHECKLIST

Use this checklist to verify all functionality:

```
✅ Basic Compliance Check
  □ Test Case 1 (Windows 11 Enterprise) - Should pass
  □ Test Case 2 (Windows Server 2022) - Should pass
  
✅ EOL Detection
  □ Test Case 3 (Windows 7) - Should show EOL
  □ Test Case 11 (Debian 9) - Should show EOL
  
✅ Multiple Vendors
  □ Test Case 4 (Ubuntu) - Should pass
  □ Test Case 5 (RHEL) - Should pass
  □ Test Case 6 (VMware) - Should pass
  □ Test Case 7 (Cisco) - Should pass
  
✅ Proprietary Hardware
  □ Test Case 8 (Dell PowerStore) - Should recognize
  □ Test Case 9 (Dell Unity) - Should recognize
  
✅ Complex Build Strings
  □ Test Case 16 (Windows complex) - Should parse
  □ Test Case 17 (Dell complex) - Should parse
  
✅ Optional Fields
  □ Test Case 19 (No build) - Should handle gracefully
  □ Test Case 20 (Proprietary) - Should show warning
```

---

## HOW TO TEST

### Method 1: Manual Copy & Paste
1. Visit: https://pravin0408.github.io/compliance_check/
2. Copy one test case from above
3. Paste each field into the form
4. Click "Validate Live Compliance"
5. Verify the result matches "Expected Result"

### Method 2: Browser DevTools Console
1. Open: https://pravin0408.github.io/compliance_check/
2. Press `F12` to open Developer Tools
3. Go to "Console" tab
4. You'll see debug logs for each submission
5. Check for any JavaScript errors

### Method 3: CLI Testing (Local)
```bash
python realtime_patch_checker.py \
  --vendor "Microsoft" \
  --os-name "Windows 11 Enterprise" \
  --os-version "11-24h2-e" \
  --os-build "10.0.26100"
```

---

## EXPECTED OUTCOMES

### Success Indicators ✅
- [ ] Form accepts input without freezing
- [ ] "Validate Live Compliance" button is responsive
- [ ] Results display within 2-3 seconds
- [ ] Lifecycle status shows green (supported) or red (EOL)
- [ ] Patch status shows green (secure) or red (missing)
- [ ] No console errors (F12 → Console tab)

### Failure Indicators ❌
- [ ] Form freezes after clicking button
- [ ] No results displayed
- [ ] Console shows JavaScript errors
- [ ] Button becomes disabled and doesn't re-enable
- [ ] "Querying..." message stays indefinitely

---

## TROUBLESHOOTING

### If form doesn't respond:
1. **Hard refresh browser**: Ctrl+Shift+Delete (clear cache)
2. **Open DevTools**: Press F12
3. **Go to Console tab**: Look for red error messages
4. **Take screenshot** of any errors
5. **Report the exact error message**

### If results are wrong:
1. **Check the console logs** (F12 → Console)
2. **Verify you entered data correctly** (copy-paste to avoid typos)
3. **Try a different test case** to isolate the issue
4. **Check if API is responding** (open Network tab in F12)

### If version doesn't match:
1. **Use exact version format** from the "Recent Releases" table
2. **Try fuzzy matching** (e.g., "24H2" for Windows 11)
3. **Check vendor documentation** for correct version string

---

## LIVE TESTING NOW

**🔗 Start testing here**: https://pravin0408.github.io/compliance_check/

**Try Test Case 1 first** (Windows 11 Enterprise - most reliable):

```
Vendor Name: Microsoft
OS or Appliance Name: Windows 11 Enterprise
OS Version: 24H2
Current Patch/Build On Device: 10.0.26100
```

Then report back:
1. ✅ Did it work? (Yes/No)
2. What result did you see?
3. Any error messages? (F12 → Console)

---

**Document Created**: 2026-09-03T18:10:02.921Z  
**Test Cases**: 20 comprehensive scenarios  
**Status**: Ready for testing

