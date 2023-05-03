from upsetplot import plot
import pandas as pd

df = pd.read_csv('C:/Users/oriol.medina/PycharmProjects/pythonProject/x.csv', on_bad_lines='skip', sep=';')
df2 = pd.DataFrame()

zona_urbana = []
victimes_mortals = []
boira = []

# transform to true/false
for i in range(len(df['zona'])):
    if df['zona'][i] == 'Zona urbana':
        zona_urbana.append(True)
    else:
        zona_urbana.append(False)

for i in range(len(df['F_MORTS'])):
    if df['F_MORTS'][i] > 0:
        victimes_mortals.append(True)
    else:
        victimes_mortals.append(False)

for i in range(len(df['D_BOIRA'])):
    if df['D_BOIRA'][i] == 'Si':
        boira.append(True)
    else:
        boira.append(False)

df2['zona_urbana'] = zona_urbana
df2['victimes_mortals'] = victimes_mortals
df2['boira'] = boira

#print(df2)

# Using GroupBy & count() on multiple column
df3 = df2.groupby(['zona_urbana','victimes_mortals', 'boira'])['boira'].count()
print(df3)
plot(df3)

