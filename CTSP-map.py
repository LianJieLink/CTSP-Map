import folium
from folium import plugins

# 1. Initialize map, enable scale control and base map settings
map_center = [24.205, 120.610]
m = folium.Map(location=map_center, zoom_start=15, tiles=None, control_scale=True)

# Add OSM and Google Satellite maps
folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google', name='Google Satellite', overlay=False
).add_to(m)

# --- 2. Precisely define factory areas (Polygons) ---

# TSMC Fab 15A (North block of Keya 6th Rd)
tsmc_15a_poly = [
    [24.210748, 120.613622], [24.212753, 120.614386],
    [24.212835, 120.614151], [24.213276, 120.614314],
    [24.213370, 120.614092], [24.213669, 120.614195],
    [24.213693, 120.614135], [24.214217, 120.614355],
    [24.214181, 120.614447], [24.214289, 120.614508],
    [24.214259, 120.614672], [24.214715, 120.614855],
    [24.213774, 120.617844], [24.211415, 120.616943],
    [24.210194, 120.616207], [24.210371, 120.615796],
    [24.210087, 120.615588]
]

# TSMC Fab 15B (Main area around Xinke Rd)
tsmc_15b_poly = [
    [24.207266, 120.604354], [24.211896, 120.605976],
    [24.211193, 120.608122], [24.210209, 120.607800],
    [24.209502, 120.610195], [24.207666, 120.609473],
    [24.207899, 120.608511], [24.207250, 120.608247],
    [24.207655, 120.607025], [24.206988, 120.606751],
    [24.207289, 120.605672], [24.206855, 120.605507],
]

# Taichung Zero Waste Manufacturing Center (No. 8, Keya 7th Rd, West of 15A)
zero_waste_poly = [
    [24.217901, 120.618393], [24.218547, 120.617499],
    [24.218812, 120.617482], [24.218866, 120.617578],
    [24.218868, 120.618118], [24.219117, 120.618159],
    [24.219097, 120.620247], [24.218540, 120.620500],
    [24.217917, 120.620484], [24.217735, 120.620346],
]

tsmc_ap5_poly = [
    [24.214941, 120.615113], [24.215863, 120.615447],
    [24.215750, 120.615847], [24.216071, 120.615973],
    [24.215202, 120.618677], [24.213999, 120.618230]
]

tsmc_F22_poly = [
    [22.709036, 120.309586], [22.710023, 120.311178],
    [22.710440, 120.310996], [22.711394, 120.312520],
    [22.711269, 120.312668], [22.711647, 120.313366],
    [22.708753, 120.315414], [22.707774, 120.313353],
    [22.707393, 120.313551], [22.706121, 120.311368]
]

tsmc_AP3_poly = [
    [24.884367, 121.184084], [24.884230, 121.186584],
    [24.882323, 121.186456], [24.882495, 121.183958]
]

tsmc_AP6_poly = [
    [24.703230, 120.908459], [24.703207, 120.906236],
    [24.709369, 120.906242], [24.709336, 120.908146]
]

tsmc_F20_poly = [
    [24.764687, 121.001860], [24.767499, 121.002788],
    [24.766183, 121.007464], [24.763308, 121.006402]
]

tsmc_F12P1and2_poly = [
    [24.773022, 121.010353], [24.774771, 121.012461],
    [24.772975, 121.014548], [24.771347, 121.012944],
]

tsmc_F12P4and5_poly = [
    [24.769878, 121.010905], [24.771193, 121.012924],
    [24.770647, 121.013607], [24.769822, 121.014109],
    [24.767651, 121.011096], [24.768660, 121.010739]
]

tsmc_F12P6_poly = [
    [24.771438, 121.009267], [24.772856, 121.010237],
    [24.771313, 121.012809], [24.770037, 121.010997],
    [24.770751, 121.010482]
]

tsmc_F12P7_poly = [
    [24.767562, 121.011198], [24.769513, 121.014310],
    [24.767834, 121.015373], [24.766462, 121.013011],
    [24.766503, 121.012542], [24.766819, 121.011837]
]

tsmc_F12P8_poly = [
    [24.770349, 121.008625], [24.770309, 121.010572],
    [24.769786, 121.010746], [24.768360, 121.010563],
    [24.767955, 121.010715], [24.766788, 121.011694],
    [24.766861, 121.008381], [24.768116, 121.008181],
    [24.768328, 121.008160], [24.769580, 121.008297]
]

