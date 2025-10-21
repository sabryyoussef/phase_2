# Custom Modules Installation Plan - Error-Free Strategy

## Overview
This document provides a systematic, error-free approach to installing 60+ custom Odoo modules following exact dependency requirements and best practices.

## Prerequisites ✅ COMPLETED
- ✅ Base Odoo modules installed (base, web, mail, portal, contacts, crm, project, hr, account, etc.)
- ✅ Database: `freezoners_mirror` ready
- ✅ Config file: `/etc/odoo16.conf` configured
- ✅ Virtual environment: `/opt/odoo16/odoo16-venv` active
- ✅ Odoo running as system service
- ✅ Git repository with checkpoints

## Installation Strategy

### Phase 1: Pre-Installation Setup
**Purpose**: Prepare environment and create safety checkpoints
**Time**: 5 minutes
**Risk**: Low

### Phase 2: Level 1 - Foundation Modules (41 modules)
**Purpose**: Install modules with minimal dependencies
**Time**: 45-60 minutes
**Risk**: Medium

### Phase 3: Level 2 - Dependent Modules (11 modules)
**Purpose**: Install modules that depend on Level 1 modules
**Time**: 20-30 minutes
**Risk**: Medium

### Phase 4: Level 3 - Final Modules (1 module)
**Purpose**: Install final payment/status modules
**Time**: 5-10 minutes
**Risk**: Low

### Phase 5: Verification & Testing
**Purpose**: Verify all modules installed correctly
**Time**: 10 minutes
**Risk**: Low

---

## Phase 1: Pre-Installation Setup

### Step 1.1: Create Pre-Custom Installation Checkpoint
```bash
cd /opt/odoo16
git add -A
git commit -m "Pre-custom installation checkpoint: Ready to install custom modules

- All base modules successfully installed
- Odoo running as system service
- Database and environment ready
- Starting custom module installation following dependency order"
```

### Step 1.2: Stop Odoo Service for Installation
```bash
sudo systemctl stop odoo16
```

### Step 1.3: Verify Environment
```bash
cd /opt/odoo16/odoo16
source /opt/odoo16/odoo16-venv/bin/activate
pwd  # Should show: /opt/odoo16/odoo16
which python  # Should show: /opt/odoo16/odoo16-venv/bin/python
```

---

## Phase 2: Level 1 - Foundation Modules (41 modules)

### Step 2.1: Install Core Foundation Modules (Batch 1 - 10 modules)
**Modules**: account_invoice_report, activity_dashboard_mngmnt, attendance_detection, bi_hr_equipment_asset_management, bi_user_audit_management
**Estimated Time**: 10-15 minutes
**Risk Level**: Low

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i account_invoice_report,activity_dashboard_mngmnt,attendance_detection,bi_hr_equipment_asset_management,bi_user_audit_management
```

**Verification**:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['account_invoice_report', 'activity_dashboard_mngmnt', 'attendance_detection', 'bi_hr_equipment_asset_management', 'bi_user_audit_management']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Batch 1: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

### Step 2.2: Install Communication & Survey Modules (Batch 2 - 5 modules)
**Modules**: bwa_email_conf, bwa_f360_commission, bwa_survey, client_birthday, client_categorisation
**Estimated Time**: 8-12 minutes
**Risk Level**: Low

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i bwa_email_conf,bwa_f360_commission,bwa_survey,client_birthday,client_categorisation
```

### Step 2.3: Install CRM Enhancement Modules (Batch 3 - 5 modules)
**Modules**: crm_assignation, crm_controller, crm_lead_heat, crm_report, discipline_system
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i crm_assignation,crm_controller,crm_lead_heat,crm_report,discipline_system
```

### Step 2.4: Install Employee & Task Modules (Batch 4 - 5 modules)
**Modules**: employee_salesperson_task, freezoner_password, hide_any_menu, hr_attendance_geofence, hr_attendance_ip_mac
**Estimated Time**: 8-12 minutes
**Risk Level**: Low

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i employee_salesperson_task,freezoner_password,hide_any_menu,hr_attendance_geofence,hr_attendance_ip_mac
```

### Step 2.5: Install HR Location & Custom Modules (Batch 5 - 5 modules)
**Modules**: hr_attendance_location, hr_attendance_photo_geolocation, hr_employee_custom, hr_expense_custom, hr_leave_custom
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i hr_attendance_location,hr_attendance_photo_geolocation,hr_employee_custom,hr_expense_custom,hr_leave_custom
```

### Step 2.6: Install HR Certificate & Theme Modules (Batch 6 - 5 modules)
**Modules**: hr_salary_certificate, ks_curved_backend_theme_enter, kw_project_assign_wizard, leaves_check, ms_query
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i hr_salary_certificate,ks_curved_backend_theme_enter,kw_project_assign_wizard,leaves_check,ms_query
```

