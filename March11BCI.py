# Getting Values and Printing
import csv
import decimal

# Getting Time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")

# Importing Data
csv.register_dialect('myDialect',
                     delimiter=',',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)
count: int = 0
valence: float = 0

with open('Data/train_valence.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        valence = valence + float(row[0])
        count = count + 1
        if count == 5:
            break

count: int = 0
arousal: float = 0
with open('Data/train_arousal.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        arousal = float(row[0]) + float(row[0])
        count = count + 1
        if count == 5:
            break

# Rounding and Mean
round_num = valence
valencefirstrounded_val = decimal.Decimal(round_num).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_HALF_DOWN)
valencequotient = valencefirstrounded_val /5
round_num = valencequotient
valencefinal_val = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_DOWN)
print("Mean Of Frequency (Valence): ", valencefinal_val)


round_num = arousal
arousalfirstrounded_val = decimal.Decimal(round_num).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_HALF_DOWN)
arousalquotient = arousalfirstrounded_val /5
round_num = arousalquotient
arousalfinal_val = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_DOWN)
print("Mean of Frequency (Arousal): ", arousalfinal_val)

# If Statements
if 0.14 < valencefinal_val <= -0.10 and 0.74 < arousalfinal_val <= -0.84:
    emotion1 = "Afraid"
    print(current_time + " - " + emotion1)

elif 0.76 <= valencefinal_val < 0.80 and -0.73 <= arousalfinal_val <= -0.63:
    emotion2 = "Calm"
    print(current_time + " - " + emotion2)

elif 0.79 <= valencefinal_val <= 0.83 and -0.60 <= arousalfinal_val <= -0.50:
    emotion3 = "Content"
    print(current_time + " - " + emotion3)

elif -0.70 <= valencefinal_val <= 0.30 and -0.37 <= arousalfinal_val <= -0.27:
    emotion4 = "Discontent"
    print(current_time + " - " + emotion4)

elif 0.87 <= valencefinal_val <= 0.19 and 0.12 <= arousalfinal_val <= 0.22:
    emotion5 = "Happy"
    print(current_time + " - " + emotion5)

elif 0.88 <= valencefinal_val <= 0.10 and 0.03 <= arousalfinal_val <= 0.13:
    emotion6 = "Good"
    print(current_time + " - " + emotion6)

elif 0.037 <= valencefinal_val <= -0.04 and -0.11 <= arousalfinal_val <= -0.01:
    emotion7 = "Impressed"
    print(current_time + " - " + emotion7)

elif -0.82 <= valencefinal_val <= -0.78 and -0.08 <= arousalfinal_val <= 0.02:
    emotion8 = "Disappointed"
    print(current_time + " - " + emotion8)

elif -0.37 <= valencefinal_val <= -0.33 and -0.83 <= arousalfinal_val <= -0.73:
    emotion9 = "Bored"
    print(current_time + " - " + emotion9)

elif -0.20 <= valencefinal_val <= -0.16 and 0.78 <= arousalfinal_val <= 0.88:
    emotion10 = "Enraged"
    print(current_time + " - " + emotion10)

elif -0.07 <= valencefinal_val <= -0.03 and -0.70 <= arousalfinal_val <= -0.60:
    emotion11 = "Melancholy"
    print(current_time + " - " + emotion11)

elif -0.73 <= valencefinal_val <= -0.69 and 0.50 <= arousalfinal_val <= 0.60:
    emotion12 = "Distressed"
    print(current_time + " - " + emotion12)

elif -0.09 <= valencefinal_val <= -0.05 and -0.37 <= arousalfinal_val <= -0.27:
    emotion13 = "Worried"
    print(current_time + " - " + emotion13)

elif -0.20 <= valencefinal_val <= -0.12 and -0.17 <= arousalfinal_val <= -0.07:
    emotion14 = "Apathetic"
    print(current_time + " - " + emotion14)

elif 0.56 <= valencefinal_val <= 0.60 and -0.65 <= arousalfinal_val <= -0.55:
    emotion15 = "Contemplative"
    print(current_time + " - " + emotion15)

elif -0.83 <= valencefinal_val <= -0.79 and -0.45 <= arousalfinal_val <= -0.35:
    emotion16 = "Sad"
    print(current_time + " - " + emotion16)

elif 0.87 <= valencefinal_val <= 0.91 and -0.15 <= arousalfinal_val <= -0.05:
    emotion16 = "Pleased"
    print(current_time + " - " + emotion16)

else:
    print('Child was okay , and no outlier emotions were detected', " - "+current_time )
