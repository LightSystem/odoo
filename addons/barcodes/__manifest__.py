{
    'name': 'Barcode',
    'version': '2.0',
    'category': 'Hidden',
    'summary': 'Scan and Parse Barcodes',
    'depends': ['web'],
    'data': [
        'data/barcodes_data.xml',
        'views/barcodes_view.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
    'post_init_hook': '_assign_default_nomeclature_id',
    'assets': {
        'web.assets_backend': [
            'barcodes/static/src/**/*',
        ],
        'web.tests_assets': ['barcodes/static/tests/legacy/helpers.js'],
        'web.qunit_suite_tests': ['barcodes/static/tests/legacy/basic/**/*_test.js'],
        'web.assets_unit_tests': ['barcodes/static/tests/*.test.js'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}
