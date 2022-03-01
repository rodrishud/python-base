# Exercícios

## 1. Function para Análise de Indicadores

# A maioria das empresas tem suas próprias regras para cálculos de indicadores.

# - Algumas empresas definem que um cliente é considerado um cliente inadimplente quando ele está devendo acima de X reais e por mais de X dias.
# - Algumas empresas definem que um vendedor bateu a meta quando ele vendeu acima de X reais (outras ainda analisam não só as vendas desse vendedor, mas também da loja ou da unidade de negócios que ele faz parte, ou ainda uma avaliação qualitativa)
# - Algumas empresas definem que um produto está em "falta" no estoque quando ele está abaixo de um nível mínimo quando um cliente insere um novo pedido daquele produto
# - E assim vai para dezenas de indicadores.

# O ponto importante é, cada empresa tem alguma adaptação do cálculo de indicadores. E normalmente se formos analisar esses indicadores é interessante ter funções que façam todo o trabalho de análise deles. Por isso, vamos construir 2 exemplos aqui:

### Item 1: Crie uma função que calcula o percentual de Stockout de uma empresa

# - O % de stockout é dado por (Vendas Perdidas por Estoque) / (Vendas Concluídas + Vendas Perdidas por Estoque) -> essas vendas são dadas em valor total (dinheiro) e não em quantidade de vendas
# - Seu programa recebe um dicionário com todas as vendas da empresa, o status dela (se foi Concluída ou Cancelada) e, caso tenha sido Cancelada, o motivo de Cancelamento. O formato é o seguinte:

'''
    vendas = {
    'VE0001': (15000, 'Concluído', ''),
    'VE0002': (13300, 'Cancelado', 'Cancelado pelo Cliente'),
    'VE0003': (12000, 'Concluído', ''),
    ...
}
'''

# - Para reforçar: As vendas Canceladas por qualquer outro motivo que não seja a Falta de Estoque não devem ser consideradas para a conta do Stockout.

