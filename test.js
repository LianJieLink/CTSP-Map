const fs = require('fs');
fetch('https://data.moenv.gov.tw/api/v2/aqx_p_268?api_key=c26e8777-0479-4287-aa2f-054299ae4a25&offset=1000')
  .then(res => res.json())
  .then(data => {
    const targets = ['陽明國小', '國安國小', '都會公園', '中科實中', '實中'];
    const found = data.records.filter(r => targets.some(t => r.dp_no && r.dp_no.includes(t)));
    if (found.length > 0) {
      const distinctDesp = [...new Set(found.map(f => f.desp))];
      const distinctDpNo = [...new Set(found.map(f => f.dp_no))];
      console.log('Found stations:', distinctDpNo);
      console.log('Found parameters:', distinctDesp);
      fs.writeFileSync('found.json', JSON.stringify(found.slice(0, 5), null, 2));
    } else {
      console.log('No matching stations in offset 1000.');
    }
  });
