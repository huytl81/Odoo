# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Approvals by VietTotal',
    'version': '1.0',
    'category': 'Human Resources/Approvals',
    'sequence': 190,
    'summary': 'Create and validate approvals requests',
    'description': """
This module manages approvals workflow
======================================

This module manages approval requests like business trips,
out of office, overtime, borrow items, general approvals,
procurements, contract approval, etc.

According to the approval type configuration, a request
creates next activities for the related approvers.
    """,
    'depends': ['mail', 'hr', 'product'],
    'data': [
        'security/approval_security.xml',
        'security/ir.model.access.csv',

        'data/approval_category_data.xml',
        'data/mail_activity_data.xml',

        'views/approval_category_views.xml',
        'views/approval_category_approver_views.xml',
        'views/approval_product_line_views.xml',
        'views/approval_request_views.xml',
        'views/res_users_views.xml',
    ],
    'demo':[
        'data/approval_demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {
        'mail.assets_discuss_public': [
            'vtt_approvals/static/src/components/*/*',
            'vtt_approvals/static/src/models/*/*.js',
        ],
        'web.assets_backend': [
            'vtt_approvals/static/src/components/*/*.js',
            'vtt_approvals/static/src/components/*/*.scss',
            'vtt_approvals/static/src/models/*/*.js',
            'vtt_approvals/static/src/widgets/*/*.js',
        ],
        'web.assets_tests': [
            'vtt_approvals/static/tests/tours/**/*',
        ],
        'web.tests_assets': [
            'vtt_approvals/static/tests/helpers/**/*',
        ],
        'web.qunit_suite_tests': [
            'vtt_approvals/static/src/components/*/tests/*.js',
        ],
        'web.assets_qweb': [
            'vtt_approvals/static/src/components/*/*.xml',
            'vtt_approvals/static/src/xml/*.xml',
        ],
    },
    'license': 'OEEL-1',
}