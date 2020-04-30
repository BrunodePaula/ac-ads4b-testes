_all_ = ('calcular_ir', 'calcular_inss')

def calcular_inss(salario):
	if salario < 1830.29: 
		porcentagem_desconto_inss = 8
	if salario >= 1830.30 and salario < 3050.52: 
		porcentagem_desconto_inss = 9
	if salario >= 3050.53 and salario < 6101.06: 
		porcentagem_desconto_inss = 11
	return salario * porcentagem_desconto_inss / 100.0

def calcular_ir(salario, desconto_inss):
	base_calculo_ir = salario - desconto_inss

	if base_calculo_ir < 1637.12:
		return 0

	if base_calculo_ir >= 1903.99 and base_calculo_ir < 2826.65: 
		porcentagem_desconto_ir = 7.5
		deducao_imposto = 142.80

	if base_calculo_ir >= 2826.66 and base_calculo_ir < 3751.05: 
		porcentagem_desconto_ir = 15
		deducao_imposto = 354.80

	if base_calculo_ir >= 3751.06 and base_calculo_ir < 4664.68: 
		porcentagem_desconto_ir = 22.5
		deducao_imposto = 636.13

	if base_calculo_ir >= 4664.69: 
		porcentagem_desconto_ir = 27.5
		deducao_imposto = 869.36

	return (base_calculo_ir * porcentagem_desconto_ir / 100.0) - deducao_imposto
