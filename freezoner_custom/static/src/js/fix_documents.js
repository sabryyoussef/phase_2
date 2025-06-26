/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { DocumentsTypeIcon } from "@documents/components/documents_type_icon/documents_type_icon";

// Patch the existing DocumentsTypeIcon component
patch(DocumentsTypeIcon.prototype, {
  /**
   * Override isRequest to safely handle missing method
   */
  isRequest() {
    try {
      const record = this.props.record;
      return record && typeof record.isRequest === "function"
        ? record.isRequest()
        : false;
    } catch (error) {
      console.log("isRequest method not available, returning false");
      return false;
    }
  },
});

console.log("DocumentsTypeIcon patch applied successfully");
