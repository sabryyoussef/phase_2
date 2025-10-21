# Level 1 Modules - UI Installation Format (Easy Copy-Paste)

## Overview
This document provides all Level 1 modules in a format that's easy to copy and paste for UI installation in Odoo Apps menu.

---

## Stage 1: Core Foundation Modules (5 modules)
**Purpose**: Install essential foundation modules that other modules depend on
**Risk Level**: Low

### Copy-Paste Module Names (Concatenated):
```
account_invoice_reportoractivity_dashboard_mngmntorattendance_detectionorbi_hr_equipment_asset_managementorbi_user_audit_management
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 1" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 2: Communication & Survey Modules (5 modules)
**Purpose**: Install communication and survey functionality
**Risk Level**: Low

### Copy-Paste Module Names (Concatenated):
```
bwa_email_conforbwa_f360_commissionorclient_birthdayorclient_categorisationorcrm_assignation
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 2" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 3: CRM Enhancement Modules (5 modules)
**Purpose**: Enhance CRM functionality with custom features
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
crm_controllerorcrm_lead_heatorcrm_reportordiscipline_systemoremployee_salesperson_task
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 3" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 4: Employee & Task Management (5 modules)
**Purpose**: Employee management and task assignment features
**Risk Level**: Low

### Copy-Paste Module Names (Concatenated):
```
freezoner_passwordorhide_any_menuorhr_attendance_geofenceorhr_attendance_ip_macorhr_attendance_location
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 4" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 5: HR Location & Custom Modules (5 modules)
**Purpose**: HR location tracking and custom HR features
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
hr_attendance_photo_geolocationorhr_employee_customorhr_expense_customorhr_leave_customorhr_salary_certificate
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 5" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 6: HR Certificate & Theme Modules (5 modules)
**Purpose**: HR certificates and backend theme customization
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
ks_curved_backend_theme_enterorkw_project_assign_wizardorleaves_checkorms_queryormultiproject_saleorder
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 6" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 7: Project & Integration Modules (5 modules)
**Purpose**: Project management enhancements and third-party integrations
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
odoo_attendance_user_locationorodoo_whatsapp_integrationorpartner_organizationorpartner_risk_assessmentorpartner_statement_knk
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 7" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Stage 8: Final Foundation Modules (6 modules)
**Purpose**: Complete Level 1 with partner, payment, and reporting modules
**Risk Level**: Medium

### Copy-Paste Module Names (Concatenated):
```
payment_validationorproduct_restrictionorproject_by_clientorproject_partner_fieldsorquery_deluxeorreport_xlsx
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Stage 8" from the category filter
3. **Alternative**: Copy the concatenated string above and paste into search box
4. Install all modules at once or select individual modules
5. Verify UI is working after installation

---

## Final Stage: Reporting & Sales Modules (4 modules)
**Purpose**: Complete Level 1 with reporting and sales enhancements
**Risk Level**: Low

### Copy-Paste Module Names (Concatenated):
```
sales_commissionorsales_person_customer_accessorstripe_fee_extensionorbwa_survey
```

### Installation Steps:
1. Go to **Apps** menu in Odoo UI
2. **Filter by Category**: Select "Level1 Final" from the category filter
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
- ⚠️ `ks_curved_backend_theme_enter` - May cause UI corruption
- ⚠️ `bwa_survey` - Has field conflicts (moved to final stage)
- ⚠️ Any theme or UI-related modules

### **Success Criteria:**
- ✅ All 41 modules installed without errors
- ✅ UI remains functional after each installation
- ✅ No error messages in Odoo logs
- ✅ All modules show as "Installed" in Apps menu

---

## 📊 **Quick Reference - All Modules in One List:**

For easy searching in Apps menu:

```
account_invoice_report
activity_dashboard_mngmnt
attendance_detection
bi_hr_equipment_asset_management
bi_user_audit_management
bwa_email_conf
bwa_f360_commission
client_birthday
client_categorisation
crm_assignation
crm_controller
crm_lead_heat
crm_report
discipline_system
employee_salesperson_task
freezoner_password
hide_any_menu
hr_attendance_geofence
hr_attendance_ip_mac
hr_attendance_location
hr_attendance_photo_geolocation
hr_employee_custom
hr_expense_custom
hr_leave_custom
hr_salary_certificate
ks_curved_backend_theme_enter
kw_project_assign_wizard
leaves_check
ms_query
multiproject_saleorder
odoo_attendance_user_location
odoo_whatsapp_integration
partner_organization
partner_risk_assessment
partner_statement_knk
payment_validation
product_restriction
project_by_client
project_partner_fields
query_deluxe
report_xlsx
sales_commission
sales_person_customer_access
stripe_fee_extension
bwa_survey
```

---

**Last Updated**: October 3, 2025
**Status**: Ready for UI installation
**Total Modules**: 41 Level 1 modules