vendas = {'VE0001': (9868,'Concluído',''),'VE0002': (9642,'Concluído',''),'VE0003': (6007,'Concluído',''),'VE0004': (15562,'Concluído',''),'VE0005': (18752,'Cancelado','Estoque em Falta'),'VE0006': (16358,'Cancelado','Estoque em Falta'),'VE0007': (17045,'Concluído',''),'VE0008': (12230,'Concluído',''),'VE0009': (6747,'Concluído',''),'VE0010': (15114,'Concluído',''),'VE0011': (12497,'Concluído',''),'VE0012': (6001,'Concluído',''),'VE0013': (16227,'Cancelado','Cancelada pelo Cliente'),'VE0014': (16150,'Concluído',''),'VE0015': (17705,'Concluído',''),'VE0016': (9978,'Concluído',''),'VE0017': (4266,'Concluído',''),'VE0018': (11531,'Concluído',''),'VE0019': (10352,'Cancelado','Cancelada pelo Cliente'),'VE0020': (16544,'Concluído',''),'VE0021': (15488,'Concluído',''),'VE0022': (15828,'Concluído',''),'VE0023': (1218,'Concluído',''),'VE0024': (11560,'Concluído',''),'VE0025': (14220,'Concluído',''),'VE0026': (17839,'Concluído',''),'VE0027': (4050,'Concluído',''),'VE0028': (7594,'Cancelado','Estoque em Falta'),'VE0029': (19586,'Concluído',''),'VE0030': (8453,'Concluído',''),'VE0031': (3589,'Concluído',''),'VE0032': (13472,'Cancelado','Cancelada pelo Cliente'),'VE0033': (16994,'Concluído',''),'VE0034': (2139,'Concluído',''),'VE0035': (10173,'Concluído',''),'VE0036': (17784,'Cancelado','Estoque em Falta'),'VE0037': (12214,'Concluído',''),'VE0038': (5878,'Concluído',''),'VE0039': (2622,'Concluído',''),'VE0040': (9765,'Concluído',''),'VE0041': (8872,'Concluído',''),'VE0042': (16543,'Concluído',''),'VE0043': (8994,'Concluído',''),'VE0044': (4332,'Concluído',''),'VE0045': (19679,'Concluído',''),'VE0046': (14968,'Concluído',''),'VE0047': (6352,'Concluído',''),'VE0048': (11461,'Concluído',''),'VE0049': (5285,'Concluído',''),'VE0050': (11639,'Concluído',''),'VE0051': (6023,'Concluído',''),'VE0052': (4943,'Concluído',''),'VE0053': (5654,'Concluído',''),'VE0054': (11734,'Concluído',''),'VE0055': (2742,'Concluído',''),'VE0056': (5380,'Cancelado','Estoque em Falta'),'VE0057': (5578,'Concluído',''),'VE0058': (1897,'Concluído',''),'VE0059': (7857,'Concluído',''),'VE0060': (4472,'Concluído',''),'VE0061': (19874,'Concluído',''),'VE0062': (13323,'Cancelado','Cancelada pelo Cliente'),'VE0063': (5821,'Concluído',''),'VE0064': (4410,'Concluído',''),'VE0065': (16676,'Concluído',''),'VE0066': (10577,'Concluído',''),'VE0067': (10627,'Concluído',''),'VE0068': (1987,'Concluído',''),'VE0069': (13197,'Concluído',''),'VE0070': (15063,'Concluído',''),'VE0071': (14363,'Concluído',''),'VE0072': (10452,'Concluído',''),'VE0073': (15376,'Concluído',''),'VE0074': (4661,'Concluído',''),'VE0075': (13287,'Concluído',''),'VE0076': (8278,'Concluído',''),'VE0077': (7134,'Concluído',''),'VE0078': (16568,'Concluído',''),'VE0079': (17732,'Concluído',''),'VE0080': (5127,'Concluído',''),'VE0081': (4582,'Concluído',''),'VE0082': (14804,'Cancelado','Cancelada pelo Cliente'),'VE0083': (12362,'Concluído',''),'VE0084': (1148,'Concluído',''),'VE0085': (14018,'Concluído',''),'VE0086': (15891,'Concluído',''),'VE0087': (4517,'Concluído',''),'VE0088': (1770,'Concluído',''),'VE0089': (14926,'Concluído',''),'VE0090': (13627,'Concluído',''),'VE0091': (3047,'Concluído',''),'VE0092': (13924,'Concluído',''),'VE0093': (7158,'Concluído',''),'VE0094': (5942,'Concluído',''),'VE0095': (13480,'Concluído',''),'VE0096': (17686,'Concluído',''),'VE0097': (5722,'Cancelado','Cancelada pelo Cliente'),'VE0098': (16963,'Concluído',''),'VE0099': (14225,'Concluído',''),'VE0100': (12553,'Concluído',''),'VE0101': (18047,'Concluído',''),'VE0102': (11420,'Concluído',''),'VE0103': (6191,'Concluído',''),'VE0104': (8388,'Concluído',''),'VE0105': (17210,'Concluído',''),'VE0106': (12217,'Concluído',''),'VE0107': (8984,'Concluído',''),'VE0108': (7638,'Cancelado','Cancelada pelo Cliente'),'VE0109': (8462,'Concluído',''),'VE0110': (14081,'Concluído',''),'VE0111': (10842,'Concluído',''),'VE0112': (13261,'Concluído',''),'VE0113': (16953,'Cancelado','Estoque em Falta'),'VE0114': (5343,'Concluído',''),'VE0115': (4734,'Concluído',''),'VE0116': (13606,'Cancelado','Cancelada pelo Cliente'),'VE0117': (17106,'Cancelado','Estoque em Falta'),'VE0118': (17704,'Concluído',''),'VE0119': (12242,'Concluído',''),'VE0120': (7476,'Cancelado','Estoque em Falta'),'VE0121': (18408,'Concluído',''),'VE0122': (13612,'Concluído',''),'VE0123': (18198,'Concluído',''),'VE0124': (4844,'Concluído',''),'VE0125': (12750,'Concluído',''),'VE0126': (11969,'Concluído',''),'VE0127': (15337,'Concluído',''),'VE0128': (1100,'Concluído',''),'VE0129': (18893,'Concluído',''),'VE0130': (15850,'Concluído',''),'VE0131': (2097,'Concluído',''),'VE0132': (11636,'Cancelado','Estoque em Falta'),'VE0133': (12603,'Concluído',''),'VE0134': (10769,'Concluído',''),'VE0135': (11016,'Concluído',''),'VE0136': (14556,'Concluído',''),'VE0137': (1389,'Concluído',''),'VE0138': (11681,'Concluído',''),'VE0139': (16759,'Cancelado','Cancelada pelo Cliente'),'VE0140': (16317,'Concluído',''),'VE0141': (5965,'Concluído',''),'VE0142': (4493,'Concluído',''),'VE0143': (5398,'Concluído',''),'VE0144': (9875,'Concluído',''),'VE0145': (17492,'Concluído',''),'VE0146': (7473,'Concluído',''),'VE0147': (10284,'Concluído',''),'VE0148': (10778,'Concluído',''),'VE0149': (2227,'Concluído',''),'VE0150': (14157,'Concluído',''),'VE0151': (9516,'Concluído',''),'VE0152': (9824,'Concluído',''),'VE0153': (5118,'Concluído',''),'VE0154': (5123,'Concluído',''),'VE0155': (2697,'Concluído',''),'VE0156': (19024,'Concluído',''),'VE0157': (5128,'Concluído',''),'VE0158': (8293,'Cancelado','Estoque em Falta'),'VE0159': (18782,'Concluído',''),'VE0160': (12182,'Concluído',''),'VE0161': (9063,'Concluído',''),'VE0162': (17608,'Concluído',''),'VE0163': (8456,'Cancelado','Cancelada pelo Cliente'),'VE0164': (1291,'Concluído',''),'VE0165': (14018,'Concluído',''),'VE0166': (2791,'Concluído',''),'VE0167': (17953,'Concluído',''),'VE0168': (14627,'Concluído',''),'VE0169': (3296,'Concluído',''),'VE0170': (1863,'Concluído',''),'VE0171': (4719,'Concluído',''),'VE0172': (15060,'Concluído',''),'VE0173': (2596,'Cancelado','Cancelada pelo Cliente'),'VE0174': (4919,'Concluído',''),'VE0175': (13770,'Concluído',''),'VE0176': (15041,'Cancelado','Estoque em Falta'),'VE0177': (6702,'Concluído',''),'VE0178': (9989,'Concluído',''),'VE0179': (5135,'Concluído',''),'VE0180': (13337,'Concluído',''),'VE0181': (13457,'Concluído',''),'VE0182': (17218,'Concluído',''),'VE0183': (6424,'Concluído',''),'VE0184': (5478,'Concluído',''),'VE0185': (10478,'Cancelado','Cancelada pelo Cliente'),'VE0186': (3240,'Concluído',''),'VE0187': (16503,'Concluído',''),'VE0188': (12762,'Concluído',''),'VE0189': (6985,'Cancelado','Cancelada pelo Cliente'),'VE0190': (13013,'Concluído',''),'VE0191': (5706,'Concluído',''),'VE0192': (6521,'Cancelado','Estoque em Falta'),'VE0193': (12904,'Concluído',''),'VE0194': (14691,'Concluído',''),'VE0195': (19338,'Concluído',''),'VE0196': (4556,'Cancelado','Cancelada pelo Cliente'),'VE0197': (9653,'Concluído',''),'VE0198': (4617,'Concluído',''),'VE0199': (4717,'Concluído',''),'VE0200': (8366,'Concluído','')}


