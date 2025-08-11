import requests
import json


def get_premium(age, ht, wt, is_dia, is_bp,
                is_trans, is_chron, is_allergy, is_cancer, surg_cnt):
    diabetic = 1 if is_dia else 0
    bp = 1 if is_bp else 0
    trans = 1 if is_trans else 0
    chron = 1 if is_chron else 0
    allergy = 1 if is_allergy else 0
    cancer = 1 if is_cancer else 0

    url = 'http://127.0.0.1:5000/get-premium'
    headers = {'content-type': 'application/json'}
    req_data = {

            "age": age,
            "height": ht,
            "weight": wt,
            "diabetic": diabetic,
            "bp": bp,
            "transplant": trans,
            "chronic": chron,
            "allergy": allergy,
            "cancer": cancer,
            "surgery": surg_cnt
    }
    resp = requests.post(url, json=req_data, headers=headers)

    resp_dict = json.loads(resp.text)

    return resp_dict['premium']