tsmc_F18P1_poly = [
    [23.117909, 120.261374], [23.121140, 120.259796],
    [23.122033, 120.261913], [23.118956, 120.263582]
]

tsmc_F18P2_poly = [
    [23.117805, 120.257763], [23.119772, 120.256815],
    [23.121056, 120.259705], [23.119123, 120.260661]
]

tsmc_F18P7_poly = [
    [23.118892, 120.263711], [23.120678, 120.267745],
    [23.118201, 120.267531], [23.117833, 120.267303],
    [23.116813, 120.264822]
]

# --- 3. Station Coordinates ---
# MOENV Stations (Blue Asterisk)
env_pts = {
    "沙鹿": [24.225628, 120.568794],
    "西屯": [24.162197, 120.616917],
    "忠明": [24.151958, 120.641092],
    "楠梓": [22.733667, 120.328289],
    "左營": [22.674861, 120.292917],
    "仁武": [22.689056, 120.332631],
    "龍潭": [24.86400048, 121.21645772],
    "新竹": [24.8056356, 120.97236752],
    "竹東": [24.74091408, 121.08895493],
    "頭份": [24.69690679, 120.89869286],
    "朴子": [23.46538, 120.2478],
    "嘉義": [23.46477865, 120.44125148],
    "新港": [23.554839, 120.345531],
    "善化": [23.11337642, 120.29740529],
    "安南": [23.048197, 120.2175]
}

# SP Industrial Stations (Green Triangle)
ind_pts = {
    "陽明國小": [24.22139, 120.63194], 
    "國安國小": [24.19361, 120.60861], 
    "都會公園": [24.21111, 120.59833], 
    "中科實中": [24.22944, 120.62583],
    "竹科龍潭(環保中心)": [24.887787, 121.1883272],
    "竹科德龍(德龍國小)": [24.882046, 121.195207],
    "竹科聖德(聖德里)": [24.889177, 121.201821],
    "新安": [24.784714, 120.991939],
    "靜心湖": [24.778281, 121.013773],
    "力行": [24.76637, 121.016265],
    "興業": [24.77806, 120.989786],
    "竹南東": [24.70966, 120.92154],
    "竹南西": [24.71361, 120.91031],
    "竹南南": [24.70611, 120.91282],
    "竹南北": [24.70817, 120.89529],
    "嘉義縣東石": [23.46248333, 120.172425],
    "公13": [23.09003889, 120.2845694],
    "公19": [23.12582, 120.26943],
    "公29": [23.10635, 120.2692611],
    "南科實中": [23.10739722, 120.2912611],
    "油廠國小": [22.709434, 120.303392],
    "半屏山加壓站": [22.695393, 120.301884],
    "園區東南站": [22.703263, 120.32075],
    "園區北站": [22.712882, 120.313685]
}

# CWA Stations (Orange Cloud)
cwa_pts = {
    "大雅(自動)": [24.2153, 120.6244],
    "高雄(人工)": [22.7304, 120.3125],
    "龍潭(自動)": [24.889177, 121.201821],
    "新竹市東區(自動)": [24.7987, 120.9869],
    "寶山(自動)": [24.7350, 121.0252],
    "竹東(自動)": [24.7671, 121.0579],
    "頭份(自動)": [24.6882, 120.9122],
    "龍鳳(自動)": [24.7000, 120.8591],
    "六腳(自動)": [23.4929, 120.2906],
    "蔦松(自動)": [23.5143, 120.2297],
    "善化(自動)": [23.1129, 120.2972],
    "安定(自動)": [23.1026, 120.2276]
}

# --- 3.5. Fetch MOENV API Data ---
import json
# Data fetching moved to Javascript for real-time frontend updates on Github Pages
# --- 4. Draw Layers ---

