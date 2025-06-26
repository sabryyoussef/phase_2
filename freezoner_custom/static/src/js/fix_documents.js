/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

// Simple replacement for DocumentsTypeIcon
class SimpleDocumentsTypeIcon extends Component {
  static template = xml`
        <div class="o_documents_type_icon">
            <i class="fa fa-file-text-o"/>
        </div>
    `;

  static props = {
    record: { type: Object, optional: true },
    readonly: { type: Boolean, optional: true },
    value: { type: [Boolean, String, Number], optional: true },
  };
}

// Register our simple replacement
registry.category("fields").add("documents_type_icon", {
  component: SimpleDocumentsTypeIcon,
  force: true,
});

console.log("Simple DocumentsTypeIcon replacement loaded successfully");
