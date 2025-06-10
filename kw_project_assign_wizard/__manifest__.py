{
    'name': 'Project task assign wizard',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Project',
    'license': 'OPL-1',
    'version': '18.0.1.0.5',

    'depends': ['project', ],
    'data': [
        'security/ir.model.access.csv',

        'wizard/assign_wizard.xml',
    ],

    'installable': True,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'live_test_url': 'https://kw-project.demo13.kitworks.systems',
}
