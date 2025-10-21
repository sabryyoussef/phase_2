# Level 2 Modules - Staged Installation Plan (11 Modules)

## Overview
This plan breaks down the 11 Level 2 dependent modules into 5 carefully planned stages, installing 1-3 modules per stage to minimize risk and ensure stability.

## Prerequisites ✅
- ✅ All Level 1 modules installed successfully
- ✅ Database: `freezoners_mirror` ready
- ✅ Config: `/etc/odoo16.conf` configured
- ✅ Virtual environment active
- ✅ Odoo service stopped for installation

---

## Stage 1: Partner Custom Modules (3 modules)
**Purpose**: Install partner customization modules that extend partner functionality
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Level 1 modules + Base Partner modules

### Modules to Install:
1. `partner_custom` - Custom partner functionality
2. `partner_custom_fields` - Additional partner custom fields
3. `partner_fname_lname` - Partner first name and last name handling

### Installation Command:
```bash
cd /opt/odoo16/odoo16
source /opt/odoo16/odoo16-venv/bin/activate
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i partner_custom,partner_custom_fields,partner_fname_lname
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['partner_custom', 'partner_custom_fields', 'partner_fname_lname']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 1: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 2: Client & Cabinet Modules (2 modules)
**Purpose**: Install client document management and cabinet directory functionality
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Level 1 modules + Partner modules

### Modules to Install:
1. `client_documents` - Client document management system
2. `cabinet_directory` - Cabinet directory management

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i client_documents,cabinet_directory
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['client_documents', 'cabinet_directory']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 2: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 3: CRM Log & Compliance Modules (2 modules)
**Purpose**: Install CRM logging and compliance cycle management
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Level 1 modules + CRM modules

### Modules to Install:
1. `crm_log` - CRM logging functionality
2. `compliance_cycle` - Compliance cycle management

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i crm_log,compliance_cycle
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['crm_log', 'compliance_cycle']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 3: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 4: Freezoner Custom Modules (3 modules)
**Purpose**: Install core Freezoner custom functionality and project customization
**Estimated Time**: 8-12 minutes
**Risk Level**: Medium
**Dependencies**: Level 1 modules + Base modules

### Modules to Install:
1. `freezoner_custom` - Core Freezoner custom functionality
2. `freezoner_sale_approval` - Freezoner sale approval system
3. `project_custom` - Project customization features

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i freezoner_custom,freezoner_sale_approval,project_custom
```

### Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
modules = ['freezoner_custom', 'freezoner_sale_approval', 'project_custom']
installed = env['ir.module.module'].search([('name', 'in', modules), ('state', '=', 'installed')])
print(f'Stage 4: {len(installed)}/{len(modules)} modules installed')
print('Installed:', installed.mapped('name'))
"
```

---

## Stage 5: Final Level 2 Module (1 module)
**Purpose**: Complete Level 2 with task update functionality
**Estimated Time**: 5-8 minutes
**Risk Level**: Low
**Dependencies**: Level 1-4 modules

### Modules to Install:
1. `task_update` - Task update functionality

### Installation Command:
```bash
./odoo-bin -c /etc/odoo16.conf -d freezoners_mirror -i task_update
```

### Final Verification:
```bash
./odoo-bin shell -c /etc/odoo16.conf -d freezoners_mirror --stop-after-init -c "
# Check all Level 2 modules
all_level2_modules = [
    'partner_custom', 'partner_custom_fields', 'partner_fname_lname',
    'client_documents', 'cabinet_directory',
    'crm_log', 'compliance_cycle',
    'freezoner_custom', 'freezoner_sale_approval', 'project_custom',
    'task_update'
]

installed = env['ir.module.module'].search([('name', 'in', all_level2_modules), ('state', '=', 'installed')])
installed_names = set(installed.mapped('name'))
not_installed = [m for m in all_level2_modules if m not in installed_names]

print(f'Level 2 Total modules: {len(all_level2_modules)}')
print(f'Successfully installed: {len(installed_names)}')
print(f'Failed to install: {len(not_installed)}')
if not_installed:
    print('Failed modules:', not_installed)
else:
    print('🎉 All Level 2 modules installed successfully!')
"
```

---

## Git Checkpoints After Each Stage

### After Stage 1:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 1 complete: Partner custom modules (3 modules)

- partner_custom, partner_custom_fields, partner_fname_lname
- All modules installed successfully"
```

### After Stage 2:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 2 complete: Client & cabinet modules (2 modules)

- client_documents, cabinet_directory
- All modules installed successfully"
```

### After Stage 3:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 3 complete: CRM log & compliance modules (2 modules)

- crm_log, compliance_cycle
- All modules installed successfully"
```

### After Stage 4:
```bash
cd /opt/odoo16
git add -A
git commit -m "Stage 4 complete: Freezoner custom modules (3 modules)

- freezoner_custom, freezoner_sale_approval, project_custom
- All modules installed successfully"
```

### After Stage 5:
```bash
cd /opt/odoo16
git add -A
git commit -m "Level 2 COMPLETE: All 11 dependent modules installed successfully

- Final module: task_update
- Total: 11/11 Level 2 modules installed
- Ready for Level 3 final module installation"
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

- **Stage 1**: 8-12 minutes (3 modules)
- **Stage 2**: 8-12 minutes (2 modules)
- **Stage 3**: 8-12 minutes (2 modules)
- **Stage 4**: 8-12 minutes (3 modules)
- **Stage 5**: 5-8 minutes (1 module)

**Total Estimated Time**: 45-60 minutes for all 11 Level 2 modules

---

## Success Criteria

✅ **Level 2 Complete When:**
- [ ] All 11 modules installed without errors
- [ ] All 5 stages completed successfully
- [ ] All Git checkpoints created
- [ ] Verification shows 11/11 modules installed
- [ ] No error messages in logs
- [ ] Ready for Level 3 installation

---

## Next Steps After Level 2

Once Level 2 is complete:
1. **Create final Level 2 checkpoint**
2. **Start Level 3 installation** (1 final module)
3. **Complete system verification**
4. **Full system testing**

---

**Last Updated**: October 3, 2025
**Status**: Ready for execution
**Next Step**: Begin Stage 1 - Partner Custom Modules
