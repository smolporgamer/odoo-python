import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class CatCounter extends Component {
    static template = "animals.CatCounter";

    setup() {
        this.state = useState({ count: 0 });
    }

    increment() {
        this.state.count++;
    }
}

registry.category("actions").add("animals.CatCounter", CatCounter);