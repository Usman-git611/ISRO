import osmnx as ox

def fetch_urban_geometry(place_name="Kolkata, India"):
    print(f"Fetching building maps for {place_name}...")
    try:
        buildings = ox.geometries_from_place(place_name, tags={"building": True})
        building_area = buildings.geometry.area.sum()
        print(f"Success! Total building footprint area: {building_area:.2f} sq meters")
        return buildings
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    fetch_urban_geometry()
