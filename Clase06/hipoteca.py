saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses_transcurridos = 0
pago_extra_mes_comienzo = 60
pago_extra_mes_fin = 107
pago_extra = 1000

while saldo>0:
            if meses_transcurridos>=pago_extra_mes_comienzo and meses_transcurridos<=pago_extra_mes_fin:
                saldo = saldo * (1+tasa/12) - pago_mensual-pago_extra
                total_pagado = total_pagado + pago_mensual+pago_extra
                meses_transcurridos +=1
            else:
                saldo = saldo * (1+tasa/12) - pago_mensual
                total_pagado = total_pagado + pago_mensual
                meses_transcurridos +=1
            if(saldo<0):
                total_pagado = total_pagado+saldo
                saldo = 0
            print(meses_transcurridos, "\t",round(total_pagado,2),"\t",round(saldo,2))

Resultado = f'Se pagó un total de ${total_pagado:0.2f} en {meses_transcurridos} meses'
print(Resultado)
