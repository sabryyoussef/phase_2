# Level 1 Modules - Staged Installation Plan (41 Modules)

## Overview
This plan breaks down the 41 Level 1 foundation modules into 8 carefully planned stages, installing 4-6 modules per stage to minimize risk and ensure stability.

## Prerequisites ✅
- ✅ All base Odoo modules installed
- ✅ Database: `freezoners_mirror` ready
- ✅ Config: `/etc/odoo16.conf` configured
- ✅ Virtual environment active
- ✅ Odoo service stopped for installation

---

## Stage 1: Core Foundation Modules (5 modules)
**Purpose**: Install essential foundation modules that other modules depend on
**Estimated Time**: 8-12 minutes
**Risk Level**: Low
**Dependencies**: Base Odoo modules only

### Modules to Install:
1. `account_invoice_report` - Invoice reporting enhancements
2. `activity_dashboard_mngmnt` - Activity dashboard management
3. `attendance_detection` - Attendance detection system
4. `bi_hr_equipment_asset_management` - HR equipment and asset management
5. `bi_user_audit_management` - User audit management

### Installation Command:
```bash
cd /opt/odoo16/odoo16
source /opt/odoo16/odoo16-venv/bin/activate
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i account_invoice_report,activity_dashboard_mngmnt,attendance_detection,bi_hr_equipment_asset_management,bi_user_audit_management
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['account_invoice_report', 'activity_dashboard_mngmnt', 'attendance_detection', 'bi_hr_equipment_asset_management', 'bi_user_audit_management']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 1: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 2: Communication & Survey Modules (5 modules)
**Purpose**: Install communication and survey functionality
**Estimated Time**: 8-12 minutes
**Risk Level**: Low
**Dependencies**: Base modules + Stage 1

### Modules to Install:
1. `bwa_email_conf` - Email configuration enhancements
2. `bwa_f360_commission` - Commission management system
3. `client_birthday` - Client birthday management
4. `client_categorisation` - Client categorization system
5. `crm_assignation` - CRM assignment management

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i bwa_email_conf,bwa_f360_commission,client_birthday,client_categorisation,crm_assignation
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['bwa_email_conf', 'bwa_f360_commission', 'client_birthday', 'client_categorisation', 'crm_assignation']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 2: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 3: CRM Enhancement Modules (5 modules)
**Purpose**: Enhance CRM functionality with custom features
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Base CRM + Stage 1-2

### Modules to Install:
1. `crm_controller` - CRM controller enhancements
2. `crm_lead_heat` - Lead heat tracking
3. `crm_report` - CRM reporting enhancements
4. `discipline_system` - Employee discipline system
5. `employee_salesperson_task` - Employee salesperson task management

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i crm_controller,crm_lead_heat,crm_report,discipline_system,employee_salesperson_task
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['crm_controller', 'crm_lead_heat', 'crm_report', 'discipline_system', 'employee_salesperson_task']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 3: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 4: Employee & Task Management (5 modules)
**Purpose**: Employee management and task assignment features
**Estimated Time**: 8-12 minutes
**Risk Level**: Low
**Dependencies**: Base HR + Stage 1-3

### Modules to Install:
1. `freezoner_password` - Freezoner password management
2. `hide_any_menu` - Menu hiding functionality
3. `hr_attendance_geofence` - HR attendance geofencing
4. `hr_attendance_ip_mac` - HR attendance IP/MAC tracking
5. `hr_attendance_location` - HR attendance location tracking

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i freezoner_password,hide_any_menu,hr_attendance_geofence,hr_attendance_ip_mac,hr_attendance_location
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['freezoner_password', 'hide_any_menu', 'hr_attendance_geofence', 'hr_attendance_ip_mac', 'hr_attendance_location']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 4: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 5: HR Location & Custom Modules (5 modules)
**Purpose**: HR location tracking and custom HR features
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Base HR + Stage 1-4

### Modules to Install:
1. `hr_attendance_photo_geolocation` - HR attendance photo with geolocation
2. `hr_employee_custom` - Custom HR employee features
3. `hr_expense_custom` - Custom HR expense features
4. `hr_leave_custom` - Custom HR leave features
5. `hr_salary_certificate` - HR salary certificate generation

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i hr_attendance_photo_geolocation,hr_employee_custom,hr_expense_custom,hr_leave_custom,hr_salary_certificate
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['hr_attendance_photo_geolocation', 'hr_employee_custom', 'hr_expense_custom', 'hr_leave_custom', 'hr_salary_certificate']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 5: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 6: HR Certificate & Theme Modules (5 modules)
**Purpose**: HR certificates and backend theme customization
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Base HR + Stage 1-5

### Modules to Install:
1. `ks_curved_backend_theme_enter` - Curved backend theme
2. `kw_project_assign_wizard` - Project assignment wizard
3. `leaves_check` - Leave checking functionality
4. `ms_query` - MS Query functionality
5. `multiproject_saleorder` - Multi-project sale order management

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i ks_curved_backend_theme_enter,kw_project_assign_wizard,leaves_check,ms_query,multiproject_saleorder
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['ks_curved_backend_theme_enter', 'kw_project_assign_wizard', 'leaves_check', 'ms_query', 'multiproject_saleorder']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 6: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 7: Project & Integration Modules (5 modules)
**Purpose**: Project management enhancements and third-party integrations
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Base Project + Stage 1-6

### Modules to Install:
1. `odoo_attendance_user_location` - Odoo attendance user location
2. `odoo_whatsapp_integration` - WhatsApp integration
3. `partner_organization` - Partner organization management
4. `partner_risk_assessment` - Partner risk assessment
5. `partner_statement_knk` - Partner statement generation

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i odoo_attendance_user_location,odoo_whatsapp_integration,partner_organization,partner_risk_assessment,partner_statement_knk
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['odoo_attendance_user_location', 'odoo_whatsapp_integration', 'partner_organization', 'partner_risk_assessment', 'partner_statement_knk']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 7: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 8: Final Foundation Modules (6 modules)
**Purpose**: Complete Level 1 with partner, payment, and reporting modules
**Estimated Time**: 10-15 minutes
**Risk Level**: Medium
**Dependencies**: Base modules + Stage 1-7

### Modules to Install:
1. `payment_validation` - Payment validation system
2. `product_restriction` - Product restriction functionality
3. `project_by_client` - Project organization by client
4. `project_partner_fields` - Project partner field enhancements
5. `query_deluxe` - Advanced query functionality
6. `report_xlsx` - Excel report generation

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i payment_validation,product_restriction,project_by_client,project_partner_fields,query_deluxe,report_xlsx
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['payment_validation', 'product_restriction', 'project_by_client', 'project_partner_fields', 'query_deluxe', 'report_xlsx']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 8: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Final Stage: Reporting & Sales Modules (5 modules)
**Purpose**: Complete Level 1 with reporting and sales enhancements
**Estimated Time**: 8-12 minutes
**Risk Level**: Low
**Dependencies**: Base modules + Stage 1-8

### Modules to Install:
1. `sales_commission` - Sales commission management
2. `sales_person_customer_access` - Sales person customer access control
3. `stripe_fee_extension` - Stripe fee calculation extension
4. `bwa_survey` - Survey functionality (moved from Stage 2 - depends on freezoner_custom)

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i sales_commission,sales_person_customer_access,stripe_fee_extension,bwa_survey
```

