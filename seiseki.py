import csv
import glob 
import sys

pattern = "SIRS*"
files = glob.glob(pattern)

if not files:
    print("ファイルが見つかりません")
    sys.exit(1)


for file_name in files:
    gpa = 0
    grade_sum = 0
    tanni = 0
    aa_a_ratio = 0
    aa_ratio = 0
    a_ratio = 0
    b_ratio = 0
    c_ratio = 0
    d_ratio = 0
    with open (file_name)as file:
        reader = csv.reader(file)

        for row in reader:
            if(row[7]=='A+'):
                grade = 4.3
                aa_ratio += 1*float(row[4])
            elif(row[7]=='A'):
                grade = 4
                a_ratio += 1*float(row[4])
            elif(row[7]=='B'):
                grade = 3
                b_ratio += 1*float(row[4])
            elif(row[7]=='C'):
                grade = 2
                c_ratio += 1*float(row[4])
            elif(row[7]=='D'):
                grade = 0
                d_ratio += 1*float(row[4])
            else:
                continue
            grade_sum += grade * float(row[4])
            tanni += float(row[4])

    print(f'ファイル名:{file.name}, A+:{aa_ratio}単位, A:{a_ratio}単位, B:{b_ratio}単位, C:{c_ratio}単位, D:{d_ratio}単位')
    if(tanni != 0): 
        aa_a_ratio = (aa_ratio + a_ratio)/tanni
        aa_ratio /= tanni
        a_ratio /= tanni
        b_ratio /= tanni
        c_ratio /= tanni
        d_ratio /= tanni
        gpa = grade_sum / tanni
            
    print(f'ファイル名:{file.name}, GPA:{gpa:.2f}, A以上:{aa_a_ratio:.2f}, A+:{aa_ratio:.2f}, A:{a_ratio:.2f}, B:{b_ratio:.2f}, C:{c_ratio:.2f}, D:{d_ratio:.2f}')
