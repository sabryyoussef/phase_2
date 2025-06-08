{
    "name": "Partner Custom",
    "author": "Beshoy Wageh",
    "depends": ["base", "product", "documents"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/partner.xml",
        "data/partner_stage_data.xml",
        'views/stages.xml',
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