### Step 2.7: Install Project & Integration Modules (Batch 7 - 5 modules)
**Modules**: multiproject_saleorder, odoo_attendance_user_location, odoo_whatsapp_integration, partner_organization, partner_risk_assessment
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i multiproject_saleorder,odoo_attendance_user_location,odoo_whatsapp_integration,partner_organization,partner_risk_assessment
```

### Step 2.8: Install Partner & Payment Modules (Batch 8 - 5 modules)
**Modules**: partner_statement_knk, payment_validation, product_restriction, project_by_client, project_partner_fields
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i partner_statement_knk,payment_validation,product_restriction,project_by_client,project_partner_fields
```

### Step 2.9: Install Final Level 1 Modules (Batch 9 - 6 modules)
**Modules**: query_deluxe, report_xlsx, sales_commission, sales_person_customer_access, stripe_fee_extension
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i query_deluxe,report_xlsx,sales_commission,sales_person_customer_access,stripe_fee_extension
```

### Step 2.10: Level 1 Verification & Checkpoint
```bash
cd /opt/odoo16
git add -A
git commit -m "Checkpoint: Level 1 foundation modules installed successfully

- Installed 41 foundation modules in 9 batches
- All modules with minimal dependencies completed
- Ready for Level 2 dependent modules installation"
```

---

## Phase 3: Level 2 - Dependent Modules (11 modules)

### Step 3.1: Install Partner Custom Modules (Batch 1 - 3 modules)
**Modules**: partner_custom, partner_custom_fields, partner_fname_lname
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i partner_custom,partner_custom_fields,partner_fname_lname
```

### Step 3.2: Install Client & Cabinet Modules (Batch 2 - 2 modules)
**Modules**: client_documents, cabinet_directory
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i client_documents,cabinet_directory
```

### Step 3.3: Install CRM Log & Compliance Modules (Batch 3 - 2 modules)
**Modules**: crm_log, compliance_cycle
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i crm_log,compliance_cycle
```

### Step 3.4: Install Freezoner Custom Modules (Batch 4 - 3 modules)
**Modules**: freezoner_custom, freezoner_sale_approval, project_custom
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i freezoner_custom,freezoner_sale_approval,project_custom
```

### Step 3.5: Install Final Level 2 Module (Batch 5 - 1 module)
**Modules**: task_update
**Estimated Time**: 5-8 minutes
**Risk Level**: Low

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i task_update
```

### Step 3.6: Level 2 Verification & Checkpoint
```bash
cd /opt/odoo16
git add -A
git commit -m "Checkpoint: Level 2 dependent modules installed successfully

- Installed 11 dependent modules in 5 batches
- All modules depending on Level 1 modules completed
- Ready for Level 3 final modules installation"
```

---

## Phase 4: Level 3 - Final Modules (1 module)

### Step 4.1: Install Payment Status Module
**Modules**: payment_status_in_sale
**Estimated Time**: 5-8 minutes
**Risk Level**: Low

```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i payment_status_in_sale
```

### Step 4.2: Level 3 Verification & Checkpoint
```bash
cd /opt/odoo16
git add -A
git commit -m "Checkpoint: Level 3 final modules installed successfully

- Installed payment_status_in_sale module
- All custom modules installation completed
- Ready for system verification and testing"
```

---

## Phase 5: Verification & Testing

### Step 5.1: Comprehensive Module Verification
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
# Check all custom modules
all_custom_modules = [
    'account_invoice_report', 'activity_dashboard_mngmnt', 'attendance_detection', 'bi_hr_equipment_asset_management', 'bi_user_audit_management',
    'bwa_email_conf', 'bwa_f360_commission', 'bwa_survey', 'client_birthday', 'client_categorisation',
    'crm_assignation', 'crm_controller', 'crm_lead_heat', 'crm_report', 'discipline_system',
    'employee_salesperson_task', 'freezoner_password', 'hide_any_menu', 'hr_attendance_geofence', 'hr_attendance_ip_mac',
    'hr_attendance_location', 'hr_attendance_photo_geolocation', 'hr_employee_custom', 'hr_expense_custom', 'hr_leave_custom',
    'hr_salary_certificate', 'ks_curved_backend_theme_enter', 'kw_project_assign_wizard', 'leaves_check', 'ms_query',
    'multiproject_saleorder', 'odoo_attendance_user_location', 'odoo_whatsapp_integration', 'partner_organization', 'partner_risk_assessment',
    'partner_statement_knk', 'payment_validation', 'product_restriction', 'project_by_client', 'project_partner_fields',
    'query_deluxe', 'report_xlsx', 'sales_commission', 'sales_person_customer_access', 'stripe_fee_extension',
    'partner_custom', 'partner_custom_fields', 'partner_fname_lname', 'client_documents', 'cabinet_directory',
    'crm_log', 'compliance_cycle', 'freezoner_custom', 'freezoner_sale_approval', 'project_custom',
    'task_update', 'payment_status_in_sale'
]

