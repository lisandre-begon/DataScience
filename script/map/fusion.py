import borne_map as bm
import immatr_map as im
import folium

borne_map = bm.get()
immatr_map = im.get()

# Create a map centered on France

for i in range(len(borne_map)):
    t = len(borne_map)-len(immatr_map)
    print("t : "+t)
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    borne_map[i].add_to(m)
    if i >= t:
        immatr_map[i].add_to(m)
    folium.LayerControl().add_to(m)

    m.save("fusion/fusiooon"+str(i)+".html")

