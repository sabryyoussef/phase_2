/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

// Override DocumentsTypeIcon to fix isRequest error
class FixedDocumentsTypeIcon extends Component {
  static template = "documents.DocumentsTypeIcon";

  get isRequest() {
    // Safely check if isRequest method exists and call it, otherwise return false
    try {
      return this.props.record.isRequest
        ? this.props.record.isRequest()
        : false;
    } catch (error) {
      console.log("isRequest method not available, returning false");
      return false;
    }
  }
}

// Register the fixed widget to override the original
registry
  .category("fields")
  .add("documents_type_icon", FixedDocumentsTypeIcon, { force: true });

console.log("Fixed DocumentsTypeIcon widget loaded successfully");
