from flask import Flask, render_template, request
import folium
import requests
from math import sqrt
from restaurants_rec import restaurants, a_star_search, bfs

USER_LOCATION = (-7.291540, 112.804618)

def calculate_distance(loc1, loc2):
    return sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2) * 111

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    map_html = None
    best_restaurants = []
    search_times = []
    warning_msg = None
    user_location = USER_LOCATION

    if request.method == 'POST':
        # Geolocation (JS)
        try:
            user_lat = float(request.form.get('user_lat'))
            user_lon = float(request.form.get('user_lon'))
            loc_geo = (user_lat, user_lon)
        except (TypeError, ValueError):
            loc_geo = None
        
        # Manual input
        try:
            manual_lat = float(request.form.get('manual_lat'))
            manual_lon = float(request.form.get('manual_lon'))
            loc_manual = (manual_lat, manual_lon)
        except (TypeError, ValueError):
            loc_manual = None

        # Choose best location
        if loc_geo and loc_manual:
            dist = calculate_distance_km(loc_geo, loc_manual)
            if dist > 2:  # 2 km threshold, adjust as needed
                user_location = loc_manual
                warning_msg = "Auto-detected location and manual input are quite far apart. Using your manual coordinates."
            else:
                user_location = loc_geo
        elif loc_geo:
            user_location = loc_geo
        elif loc_manual:
            user_location = loc_manual
        else:
            user_location = USER_LOCATION

        # Ambil input lain
        priority = request.form.get('priority')
        min_rating = float(request.form.get('min_rating'))
        max_distance = float(request.form.get('max_distance'))
        budget = int(request.form.get('budget')) * 1000

        if priority == "rating":
            best_restaurants, search_times = a_star_search(user_location, restaurants, min_rating, max_distance, budget)
            best_restaurants.sort(key=lambda x: x['rating'], reverse=True)
            best_restaurants = best_restaurants[:5]  # batasi 5 besar, opsional
        else:
            best_restaurants, search_times = bfs(user_location, restaurants)    
            for r in best_restaurants:
                r['distance_from_user'] = calculate_distance(user_location, r["location"])

        # Create map
        m = folium.Map(location=user_location, zoom_start=14)
        folium.Marker(
            location=user_location,
            popup=f"Your location used:<br>Lat: {user_location[0]:.6f}<br>Lon: {user_location[1]:.6f}",
            icon=folium.Icon(color="blue", icon="user")
        ).add_to(m)

        # All restaurants (gray, or thumbs-up if recommended)
        for r in restaurants:
            if r.get("recommended", False):
                icon = folium.Icon(color="orange", icon="thumbs-up", prefix='fa')
                popup = f"👍 <b>{r['name']}</b>: Rating {r['rating']}, Price: {r['price_range']}"
            else:
                icon = folium.Icon(color="gray", icon="cutlery")
                popup = f"{r['name']}: Rating {r['rating']}, Price: {r['price_range']}"
            folium.Marker(
                location=r["location"],
                popup=popup,
                icon=icon
            ).add_to(m)

        # Highlight best restaurants
        for r in best_restaurants:
            folium.Marker(
                location=r["location"],
                popup=f"{r['name']}: Rating {r['rating']}, Price: {r['price_range']}",
                icon=folium.Icon(color="green" if r["rating"] >= 4.5 else "red", icon="cutlery")
            ).add_to(m)

            # Route (optional)
            route_url = f"http://router.project-osrm.org/route/v1/driving/{user_location[1]},{user_location[0]};{r['location'][1]},{r['location'][0]}?overview=full&geometries=geojson"
            route_response = requests.get(route_url)
            route_data = route_response.json()
            if "routes" in route_data and route_data["routes"]:
                route_points = route_data["routes"][0]["geometry"]["coordinates"]
                route_points = [(point[1], point[0]) for point in route_points]
                folium.PolyLine(route_points, color="blue", weight=4, opacity=0.7).add_to(m)

        map_html = m._repr_html_()

    return render_template('index.html', map_html=map_html, warning_msg=warning_msg, best_restaurants=best_restaurants)

if __name__ == '__main__':
    app.run(debug=True)
