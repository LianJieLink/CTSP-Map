import urllib.request
import urllib.parse
import json

base_url = "https://data.moenv.gov.tw/api/v2/aqx_p_268"
params = {
    "api_key": "c26e8777-0479-4287-aa2f-054299ae4a25",
    "limit": 1000
}

url = base_url + "?" + urllib.parse.urlencode(params)

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    print("Keys in record:", list(data['records'][0].keys()))
    
    stnames = set()
    for r in data['records']:
        stname = r.get('stname', '') or r.get('sitename', '') or r.get('stat_name', '') or r.get('name', '')
        if not stname:
            for k, v in r.items():
                if 'name' in k.lower():
                    stnames.add(v)
        else:
            stnames.add(stname)
    
    print("Found names:", [s for s in stnames if any(x in str(s) for x in ['中科', '陽明', '國安', '都會', '實中'])])

