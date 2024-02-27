import csv
import glob 

pattern = "SIRS*"
files = glob.glob(pattern)

grade_sum = 0
tanni = 0
aRatio = 0
for file in files:
    with open (file)as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[7]=='A+'):
                grade = 4+0.3
                aRatio += 1*float(row[4])
            elif(row[7]=='A'):
                grade = 3+1
                aRatio += 1*float(row[4])
            elif(row[7]=='B'):
                grade = 2+1
            elif(row[7]=='C'):
                grade = 1+1
            elif(row[7]=='D'):
                grade = 0
            else:
                continue
            grade_sum += grade * float(row[4])
            tanni += float(row[4])
        aRatio /= tanni
    print(f'ファイル名:{file.name}, GPA:{grade_sum / tanni}, Aの割合:{aRatio}')
