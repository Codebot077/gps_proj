import csv
import xml.etree.ElementTree as ET


def extract_coordinates_from_kml(kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    coordinates = []

    # Find all coordinates within Placemark elements
    for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
        name = placemark.find('{http://www.opengis.net/kml/2.2}name').text
        coordinates_str = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates').text

        # Extract latitude, longitude, and altitude
        lon, lat, alt = coordinates_str.strip().split(',')

        coordinates.append([name, float(lat), float(lon), float(alt)])

    return coordinates

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Latitude', 'Longitude', 'Altitude'])
        writer.writerows(data)

if __name__ == "__main__":
    # var  = os.get_exec_path("as.exe")
    kml_file = r'25feb-02.kml'
    output_csv = r'output_coordinates.csv'

    extracted_coordinates = extract_coordinates_from_kml(kml_file)
    write_to_csv(extracted_coordinates, output_csv)
