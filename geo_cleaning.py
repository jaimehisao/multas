import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="geo_cleaning")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def clean_address(address):
    location = geocode(address)
    return location.address
