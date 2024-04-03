import plotly.express as px

from die import Die 

#Cria dois dados D6
die_1 = Die()
die_2 = Die(10)

#Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analisa os resultados 
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza os resultados 
title = "Results of Rolling two D6 dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#Personaliza ainda mais o grafico
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice_visual_d6d10.html')
