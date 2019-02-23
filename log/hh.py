import json
params='{"mobilephone":"{}admin_mobilephone","pwd":"{}admin_pwd"}'
params=json.loads(params)
print(params["mobilephone"])
if params['mobilephone']=="{}admin_mobilephone":
    params['mobilephone']=89
print(params["mobilephone"])
params={'amount': 400, 'memberId': '{}invest_id', 'loanId': '{}loan_id', 'password': '{}invest_pwd'}
if params['memberId'] == '{}invest_id':
    params['memberId'] = 99
print(params['memberId'])
params={'amount': 400, 'loanId': '{}loan_id', 'password': '{}invest_pwd', 'memberId': '{}invest_id'}
if params['password'] == '{}invest_pwd':
    params['pwd'] = 6
if params['memberId'] == '{}invest_id':
    params['memberId'] = 7
if params['password'] == '{}invest_pwd':
    params['password'] = 8
if params['loanId'] == '{}loan_id':
    params['loanId'] = 9
print(params)