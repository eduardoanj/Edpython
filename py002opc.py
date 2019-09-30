print('='*60)


salario = float(input('{}Digite o salário: '.format(' '*5)))

####################################### A conta pode ser feita no format
###################################o 8 do {:8.2f} serve para a formatação
print('{}o salario liquido é: {}R${:8.2f},'.format(' '*5,' '*9, salario))
print('{}Os gastos E: {}R${:8.2f}'.format(' '*5, ' '*17, salario*0.5 ))
print('{}Investimentos LP: {}R${:8.2f}'.format(' '*5, ' '*12, salario *0.2))
print('{}Investimentos CP: {}R${:8.2f}'.format(' '*5, ' '*12, salario *0.1))
print('{}Livre: {}R${:8.2f}'.format(' '*5, ' '*23, salario *0.2))


''
######### o *60 é para repetir 60 vezes a string
print('='*60)