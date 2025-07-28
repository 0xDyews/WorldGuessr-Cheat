# Made by Dyews: https://github.com/0xDyews <3

from mitmproxy import http
import json
import webbrowser

opened_coords = set()

def response(flow: http.HTTPFlow) -> None:
    if flow.request.method == "POST" and "/$rpc/google.internal.maps.mapsjs.v1.MapsJsInternalService/SingleImageSearch" in flow.request.path:
        try:
            data = json.loads(flow.request.get_text())
            coords = None

            for part in data:
                if isinstance(part, list):
                    for item in part:
                        if isinstance(item, list) and len(item) >= 4:
                            lat, lon = item[2], item[3]
                            if isinstance(lat, float) and isinstance(lon, float):
                                coords = f"{lat},{lon}"
                                break
                    if coords:
                        break

            if coords and coords not in opened_coords:
                opened_coords.add(coords)
                lat, lon = coords.split(',')
                gmap_link = f"https://www.google.com/maps/place/{lat},{lon}/@{lat},{lon},5z"
                print(f"[+] Opening Google Maps: {gmap_link}")
                webbrowser.open_new_tab(gmap_link)

        except Exception as e:
            print(f"[!] Error parsing coordinates: {e}")