### Final Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
# Check all Level 1 modules
all_level1_modules = [
    'account_invoice_report', 'activity_dashboard_mngmnt', 'attendance_detection', 'bi_hr_equipment_asset_management', 'bi_user_audit_management',
    'bwa_email_conf', 'bwa_f360_commission', 'client_birthday', 'client_categorisation', 'crm_assignation',
    'crm_controller', 'crm_lead_heat', 'crm_report', 'discipline_system', 'employee_salesperson_task',
    'freezoner_password', 'hide_any_menu', 'hr_attendance_geofence', 'hr_attendance_ip_mac', 'hr_attendance_location',
    'hr_attendance_photo_geolocation', 'hr_employee_custom', 'hr_expense_custom', 'hr_leave_custom', 'hr_salary_certificate',
    'ks_curved_backend_theme_enter', 'kw_project_assign_wizard', 'leaves_check', 'ms_query', 'multiproject_saleorder',
    'odoo_attendance_user_location', 'odoo_whatsapp_integration', 'partner_organization', 'partner_risk_assessment', 'partner_statement_knk',
    'payment_validation', 'product_restriction', 'project_by_client', 'project_partner_fields', 'query_deluxe',
    'report_xlsx', 'sales_commission', 'sales_person_customer_access', 'stripe_fee_extension', 'bwa_survey'
]

installed = env['ir.module.module'].search([('name', 'in', all_level1_modules), ('state', '=', 'installed')])
installed_names = set(installed.mapped('name'))
not_installed = [m for m in all_level1_modules if m not in installed_names]

