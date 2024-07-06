#=================================================================
#  Titulo: O problema dos radares.
#  Objetivo: Aprender/revisar conceitos básicos de linguagem de programação
#
#  Descrição: Uma determinada cidade possui alguns 3 radares de velocidade. O radares emitem relatórios constantes
#  que são unificados e analisados antes de serem emitidas multas de transito. Abaixo segue um desses relatorios
#
#  Radar    placa     vel_auf  vel_perm  tipo_veiculo  
#  r1        BEE4R22   70.00         60         comum
#  r1        DKR5Y21   67.00         60      especial
#  r1        ABX4I22   60.00         60         comum
#  r1        ABT8I78   67.01         60         comum
#  r2        VXX0f74   56.90         80         comum
#  r2        AKR7T45   87.00         80         comum
#  r2        ADD1G78   89.90         80         comum
#  r2        CFG3J77   73.89         80         comum
#  r3        ERR3J79   73.89        100         comum
#  r3        ERP1J22   65.89        100         comum
#  r3        BNG9J99  110.89        100      especial
#  r3        ABT8I78  110.98        100         comum
#
# Dados que :
#  vel-auf : Velocidade que foi verificada no momento em que o carro passou no radar
#  vel_perm: A velocidade máxima que a via permite
#  tipo_veiculo: 
#         Comum - Veiculos comuns de cidadãos que podem ser multados
#      especial - Veiculos que não podem ser multados como carros de polícia e ambulancias
#
# Faça um programa que 
#  - Mostre os veiculos que devem ser multados
#  - A saida deverá ser no seguinte formato
#    Placa   - %excesso - Radar
#    ADD1G78 - 12,37    - r2
# 
# Considerações
#
#  - Existe uma margem de tolerancia de 7km/h para radares até 100km/h. 
#    Ou seja se o limite for 80, veiculos que trafegarem em até 87 km/h 
#    não devem ser multados
#  - Porcentagem_excesso = [(vel_auf - vel_perm)/vel_perm] * 100
#
#================================================================= 

registroVeiculo = [
    ['r1', 'BEE4R22', 70.00, 60, 'comum'],
    ['r1', 'DKR5Y21', 67.00, 60, 'especial'],
    ['r1', 'ABX4I22', 60.00, 60, 'comum'],
    ['r1', 'ABT8I78', 67.01, 60, 'comum'],
    ['r2', 'VXX0f74', 56.90, 80, 'comum'],
    ['r2', 'AKR7T45', 87.00, 80, 'comum'],
    ['r2', 'ADD1G78', 89.90, 80, 'comum'],
    ['r2', 'CFG3J77', 73.89, 80, 'comum'],
    ['r3', 'ERR3J79', 73.89, 100, 'comum'],
    ['r3', 'ERP1J22', 65.89, 100, 'comum'],
    ['r3', 'BNG9J99', 110.89, 100, 'especial'],
    ['r3', 'ABT8I78', 110.98, 100, 'comum'],
    ['r3', 'ABT8I74', 106, 101, 'comum']
]

print(type(registroVeiculo))
print(dir(registroVeiculo))

print("\nPLACA    - PCT    - RADAR")

# for i in range(0,len(registroVeiculo)):
for i in range(0, registroVeiculo.__len__()):
    codRadar = registroVeiculo[i][0]
    placa = registroVeiculo[i][1]
    velApurada = registroVeiculo[i][2]
    velPermitida = registroVeiculo[i][3] + 7 if registroVeiculo[i][3] < 100 else registroVeiculo[i][3]
    tipoVeiculo = registroVeiculo[i][4]

    # Porcentagem_excesso = [(vel_auf - vel_perm)/vel_perm] * 100
    porcentagemExcesso = (velApurada - float(velPermitida)) / float(velPermitida) * 100
    if tipoVeiculo == 'comum' and porcentagemExcesso > 0 and velApurada > velPermitida:
        print(f'{placa}  - {porcentagemExcesso:.2f}   - {codRadar}')

print("\nPLACA    - PCT    - RADAR")

for registro in registroVeiculo:
    # Porcentagem_excesso = [(vel_auf - vel_perm)/vel_perm] * 100
    porcentagemExcesso = (registro[2] - float(registro[3])) / float(registro[3]) * 100

    if registro[4] == 'comum' and porcentagemExcesso > 0:
        print(f'{registro[1]}  - {porcentagemExcesso:.2f}   - {registro[0]}')
