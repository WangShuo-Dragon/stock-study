import finnhub
import pandas as pd
import json

class Stock:

    def __init__(self, apikey):
        self.finhub = finnhub.Client(api_key=apikey)

    def test(self,file_path):
        res = pd.DataFrame(self.finhub.company_basic_financials('AAPL', 'all'))
        nr = res.iloc[124:125,[2]]
        j = json.loads(nr.to_json())['series']['annual']
        # print(j)
        k = j.keys()
        result = []
        for i, v  in j.items():
            if len(result) == 0:
                obj = {}
                obj['Date'] = v[0]['period']
                for kv in k:
                    obj[kv] = ''
                result.append(obj)

            for x in result:
                for vv in v:
                    if vv['period'] not in [y['Date'] for y in result]:
                        obj = {}
                        obj['Date'] =  vv['period']
                        for kv in k:
                            obj[kv] = ''
                        result.append(obj)

                    if x['Date'] == vv['period']:
                        x[i] = vv['v']

    

        final_data = pd.DataFrame(result)
        with open(file=file_path) as f:
            final_data.to_excel(file_path, index=False)
        