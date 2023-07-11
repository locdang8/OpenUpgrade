from openupgradelib import openupgrade

_delete_xmlids = [
    'payment_paypal.payment_method_paypal',
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "payment_paypal", "16.0.2.0/noupdate_changes.xml")
    openupgrade.delete_records_safely_by_xml_id(env, _delete_xmlids)
