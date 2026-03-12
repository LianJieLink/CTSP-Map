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

# --- 3. Station Coordinates ---
# MOENV Stations (Blue Asterisk)
env_pts = {
    "沙鹿站": [24.225628, 120.568794],
    "西屯站": [24.162197, 120.616917],
    "忠明站": [24.151958, 120.641092],
    "楠梓站": [22.733667, 120.328289],
    "左營站": [22.674861, 120.292917],
    "仁武站": [22.689056, 120.332631],
    "龍潭": [24.86400048, 121.21645772],
    "新竹": [24.8056356, 120.97236752],
    "頭份": [24.69690679, 120.89869286],
    "朴子": [23.46538, 120.2478],
    "嘉義": [23.46477865, 120.44125148],
    "新港": [23.554839, 120.345531],
    "善化": [23.11337642, 120.29740529],
    "安南": [23.048197, 120.2175]
}

# SP Industrial Stations (Green Triangle)
ind_pts = {
    "中科陽明(陽明國小)": [24.22139, 120.63194], 
    "中科國安(國安國小)": [24.19361, 120.60861], 
    "中科公園(都會公園)": [24.21111, 120.59833], 
    "中科實中(實驗中學)": [24.22944, 120.62583],
    "宏毅社區(空品車)": [22.71329, 120.30849],
    "竹科龍潭(環保中心)": [24.887787, 121.1883272],
    "竹科德龍(德龍國小)": [24.882046, 121.195207],
    "竹科聖德(聖德里)": [24.889177, 121.201821],
    "竹科新安(新安)": [24.784714, 120.991939],
    "竹科靜心(靜心湖)": [24.778281, 121.013773],
    "竹科力行(力行)": [24.76637, 121.016265],
    "竹科興業(興業)": [24.77806, 120.989786],
    "竹科南東": [24.70966, 120.92154],
    "竹科南西": [24.71361, 120.91031],
    "竹科南南": [24.70611, 120.91282],
    "竹科南北": [24.70817, 120.89529],
    "六輕東石(嘉義東石)": [23.46248333, 120.172425],
    "南科公13": [23.09003889, 120.2845694],
    "南科公19": [23.12582, 120.26943],
    "南科公29": [23.10635, 120.2692611],
    "南科實中": [23.10739722, 120.2912611]
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

# --- 4. Draw Layers ---

# Factory Layer
fg_fab = folium.FeatureGroup(name='廠區範圍')
for coords, name in [(tsmc_15a_poly, "台積電 15A 廠"),
                     (tsmc_15b_poly, "台積電 15B 廠"),
                     (tsmc_ap5_poly, "台積電 AP5 廠"),
                     (zero_waste_poly, "台中零廢製造中心"),
                     (tsmc_F22_poly, "台積電 F22 廠"),
                     (tsmc_AP3_poly, "台積電 AP3 廠"),
                     (tsmc_AP6_poly, "台積電 AP6 廠")]:
    folium.Polygon(
        locations=coords, color="red", weight=2,
        fill=True, fill_color="red", fill_opacity=0.4,
        tooltip=name, popup=f"<b>{name}</b>"
    ).add_to(fg_fab)

# MOENV Layer
fg_env = folium.FeatureGroup(name='環境部測站')
for name, pos in env_pts.items():
    folium.Marker(
        location=pos, tooltip=name,
        icon=folium.Icon(color="blue", icon="star", prefix="fa")
    ).add_to(fg_env)

# Industrial Station Layer
fg_ind = folium.FeatureGroup(name='特殊性工業區測站')
for name, pos in ind_pts.items():
    folium.Marker(
        location=pos, tooltip=name,
        icon=folium.Icon(color="green", icon="caret-up", prefix="fa")
    ).add_to(fg_ind)

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