/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { DocumentsTypeIcon } from "@documents/components/documents_type_icon/documents_type_icon";

// Override DocumentsTypeIcon to fix isRequest error
class FixedDocumentsTypeIcon extends DocumentsTypeIcon {
  setup() {
    super.setup();
  }

  get isRequest() {
    // Safely check if isRequest method exists and call it, otherwise return false
    try {
      const record = this.props.record;
      return record && typeof record.isRequest === "function"
        ? record.isRequest()
        : false;
    } catch (error) {
      console.log("isRequest method not available, returning false");
      return false;
    }
  }
}

// Register the fixed widget to override the original
registry.category("fields").add("documents_type_icon", {
  component: FixedDocumentsTypeIcon,
  force: true,
});

console.log("Fixed DocumentsTypeIcon widget loaded successfully");
