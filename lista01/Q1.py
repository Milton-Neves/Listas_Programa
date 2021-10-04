meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('\n #######################################')

temperatura = []

print('Informe a tempertura média de cada mês \n')

media = 0
acimaMedia = {}
for i in range(len(meses)):
	temperatura.append(float(input('Mês de ' + meses[i] + ':\n')))
	media += temperatura[i]
media = media/len(meses)

for i in range(len(meses)):
	if(temperatura[i] > media):
		acimaMedia.update({meses[i] : temperatura[i]})


print('>>>> Media ANUAL das temperaturas: ' + str(media))
print('>>>> Meses com temperaturas acima da media: ' + str(acimaMedia))