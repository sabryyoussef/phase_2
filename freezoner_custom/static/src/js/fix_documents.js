/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

// Simple replacement for DocumentsTypeIcon
class SimpleDocumentsTypeIcon extends Component {
  static template = "documents.DocumentsTypeIcon";
  static props = {
    record: { type: Object, optional: true },
    readonly: { type: Boolean, optional: true },
    value: { type: [Boolean, String, Number], optional: true },
  };

  get isRequest() {
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

// Register our replacement
registry.category("fields").add("documents_type_icon", {
  component: SimpleDocumentsTypeIcon,
});

console.log("Simple DocumentsTypeIcon replacement loaded successfully");
