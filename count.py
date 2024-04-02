import sys
import boto3
from halo import Halo
from collections import defaultdict


s3 = boto3.resource('s3')
bucket = s3.Bucket(sys.argv[1])
bucketPath = sys.argv[2]


if len(sys.argv) < 2 or not sys.argv[1]:
    raise ValueError("Bucket name must be provided as a command-line argument")


spinner = Halo()
spinner.start()
spinner.text = 'Getting objects in folder...'

prefix = bucketPath
objects = list(bucket.objects.filter(Prefix=prefix))

objects_by_date = defaultdict(list)
total_count = 0


for obj in objects:
    date = obj.last_modified.strftime('%Y-%m-%d')
    objects_by_date[date].append(obj)
    total_count += 1



spinner.stop()

for date, objs in objects_by_date.items():
    print(f'Number of objects: {len(objs)} uploaded on Date: {date} ')


print(f'Total number of objects in {prefix}: {total_count}')





