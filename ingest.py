# Run with the Django shell loaded!
#   python manage.py shell < ingest.py

import csv
from device_tracker.models import Device, DeviceLocation

file_in = open('sample_data.csv', 'r')

csv_file = csv.DictReader(file_in)

# for each row in our CSV file...
for row in csv_file:
    # Step 1: Look up the device that's listed in the row
    device = Device.objects.get_or_create(id=row['device_id'])

    # Step 2: Create a location record for this device
    device_location_obj, created = DeviceLocation.objects.get_or_create(
        device=device,
        timestamp=row['timestamp'],
        latitude=row['latitude'],
        longitude=row['longitude']
    )

    if created:
        print(f"New record created for {device_location_obj.device} at {device_location_obj.timestamp}")