def calculo_stockout(dicionario_vendas):
    numerador = 0
    denominador = 0
    
    for venda in dicionario_vendas:
        valor, status, motivo = dicionario_vendas[venda]
        if status == 'Concluído':
            denominador += valor
        elif status == 'Cancelado' and motivo == 'Estoque em Falta':
            denominador += valor
            numerador += valor
        
    return numerador / denominador

print(f'{calculo_stockout(vendas):.2%}')
print()



### Item 2: Crie uma função para descobrir os clientes inadimplentes de uma empresa

# - O objetivo é identificar quem são os clientes inadimplentes e enviar essa lista de clientes para o setor de cobrança poder fazer a cobrança dos clientes.
# - Sua função deve então receber uma lista de clientes, analisar quais clientes estão inadimplentes, e retornar uma lista com os clientes inadimplentes (apenas o CPF deles já é suficiente)
# - A inadimplência nessa empresa é calculada da seguinte forma:
#    1. Se o cliente tiver devendo mais de 1.000 reais por mais de 20 dias, ele é considerado inadimplente.
#    2. Isso significa que caso ou cliente esteja devendo 2.000 reais a 10 dias, ele não é inadimplente, pois não se passaram 20 dias ainda. Da mesma forma, se ele estiver devendo 500 reais por 40 dias, ele também não é inadimplente, dado que ele deve menos de 1.000 reais.
#    3. As informações vêm no formato (cpf, valor_devido, qtde de dias)

