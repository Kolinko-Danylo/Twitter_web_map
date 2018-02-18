from geopy.geocoders import ArcGIS


def location(place):
    """
    str -> (float, float)
    Return the latitude and the longitude of the place.
    """
    location = ArcGIS(timeout=100).geocode(place)
    return [location.latitude, location.longitude]
