print ('='*20)
print ('10 TERMOS DE UMA PA')
print ('='*20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10-1) * razão # ENESIMO TERMO DE UMA P.A
for c in range (termo, décimo + razão, razão):
    print (c, end=' ➝  ')
print ('ACABOU')