clientes_devedores = [('462.286.561-65',14405,24),('251.569.170-81',16027,1),('297.681.579-21',8177,28),('790.223.154-40',9585,10),('810.442.219-10',18826,29),('419.210.299-79',11421,15),('908.507.760-43',12445,24),('911.238.364-17',1345,4),('131.115.339-28',11625,8),('204.169.467-27',5364,22),('470.806.376-11',932,29),('938.608.980-69',13809,19),('554.684.165-26',11227,2),('119.225.846-34',4475,9),('358.890.858-95',13932,20),('786.547.940-70',17048,25),('468.487.741-94',2902,8),('540.685.100-32',5806,21),('379.729.796-80',7622,24),('980.173.363-94',13167,24),('833.285.374-56',19581,24),('103.669.436-50',17126,4),('386.836.124-46',18825,11),('588.404.964-15',1545,30),('600.556.177-18',1921,7),('670.346.230-99',18079,28),('771.352.915-13',16581,23),('430.314.324-46',13942,24),('629.507.759-51',17951,11),('348.683.225-73',12424,10),('406.133.151-17',5888,30),('310.985.894-64',17316,30),('964.317.132-30',18818,30),('845.331.524-14',14284,13),('781.995.738-18',19369,29),('921.558.128-63',3206,27),('941.386.982-65',10228,26),('551.135.290-10',18822,18),('537.124.578-35',12670,6),('119.383.169-76',790,20),('938.473.410-98',8851,5),('279.775.182-54',5212,20),('210.872.954-53',13569,8),('684.995.531-65',8649,21),('653.886.282-57',504,28),('973.580.738-53',2533,9),('285.864.892-85',8200,21),('777.154.423-98',10336,8),('769.786.401-34',3233,12),('521.566.565-97',11882,14),('491.799.681-92',653,8),('344.357.819-36',8856,18),('265.362.581-99',8962,8),('331.410.527-56',18516,18),('143.188.958-61',7234,29),('751.630.472-61',13552,6),('714.707.807-80',2898,7),('585.584.932-83',239,25),('165.554.107-13',9572,23),('718.225.984-87',10534,25),('611.715.653-32',3210,11),('397.994.286-79',13651,24),('967.160.575-69',8997,25),('369.750.998-94',13952,2),('767.400.554-79',18320,11),('171.104.286-74',5821,21),('152.817.649-24',3358,30),('645.308.846-62',15176,25),('273.884.570-92',4436,13),('888.818.341-45',15730,3),('577.836.712-40',14670,16),('513.529.919-95',4002,1),('201.476.809-95',17442,21),('657.816.571-87',1582,2),('810.494.975-87',2157,9),('531.749.410-17',12355,18),('486.290.887-24',18576,26),('432.376.642-62',8027,23),('207.274.437-91',5125,29),('634.244.673-72',11387,15),('346.871.172-72',8105,23),('166.330.605-50',7865,11),('829.181.731-94',2425,8),('197.305.464-63',9681,8),('887.877.706-59',15681,10),('847.598.885-51',323,23),('817.170.984-26',5169,27),('591.397.550-29',13362,25),('872.733.198-95',5756,18),('615.629.238-82',11678,23),('194.782.846-77',11044,17),('146.392.158-88',6848,4),('240.427.458-70',3906,25),('583.662.427-52',3306,5),('841.627.523-64',4778,4),('985.337.216-77',15308,4),('912.410.722-57',11683,6),('700.720.266-23',12638,21),('605.405.529-53',3831,3),('383.256.402-25',2599,10),('248.103.486-68',9121,1),('261.974.594-90',2139,26),('297.126.704-91',18529,16),('680.569.318-52',10176,23),('296.334.647-38',225,13),('200.761.898-70',16244,20),('258.232.687-17',19462,18),('597.295.672-38',18840,11),('894.479.102-52',11375,12),('556.156.341-36',16269,23),('987.874.553-86',11253,17),('248.927.998-94',6510,1),('852.796.660-25',2662,23),('741.370.204-36',9303,16),('536.714.951-95',2877,23),('320.395.830-44',14554,5),('520.645.562-80',17547,24),('553.700.674-28',3147,14),('913.525.896-32',17651,28),('750.456.495-86',11524,9),('246.171.748-38',15184,4),('760.248.897-67',4953,25),('920.890.990-46',17172,20),('805.469.913-50',17500,21),('878.594.225-48',6255,3),('356.715.924-36',3454,13),('847.150.802-96',8602,22),('625.846.640-53',10888,19),('539.300.108-41',11225,21),('549.151.467-76',1286,21),('738.451.908-29',18905,22),('987.288.834-69',17533,25),('898.532.296-94',9719,11),('620.531.607-13',13584,10),('169.415.202-43',1871,29),('757.885.355-97',18150,28),('252.581.376-21',2497,3),('177.937.460-78',7178,8),('523.895.611-54',9878,26),('883.680.201-23',16761,3),('936.678.268-71',11017,9),('871.912.703-73',1754,9),('957.749.478-56',6914,9),('725.636.354-80',8605,13),('898.316.244-33',14363,12),('894.748.325-28',2764,3),('647.106.954-60',1482,6),('628.716.937-98',14107,8),('332.677.483-83',19146,15),('186.870.928-82',17050,12),('216.248.879-71',4384,16),('287.929.269-44',4894,19),('278.335.932-42',17220,13),('824.107.287-13',11797,7),('535.354.954-30',9195,22),('311.762.241-12',13871,2),('209.759.133-88',13580,21),('505.728.766-53',16950,13),('879.471.988-23',17427,14),('772.329.947-39',3462,8),('321.123.241-10',2592,22),('407.342.963-78',11435,21),('786.935.637-47',14240,9),('461.791.351-55',142,2),('770.920.161-42',1247,24),('639.870.185-59',6430,10),('815.943.237-83',19550,22),('141.774.255-61',17866,13),('379.995.400-37',9503,29),('261.103.178-64',19167,13),('495.461.913-57',12265,29),('498.848.750-79',14549,16),('578.770.731-84',1462,5),('408.987.269-72',5647,28),('191.970.336-40',6313,15),('761.137.848-34',10654,23),('810.512.154-21',14928,1),('256.371.788-38',7085,2),('216.401.188-57',1531,23),('956.318.620-43',6327,22),('986.516.478-33',3866,25),('105.665.555-60',7118,4),('259.228.430-72',1601,8),('133.627.971-58',10142,14),('327.988.845-70',14985,23),('363.167.322-63',17236,7),('189.986.406-38',16888,18),('661.194.373-45',7824,1),('805.728.877-53',514,10),('887.826.412-21',15977,24),('122.975.174-32',9409,25),('456.550.370-55',19922,18),('388.243.133-66',19785,17),('208.788.890-61',11893,22),('881.332.662-49',6344,16),('912.349.944-52',6858,15),('534.904.583-32',9559,11),('825.175.334-25',19805,15),('339.191.298-46',13325,8),('569.993.915-78',4339,15)]


def inadimplentes(lista):
    lista_cpf = []
    for cliente in lista:
        cpf, valor_devido, dias = cliente
        if valor_devido > 1000 and dias > 20:
            lista_cpf.append(cpf)
    
    return lista_cpf

print(inadimplentes(clientes_devedores))