# Factory Layer
fg_fab = folium.FeatureGroup(name='廠區範圍')
for coords, name in [(tsmc_15a_poly, "台積電 15A 廠"),
                     (tsmc_15b_poly, "台積電 15B 廠"),
                     (tsmc_ap5_poly, "台積電 AP5 廠"),
                     (zero_waste_poly, "台中零廢製造中心"),
                     (tsmc_F22_poly, "台積電 F22 廠"),
                     (tsmc_AP3_poly, "台積電 AP3 廠"),
                     (tsmc_AP6_poly, "台積電 AP6 廠"),
                     (tsmc_F20_poly, "台積電 F20 廠"),
                     (tsmc_F12P1and2_poly, "台積電 F12P1&2 廠"),
                     (tsmc_F12P4and5_poly, "台積電 F12P4&5 廠"),
                     (tsmc_F12P6_poly, "台積電 F12P6 廠"),
                     (tsmc_F12P7_poly, "台積電 F12P7 廠"),
                     (tsmc_F12P8_poly, "台積電 F12P8 廠"),
                     (tsmc_F18P1_poly, "台積電 F18P1 廠"),
                     (tsmc_F18P2_poly, "台積電 F18P2 廠"),
                     (tsmc_F18P7_poly, "台積電 F18P7 廠")]:
    folium.Polygon(
        locations=coords, color="red", weight=2,
        fill=True, fill_color="red", fill_opacity=0.4,
        tooltip=name, popup=f"<b>{name}</b>"
    ).add_to(fg_fab)

# MOENV Layer
fg_env = folium.FeatureGroup(name='環境部測站')

# We inject JS to fetch and populate MOENV stations dynamically
env_pts_js = json.dumps(env_pts)
fg_env_name = fg_env.get_name()

js_code = f"""
<script>
window.makePopupDraggable = function(e) {{
    let popupContainer = e.popup._container;
    if (popupContainer.dataset.draggable) return;
    popupContainer.dataset.draggable = "true";
    let header = popupContainer.querySelector('.drag-header');
    if (!header) return;
    
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    header.onmousedown = function(ev) {{
        ev = ev || window.event;
        ev.preventDefault();
        pos3 = ev.clientX;
        pos4 = ev.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }};
    function elementDrag(ev) {{
        ev = ev || window.event;
        ev.preventDefault();
        pos1 = pos3 - ev.clientX;
        pos2 = pos4 - ev.clientY;
        pos3 = ev.clientX;
        pos4 = ev.clientY;
        let mb = parseInt(window.getComputedStyle(popupContainer).marginBottom || 0);
        let ml = parseInt(window.getComputedStyle(popupContainer).marginLeft || 0);
        popupContainer.style.marginBottom = (mb + pos2) + "px";
        popupContainer.style.marginLeft = (ml - pos1) + "px";
    }}
    function closeDragElement() {{
        document.onmouseup = null;
        document.onmousemove = null;
    }}
}};
document.addEventListener('DOMContentLoaded', function() {{
    const urls = [
        "https://data.moenv.gov.tw/api/v2/aqx_p_138?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_139?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_140?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_141?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_142?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_146?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_147?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_149?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_150?api_key=c26e8777-0479-4287-aa2f-054299ae4a25"
    ];

    let moenvData = {{}};
    let env_pts = {env_pts_js};

    function formatLST(dt_str) {{
        if (!dt_str || dt_str === "N/A") return "N/A";
        // API returns "YYYY-MM-DD HH:MM" in LST directly. Just append seconds.
        return dt_str + ":00";
    }}

    Promise.all(urls.map(url => fetch(url).then(res => res.json()).catch(e => null)))
        .then(results => {{
            results.forEach(data => {{
                if (!data) return;
                const records = Array.isArray(data) ? data : (data.records || []);
                records.forEach(record => {{
                    const st = record.sitename;
                    if (!moenvData[st]) moenvData[st] = {{}};
                    
                    const param = record.itemengname;
                    let pName = param;
                    if (param === 'WIND_DIREC') pName = 'WindDirec';
                    if (param === 'WIND_SPEED') pName = 'WindSpeed';
                    if (param === 'AM_TEMP') pName = 'Temp';
                    if (param === 'RH') pName = 'Humid';
                    
                    let recordTime = record.monitordate || "";
                    let currentParamTime = moenvData[st][pName + "_time"] || "";
                    
                    // Keep only the latest data for each metric
                    if (!currentParamTime || recordTime >= currentParamTime) {{
                        moenvData[st][pName] = record.concentration;
                        moenvData[st][pName + "_time"] = recordTime;
                        
                        // Update the overall station update_time to the maximum monitor date
                        let currentStTime = moenvData[st]['update_time'] || "";
                        if (!currentStTime || recordTime >= currentStTime) {{
                            moenvData[st]['update_time'] = recordTime;
                        }}
                    }}
                }});
            }});

            let layerGroup = {fg_env_name};
            Object.keys(env_pts).forEach(function(base_name) {{
                let clean_name = base_name.replace("站", "");
                let st_info = moenvData[clean_name] || {{}};
                
                let pm10 = st_info["PM10"] || "N/A";
                let pm25 = st_info["PM2.5"] || "N/A";
                let no2 = st_info["NO2"] || "N/A";
                let so2 = st_info["SO2"] || "N/A";
                let o3 = st_info["O3"] || "N/A";
                let co = st_info["CO"] || "N/A";
                let wd = st_info["WindDirec"] || "N/A";
                let ws = st_info["WindSpeed"] || "N/A";
                let temp = st_info["Temp"] || "N/A";
                let humid = st_info["Humid"] || "N/A";
                let dt_str = formatLST(st_info["update_time"]);
                
                let metrics = [
                    {{val: pm10, label: 'PM10', unit: 'μg/m³'}},
                    {{val: pm25, label: 'PM2.5', unit: 'μg/m³'}},
                    {{val: no2, label: 'NO2', unit: 'ppb'}},
                    {{val: so2, label: 'SO2', unit: 'ppb'}},
                    {{val: o3, label: 'O3', unit: 'ppb'}},
                    {{val: co, label: 'CO', unit: 'ppm'}},
                    {{val: temp, label: '溫度', unit: '°C'}},
                    {{val: humid, label: '濕度', unit: '%'}},
                    {{val: wd, label: '風向', unit: '°'}},
                    {{val: ws, label: '風速', unit: 'm/s'}}
                ];
                let rowsHtml = "";
                metrics.forEach(m => {{
                    if (m.val && m.val !== "N/A") {{
                        rowsHtml += `<tr style='border-bottom: 1px solid #eee;'><td style='color: #666; padding: 2px 0;'>${{m.label}}</td><td style='text-align: right;'><b>${{m.val}}</b> <span style='font-size: 10px; color: #888;'>${{m.unit}}</span></td></tr>`;
                    }}
                }});

                let tooltip_html = `<div style='font-family: "Segoe UI", Arial, sans-serif; font-size: 13px; width: 170px; background-color: transparent;'>
                    <div class='drag-header' style='cursor: move; font-size: 14px; font-weight: bold; color: #333; margin-bottom: 5px; border-bottom: 2px solid #3498db; padding-bottom: 3px;'>
                        📍 ${{base_name}} <span style='font-size:10px;color:#666;'>(環境部)</span>
                    </div>
                    <table style='width: 100%; border-collapse: collapse;'>
                        ${{rowsHtml}}
                    </table>
                    <div style='margin-top: 6px; font-size: 10px; color: #999; text-align: center;'>
                        🕒 擷取時間: ${{dt_str}}
                    </div>
                </div>`;

                let marker = L.marker(env_pts[base_name], {{
                    icon: L.AwesomeMarkers.icon({{icon: 'star', markerColor: 'blue', prefix: 'fa', extraClasses: 'fa-rotate-0'}})
                }});
                
                marker.bindPopup(tooltip_html, {{maxWidth: 220, autoClose: false, closeOnClick: false, className: 'draggable-popup'}});
                marker.on('popupopen', window.makePopupDraggable);
                marker.addTo(layerGroup);
            }});
        }})
        .catch(err => console.error("Error fetching MOENV APIs:", err));
}});
</script>
"""
m.get_root().html.add_child(folium.Element(js_code))