installed = env['ir.module.module'].search([('name', 'in', all_custom_modules), ('state', '=', 'installed')])
installed_names = set(installed.mapped('name'))
not_installed = [m for m in all_custom_modules if m not in installed_names]

print(f'Total custom modules: {len(all_custom_modules)}')
print(f'Successfully installed: {len(installed_names)}')
print(f'Failed to install: {len(not_installed)}')
print('Not installed modules:', not_installed)
"
```

### Step 5.2: Start Odoo Service
```bash
sudo systemctl start odoo16
sudo systemctl status odoo16
```

### Step 5.3: Final Verification
```bash
# Check Odoo is accessible
curl -I http://localhost:8069

# Check system service status
sudo systemctl is-active odoo16
```

### Step 5.4: Final Git Checkpoint
```bash
cd /opt/odoo16
git add -A
git commit -m "Final checkpoint: All custom modules installed successfully

- Level 1: 41 foundation modules installed
- Level 2: 11 dependent modules installed  
- Level 3: 1 final module installed
- Total: 53 custom modules successfully installed
- Odoo system fully operational with all customizations
- Production environment ready"
```

---

## Error Handling & Recovery

### Common Issues & Solutions

#### Issue 1: Database Lock Error
**Symptoms**: "database is locked" or "connection failed"
**Solution**:
```bash
# Kill any running Odoo processes
ps aux | grep odoo
sudo kill -9 <process_id>

# Restart PostgreSQL
sudo systemctl restart postgresql

# Try installation again
```

#### Issue 2: Module Dependency Error
**Symptoms**: "Module not found" or "dependency not satisfied"
**Solution**:
```bash
# Install missing dependencies first
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i <missing_module>

# Then retry the failed module
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i <failed_module>
```

#### Issue 3: Installation Timeout
**Symptoms**: Installation hangs or takes too long
**Solution**:
```bash
# Install modules individually instead of in batches
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i <module_name> --stop-after-init
```

#### Issue 4: Memory Issues
**Symptoms**: "Memory error" or "killed"
**Solution**:
```bash
# Increase memory limits
export PYTHONOPTIMIZE=1
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i <modules> --limit-memory-hard=67108864
```

### Rollback Procedures

#### Rollback to Pre-Custom Installation
```bash
cd /opt/odoo16
git reset --hard HEAD~1  # Rollback to base modules checkpoint
sudo systemctl restart odoo16
```

#### Rollback to Level 1 Complete
```bash
cd /opt/odoo16
git reset --hard HEAD~2  # Rollback to Level 1 checkpoint
sudo systemctl restart odoo16
```

---

## Success Criteria

### ✅ Installation Complete When:
- [ ] All 53 custom modules installed without errors
- [ ] Odoo service running normally
- [ ] Web interface accessible
- [ ] No error messages in logs
- [ ] All Git checkpoints created
- [ ] Database responsive and stable

### ✅ Verification Commands:
```bash
# Check service status
sudo systemctl status odoo16

# Check web interface
curl -I http://localhost:8069

# Check installed modules
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "print('Total installed modules:', len(env['ir.module.module'].search([('state', '=', 'installed')])))"
```

---

## Timeline Estimate

- **Phase 1**: 5 minutes (Setup & Checkpoint)
- **Phase 2**: 45-60 minutes (Level 1 - 41 modules)
- **Phase 3**: 20-30 minutes (Level 2 - 11 modules)
- **Phase 4**: 5-10 minutes (Level 3 - 1 module)
- **Phase 5**: 10 minutes (Verification & Testing)

**Total Estimated Time**: 1.5 - 2 hours

---

## Notes

- **Database**: `freezoners_mirror`
- **Config File**: `/etc/odoo16.conf`
- **Virtual Environment**: `/opt/odoo16/odoo16-venv`
- **Working Directory**: `/opt/odoo16/odoo16`
- **Git Repository**: `/opt/odoo16`

- Install modules in small batches to minimize risk
- Create checkpoints after each phase
- Monitor logs during installation
- Test functionality after each batch
- Keep Odoo service stopped during installation
- Restart service only after all modules installed

---

**Last Updated**: October 3, 2025
**Status**: Ready for execution
**Next Step**: Begin Phase 1 - Pre-Installation Setup
