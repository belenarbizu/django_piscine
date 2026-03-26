import sys
import antigravity

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Args must be 3: latitude, longitude and date")
        exit(1)
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3]
        if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
            print("Invalid coordinates")
            exit(1)
        antigravity.geohash(latitude, longitude, date.encode())
    except Exception as e:
        print(e)
        exit(1)
