import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon=list(data["LON"])
name  = list(data["NAME"])
elev = list(data["ELEVATION"])
html = """<h4> Volcano information: </h4>
Height: %s m
"""
def color_producer(elevation):
    if elevation == "-":
        return'purple'
    else:
        ele = float(elevation)
        if ele < 1000.0:
            return'darkblue'
        elif ele < 2000.0:
            return'orange'
        else:
            return'red'

def pop_return(name,elevation):
    if elevation == "-":
        return name
    else:
        return name + " "+ elevation+" ft"

map = folium.Map(location = [22.895985, 77.757801],zoom_start=6,tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,nm,el in zip(lat,lon,name,elev):
    fgv.add_child(folium.Marker(location = [lt,ln],radius=8.0, tooltip=pop_return(nm,el),
    icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
    style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("India.html")
