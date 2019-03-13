import csv
import tempfile
import os

with tempfile.TemporaryDirectory() as dr:
    temp_path = os.path.join(dr, 'sample.csv')
    with open(temp_path, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['aa', 'bb', 'cc'])
        writer.writerow(['11', '22', '33'])
        writer.writerow(['AA', 'BB', 'CC'])

    with open(temp_path, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)