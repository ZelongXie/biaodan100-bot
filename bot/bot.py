import json
import requests

url='https://biaodan100.com/web/formview/5bcee05975a03c49e044d43a'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',"Content-Type": "application/json"}
form={"F12_radio":"2018级","F1_radio":"西苑3号楼1区","F2_radio":"2","F3_radio":"03","F4":"xxx","F5_checkbox":"无，一切正常","F9_radio":"全齐","F10":"","F11":"","F6_checkbox":"","F7_checkbox":"","F8_checkbox":"","INITTIME":"1565587245142","FRMID":"5bcee05975a03c49e044d43a","TMOUT_number":"548","SECKEY":"","DYNAMICDATETYPE":""}
form = json.dumps(form).encode(encoding='utf-8')
req = requests.post(url=url, data=form, headers=headers)
print(req)
