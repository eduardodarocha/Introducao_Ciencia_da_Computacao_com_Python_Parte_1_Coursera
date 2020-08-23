dado = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dia = dado // 86400
segundosrest = dado % 86400
hora = segundosrest // 3600
segundosrest2 = segundosrest % 3600
minuto = segundosrest2 // 60
segundosrest3 = segundosrest2 % 60
print(f'{dia} dias, {hora} horas, {minuto} minutos e {segundosrest3} segundos.')