# Industrial Station Layer
fg_ind = folium.FeatureGroup(name='特殊性工業區測站')
target_ind_names = [
    "陽明國小", "國安國小", "都會公園", "中科實中",
    "新安", "靜心湖", "力行", "興業",
    "竹南東", "竹南西", "竹南南", "竹南北",
    "嘉義縣東石", "公13", "公19", "公29", "南科實中",
    "油廠國小", "半屏山加壓站", "園區東南站", "園區北站"
]
for name, pos in ind_pts.items():
    if name not in target_ind_names:
        folium.Marker(
            location=pos, tooltip=name,
            icon=folium.Icon(color="green", icon="caret-up", prefix="fa")
        ).add_to(fg_ind)

target_ind_pts_js = json.dumps({k: ind_pts[k] for k in target_ind_names})
fg_ind_name = fg_ind.get_name()

js_code_ind = f"""
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const indUrls = [
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=1000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=2000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=3000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=4000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=5000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=6000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=7000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=8000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=9000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=10000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=11000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25",
        "https://data.moenv.gov.tw/api/v2/aqx_p_268?offset=12000&api_key=c26e8777-0479-4287-aa2f-054299ae4a25"
    ];

    let targetIndPts = {target_ind_pts_js};
    let indData = {{}};

    Promise.all(indUrls.map(url => fetch(url).then(r => r.json()).catch(e => null)))
        .then(results => {{
            results.forEach(data => {{
                if (!data) return;
                const records = Array.isArray(data) ? data : (data.records || []);
                records.forEach(record => {{
                    const st = record.dp_no || record.sitename || record.stname || "";
                    if (!st.includes("陽明") && !st.includes("國安") && !st.includes("都會") && !st.includes("實中") &&
                        !st.includes("新安") && !st.includes("靜心") && !st.includes("力行") && !st.includes("興業") &&
                        !st.includes("南東") && !st.includes("南西") && !st.includes("南南") && !st.includes("南北") &&
                        !st.includes("東石") && !st.includes("公13") && !st.includes("公19") && !st.includes("公29") &&
                        !st.includes("油廠") && !st.includes("半屏山") && !st.includes("園區東南") && !st.includes("園區北")) return;
                    
                    let targetKey = "";
                    if (st.includes("陽明")) targetKey = "陽明國小";
                    else if (st.includes("國安")) targetKey = "國安國小";
                    else if (st.includes("都會") || st.includes("公園")) targetKey = "都會公園";
                    else if (st.includes("新安")) targetKey = "新安";
                    else if (st.includes("靜心")) targetKey = "靜心湖";
                    else if (st.includes("力行")) targetKey = "力行";
                    else if (st.includes("興業")) targetKey = "興業";
                    else if (st.includes("南東")) targetKey = "竹南東";
                    else if (st.includes("南西")) targetKey = "竹南西";
                    else if (st.includes("南南")) targetKey = "竹南南";
                    else if (st.includes("南北")) targetKey = "竹南北";
                    else if (st.includes("東石")) targetKey = "嘉義縣東石";
                    else if (st.includes("公13")) targetKey = "公13";
                    else if (st.includes("公19")) targetKey = "公19";
                    else if (st.includes("公29")) targetKey = "公29";
                    else if (st.includes("南科實中")) targetKey = "南科實中";
                    else if (st.includes("油廠")) targetKey = "油廠國小";
                    else if (st.includes("半屏山")) targetKey = "半屏山加壓站";
                    else if (st.includes("園區東南")) targetKey = "園區東南站";
                    else if (st.includes("園區北")) targetKey = "園區北站";
                    else if (st.includes("實中")) targetKey = "中科實中";
                    
                    if (!targetKey) return;
                    if (!indData[targetKey]) indData[targetKey] = {{}};
                    
                    let pName = (record.desp || record.itemengname || record.itemname || "").toLowerCase();
                    let param = "";
                    if (pName.includes("pm10") || (pName.includes("懸浮微粒") && !pName.includes("2.5") && !pName.includes("細"))) param = "PM10";
                    else if (pName.includes("pm2.5") || pName.includes("細") || pName.includes("細懸浮微粒")) param = "PM2.5";
                    else if (pName.includes("no2") || pName.includes("二氧化氮")) param = "NO2";
                    else if (pName.includes("so2") || pName.includes("二氧化硫")) param = "SO2";
                    else if (pName.includes("o3") || pName.includes("臭氧")) param = "O3";
                    else if (pName.includes("co") || pName.includes("一氧化碳")) param = "CO";
                    else if (pName.includes("風向") || pName.includes("direc")) param = "WindDirec";
                    else if (pName.includes("風速") || pName.includes("speed")) param = "WindSpeed";
                    else if (pName.includes("溫度") || pName.includes("temp") || pName === "am_temp") param = "Temp";
                    else if (pName.includes("濕度") || pName.includes("rh") || pName.includes("humid")) param = "Humid";
                    
                    if (!param) return;
                    
                    let m_date = record.m_date || record.monitordate || "";
                    let m_time = record.m_time || "";
                    let formattedTime = "";
                    if (m_date && m_time && m_time.length === 6) {{
                        formattedTime = `${{m_date}} ${{m_time.substring(0,2)}}:00:00`;
                    }} else if (m_date && m_date.includes(":")) {{
                        formattedTime = m_date;
                    }}
                    
                    let currentParamTime = indData[targetKey][param + "_time"] || "";
                    if (!currentParamTime || formattedTime >= currentParamTime) {{
                        indData[targetKey][param] = record.value || record.concentration;
                        indData[targetKey][param + "_time"] = formattedTime;
                        
                        let currentStTime = indData[targetKey]['update_time'] || "";
                        if (!currentStTime || formattedTime >= currentStTime) {{
                             indData[targetKey]['update_time'] = formattedTime;
                        }}
                    }}
                }});
            }});
            
            let layerGroup = {fg_ind_name};
            Object.keys(targetIndPts).forEach(function(base_name) {{
                let st_info = indData[base_name] || {{}};
                
                let pm10 = st_info["PM10"] || "N/A";
                let pm25 = st_info["PM2.5"] || "N/A";
                let no2 = st_info["NO2"] || "N/A";
                let so2 = st_info["SO2"] || "N/A";
                let o3 = st_info["O3"] || "N/A";
                let co = st_info["CO"] || "N/A";
                let wd = st_info["WindDirec"] || "N/A";
                let ws = st_info["WindSpeed"] || "N/A";
                let temp = st_info["Temp"] || "N/A";
                let humid = st_info["Humid"] || "N/A";
                let dt_str = st_info["update_time"] || "N/A";
                
                let metrics = [
                    {{val: pm10, label: 'PM10', unit: 'μg/m³'}},
                    {{val: pm25, label: 'PM2.5', unit: 'μg/m³'}},
                    {{val: no2, label: 'NO2', unit: 'ppb'}},
                    {{val: so2, label: 'SO2', unit: 'ppb'}},
                    {{val: o3, label: 'O3', unit: 'ppb'}},
                    {{val: co, label: 'CO', unit: 'ppm'}},
                    {{val: temp, label: '溫度', unit: '°C'}},
                    {{val: humid, label: '濕度', unit: '%'}},
                    {{val: wd, label: '風向', unit: '°'}},
                    {{val: ws, label: '風速', unit: 'm/s'}}
                ];
                let rowsHtml = "";
                metrics.forEach(m => {{
                    if (m.val && m.val !== "N/A") {{
                        rowsHtml += `<tr style='border-bottom: 1px solid #eee;'><td style='color: #666; padding: 2px 0;'>${{m.label}}</td><td style='text-align: right;'><b>${{m.val}}</b> <span style='font-size: 10px; color: #888;'>${{m.unit}}</span></td></tr>`;
                    }}
                }});
                
                let tooltip_html = `<div style='font-family: "Segoe UI", Arial, sans-serif; font-size: 13px; width: 170px; background-color: transparent;'>
                    <div class='drag-header' style='cursor: move; font-size: 14px; font-weight: bold; color: #333; margin-bottom: 5px; border-bottom: 2px solid #27ae60; padding-bottom: 3px;'>
                        📍 ${{base_name}} <span style='font-size:10px;color:#666;'>(特殊工業區)</span>
                    </div>
                    <table style='width: 100%; border-collapse: collapse;'>
                        ${{rowsHtml}}
                    </table>
                    <div style='margin-top: 6px; font-size: 10px; color: #999; text-align: center;'>
                        🕒 擷取時間: ${{dt_str}}
                    </div>
                </div>`;

                let marker = L.marker(targetIndPts[base_name], {{
                    icon: L.AwesomeMarkers.icon({{icon: 'caret-up', markerColor: 'green', prefix: 'fa', extraClasses: 'fa-rotate-0'}})
                }});
                
                marker.bindPopup(tooltip_html, {{maxWidth: 220, autoClose: false, closeOnClick: false, className: 'draggable-popup'}});
                marker.on('popupopen', window.makePopupDraggable);
                marker.addTo(layerGroup);
            }});
        }})
        .catch(err => console.error("Error fetching Industrial APIs:", err));
}});
</script>
"""
m.get_root().html.add_child(folium.Element(js_code_ind))

# CWA Station Layer
fg_cwa = folium.FeatureGroup(name='氣象署測站')
for name, pos in cwa_pts.items():
    folium.Marker(
        location=pos, tooltip=name,
        icon=folium.Icon(color="orange", icon="cloud", prefix="fa")
    ).add_to(fg_cwa)

# Add layers to the map
fg_fab.add_to(m)
fg_env.add_to(m)
fg_ind.add_to(m)
fg_cwa.add_to(m)

# 5. Add interactive plugins
folium.LayerControl(collapsed=False).add_to(m)
plugins.Fullscreen().add_to(m)
plugins.MousePosition().add_to(m)
plugins.MeasureControl(position='topleft', primary_length_unit='kilometers', secondary_length_unit='meters', primary_area_unit='sqmeters', active_color='red', completed_color='red').add_to(m)

# 6. Save
output = "index.html"
m.save(output)
print(f"✅ Corrected map generated: {output}")