print(f'Level 1 Total modules: {len(all_level1_modules)}')
print(f'Successfully installed: {len(installed_names)}')
print(f'Failed to install: {len(not_installed)}')
if not_installed:
    print('Failed modules:', not_installed)
else:
    print('🎉 All Level 1 modules installed successfully!')
"
```

---

## Git Checkpoints After Each Stage

### After Stage 1:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 1 complete: Core foundation modules (5 modules)

- account_invoice_report, activity_dashboard_mngmnt, attendance_detection
- bi_hr_equipment_asset_management, bi_user_audit_management
- All modules installed successfully"
```

### After Stage 2:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 2 complete: Communication & survey modules (5 modules)

- bwa_email_conf, bwa_f360_commission
- client_birthday, client_categorisation, crm_assignation
- All modules installed successfully"
```

### After Stage 3:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 3 complete: CRM enhancement modules (5 modules)

- crm_controller, crm_lead_heat, crm_report
- discipline_system, employee_salesperson_task
- All modules installed successfully"
```

### After Stage 4:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 4 complete: Employee & task management (5 modules)

- freezoner_password, hide_any_menu
- hr_attendance_geofence, hr_attendance_ip_mac, hr_attendance_location
- All modules installed successfully"
```

### After Stage 5:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 5 complete: HR location & custom modules (5 modules)

- hr_attendance_photo_geolocation, hr_employee_custom
- hr_expense_custom, hr_leave_custom, hr_salary_certificate
- All modules installed successfully"
```

### After Stage 6:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 6 complete: HR certificate & theme modules (5 modules)

- ks_curved_backend_theme_enter, kw_project_assign_wizard
- leaves_check, ms_query, multiproject_saleorder
- All modules installed successfully"
```

### After Stage 7:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 7 complete: Project & integration modules (5 modules)

- odoo_attendance_user_location, odoo_whatsapp_integration
- partner_organization, partner_risk_assessment, partner_statement_knk
- All modules installed successfully"
```

### After Stage 8:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 8 complete: Partner & payment modules (6 modules)

- payment_validation, product_restriction, project_by_client
- project_partner_fields, query_deluxe, report_xlsx
- All modules installed successfully"
```

### After Final Stage:
```bash
cd /opt/odoo16
git add -A
git commit -m "Level 1 COMPLETE: All 41 foundation modules installed successfully

- Final modules: sales_commission, sales_person_customer_access, stripe_fee_extension, bwa_survey
- Total: 41/41 Level 1 modules installed
- Ready for Level 2 dependent modules installation"
```

---

## Error Handling & Recovery

### If Any Stage Fails:

#### 1. Individual Module Installation
```bash
# Install failed modules one by one
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i <failed_module_name>
```

#### 2. Database Lock Resolution
```bash
# Kill any running processes
ps aux | grep odoo
sudo kill -9 <process_id>

# Restart PostgreSQL
sudo systemctl restart postgresql
```

#### 3. Rollback to Previous Stage
```bash
cd /opt/odoo16
git reset --hard HEAD~1  # Rollback to previous stage
```

---

## Timeline Estimate

- **Stage 1**: 8-12 minutes (5 modules)
- **Stage 2**: 8-12 minutes (5 modules)
- **Stage 3**: 8-12 minutes (5 modules)
- **Stage 4**: 8-12 minutes (5 modules)
- **Stage 5**: 8-12 minutes (5 modules)
- **Stage 6**: 8-12 minutes (5 modules)
- **Stage 7**: 8-12 minutes (5 modules)
- **Stage 8**: 10-15 minutes (6 modules)
- **Final Stage**: 8-12 minutes (4 modules)

**Total Estimated Time**: 1.5 - 2 hours for all 41 Level 1 modules

---

## Success Criteria

✅ **Level 1 Complete When:**
- [ ] All 41 modules installed without errors
- [ ] All 9 stages completed successfully
- [ ] All Git checkpoints created
- [ ] Verification shows 41/41 modules installed
- [ ] No error messages in logs
- [ ] Ready for Level 2 installation

---

## Next Steps After Level 1

Once Level 1 is complete:
1. **Create final Level 1 checkpoint**
2. **Start Level 2 installation** (11 dependent modules)
3. **Continue with Level 3** (1 final module)
4. **Complete system verification**

---

**Last Updated**: October 3, 2025
**Status**: Ready for execution
**Next Step**: Begin Stage 1 - Core Foundation Modules
