# Level 2 Modules - UI Installation Format (Easy Copy-Paste)

## Overview
This document provides all Level 2 modules in a format that's easy to copy and paste for UI installation in Odoo Apps menu.

---

## Stage 1: Partner Custom Modules (3 modules)
**Purpose**: Install partner customization modules that extend partner functionality
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
partner_customorpartner_custom_fieldsorpartner_fname_lname
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level2 Stage 1" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 2: Client & Cabinet Modules (2 modules)
**Purpose**: Install client document management and cabinet directory functionality
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
client_documentsorcabinet_directory
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level2 Stage 2" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 3: CRM Log & Compliance Modules (2 modules)
**Purpose**: Install CRM logging and compliance cycle management
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
crm_logorcompliance_cycle
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level2 Stage 3" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 4: Freezoner Custom Modules (3 modules)
**Purpose**: Install core Freezoner custom functionality and project customization
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
freezoner_customorfreezoner_sale_approvalorproject_custom
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level2 Stage 4" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 5: Final Level 2 Module (1 module)
**Purpose**: Complete Level 2 with task update functionality
**Risk Level**: Low

### Copy-Paste Module Names (Concatenated):
```
task_update
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level2 Stage 5" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## 🚨 **Important Notes:**

### **Installation Strategy:**
- ✅ **Install ONE module at a time** for maximum safety
- ✅ **Test UI after each installation** to catch issues early
- ✅ **If UI breaks, uninstall the last module** and try a different one
- ✅ **Create Git checkpoints** after each successful stage

### **If UI Breaks:**
1. **Uninstall the problematic module** from Apps menu
2. **Clear browser cache** (Ctrl+F5)
3. **Try installing a different module** from the same stage
4. **Report the problematic module** so we can exclude it

### **Modules to Watch Out For:**
- ⚠️ `freezoner_custom` - Core functionality, may have dependencies
- ⚠️ `project_custom` - May depend on other project modules
- ⚠️ Any modules with complex dependencies

### **Success Criteria:**
- ✅ All 11 modules installed without errors
- ✅ UI remains functional after each installation
- ✅ No error messages in Odoo logs
- ✅ All modules show as "Installed" in Apps menu

---

## 📊 **Quick Reference - All Level 2 Modules in One List:**

For easy searching in Apps menu:

```
partner_custom
partner_custom_fields
partner_fname_lname
client_documents
cabinet_directory
crm_log
compliance_cycle
freezoner_custom
freezoner_sale_approval
project_custom
task_update
```

---

**Last Updated**: October 3, 2025
**Status**: Ready for UI installation
**Total Modules**: 11 Level 2 modules
