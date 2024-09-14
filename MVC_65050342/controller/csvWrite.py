import csv

csv_path ="model/dbms.csv"

def write_csv(cowId, cowColor, cowAge):
    #เพิ่มinputที่userกรอกลงในdbms.csv
    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([cowId, cowColor, cowAge])
