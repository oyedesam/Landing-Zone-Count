import sys
import boto3
import datetime
from halo import Halo
from collections import defaultdict

s3 = boto3.resource('s3')
bucketName = sys.argv[1]
bucket = s3.Bucket(bucketName)
bucketPath = sys.argv[2]

if len(sys.argv) < 2 or not sys.argv[1]:
    raise ValueError("Bucket name must be provided as a command-line argument")

spinner = Halo()
spinner.start()
spinner.text = 'Getting objects in folder...'

prefix = bucketPath
objects = list(bucket.objects.filter(Prefix=prefix))

# Sort objects by last_modified time
objects.sort(key=lambda obj: obj.last_modified)

objects_by_period = defaultdict(list)
total_count = 0

# Use the last_modified time of the first object as the start time
start_time = objects[0].last_modified

for obj in objects:
    period_number = (obj.last_modified - start_time).days
    objects_by_period[period_number].append(obj)
    total_count += 1

spinner.stop()

with open('results.html', 'w') as f:
    f.write('<html><body>\n')
    f.write('<table border="1">\n')
    f.write('<tr><th>Bucket</th><th>Number of Objects</th><th>Period Start Time</th><th>Period End Time</th></tr>\n')
    for period_number, objs in objects_by_period.items():
        # Calculate the start and end time of the 24-hour period
        period_start_time = start_time + datetime.timedelta(days=period_number)
        period_end_time = period_start_time + datetime.timedelta(days=1)

        # Format the start and end time as strings with AM/PM
        period_start_time_str = period_start_time.strftime('%Y-%m-%d %I:%M:%S %p')
        period_end_time_str = period_end_time.strftime('%Y-%m-%d %I:%M:%S %p')

        f.write(f'<tr><td>{bucketName}/{prefix}</td><td>{len(objs)}</td><td>{period_start_time_str}</td><td>{period_end_time_str}</td></tr>\n')

    f.write('</table>\n')
    f.write(f'<p>Total number of objects in {prefix}: {total_count}</p>\n')
    f.write('</body></html>\n')
    print("Done! Check results.html for more details.")