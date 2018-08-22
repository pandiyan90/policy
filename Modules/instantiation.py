import pandas as pd
from Modules.database_connection import DB

class CrmInsurnace:
    def __init__(self):
        db = DB()
        sql = "select insurance_policy_number,insurance_policy_date,insurance_expiry_date,insurance_sum_insured,insurance_premium,insurance_gross_premium,insurance_service_tax_value,insurance_net_premium,is_deleted from crm_insurance"
        self.data = db.executeQuery(sql)

    def view(self):
        print(self.data)