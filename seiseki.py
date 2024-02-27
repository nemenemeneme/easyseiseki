import csv
import glob 
import sys

pattern = "SIRS*"
files = glob.glob(pattern)

if not files:
    print("ファイルが見つかりません")
    sys.exit(1)

grade_sum = 0
tanni = 0
a_ratio = 0
for file_name in files:
    with open (file_name)as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[7]=='A+'):
                grade = 4.3
                a_ratio += 1*float(row[4])
            elif(row[7]=='A'):
                grade = 4
                a_ratio += 1*float(row[4])
            elif(row[7]=='B'):
                grade = 3
            elif(row[7]=='C'):
                grade = 2
            elif(row[7]=='D'):
                grade = 0
            else:
                continue
            grade_sum += grade * float(row[4])
            tanni += float(row[4])
        if(tanni != 0): 
            a_ratio /= tanni
            gpa = grade_sum / tanni
        else:
            a_ratio = 0
            gpa = 0
    print(f'ファイル名:{file.name}, GPA:{gpa}, Aの割合:{a_ratio}')
