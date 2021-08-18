import json, os
from pathlib import Path
# parse Json

file = r'C:\Users\surface\Desktop\YouWe\OCR\BilagsBerier\json\response_60627_1_formatted.json'
path = Path(file)

with path.open('r', encoding='utf-8') as file:
    data = json.loads(file.read())


header_fields = (data['header_fields'])
line_items = data['line_items']

fields = ['order_number', 'voucher_type', 'payment_account_number', 'company_vat_reg_no', 'invoice_date',
          'voucher_number', 'reference', 'total_amount_excl_vat', 'payment_id', 'currency', 'payment_date',
          'payment_iban', 'joint_payment_id', 'payment_reg_number', 'company_name', 'danish_industry_code',
          'payment_code_id', 'payment_swift_bic', 'total_amount_incl_vat', 'total_vat_amount_scanned']
# print(header_fields[2])

company_vat_nr = data['header_fields'][3]
print(company_vat_nr['value'])