from odoo import http
import json


class SanlongProdInfo(http.Controller):

    @http.route("/Sanlong/api/prod/info/upload_data", auth="user", csrf=False, type="json", methods=['POST'])
    def upload_data_data(self, **kwargs):
        data = json.loads(http.request.httprequest.data)
        env = http.request.env(context=dict(http.request.env.context, show_address=True, no_tag_br=True))
        
        partner = env['sanlong.prod.info']
        # Delete all
        partner.search([]).unlink()
        
        # create
        try:
            for x in data['data']:
                partner.create(
                    {
                        "mysql_id": x['id'],
                        "slPN": x['slPN'],
                        "customPN": x['customPN'],
                        "backPN": x['backPN'],
                        "colorNO": x['colorNO'],
                        "mould": x['mould'],
                        "standardSec": x['standardSec'],
                        "category": x['category'],
                        "TRDH_T_LINE": x['TRDH_T_LINE'],
                    }
                )
                
            env.cr.commit()
            return "success"
        except:
            return "error"
            
