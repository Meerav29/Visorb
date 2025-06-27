from skyfield.api import load, EarthSatellite

def load_satellite_from_tle(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    name = lines[0].strip()
    satellite = EarthSatellite(lines[1], lines[2], name)
    return satellite

def get_positions(satellite, duration_minutes=90, step_seconds=60):
    ts = load.timescale()
    times = ts.utc(2024, 6, 26, 0, range(0, duration_minutes))
    geocentric = satellite.at(times)
    x, y, z = geocentric.position.km
    return times, x, y, z