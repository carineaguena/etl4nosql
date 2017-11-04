

# Adiciona as interfaces do framework
import IDataMgr
import IModelMgr
import IOpMgr
import IProcMgr

## Determina as bases de dados usadas
dataFonte = IDataMgr.IDataMgt("localhost","root","12346")
print(dataFonte.connection())

## Cria a amostra dos dados a serem manipulados
amostra = IModelMgr.IModelMgt(id(dataFonte))
print(amostra.readData())

## Cria as operacoes a serem executadas
operacao = IOpMgr.IOpMgt(id(amostra))
while True:
    try:
        select = 1
        operacao.putOps(amostra.createOp())
        select = int(input("to continue press 1 or press another number to stop:"))
    except ValueError:
        print("Not a valid input")
    else:
        if select != 1:
            break
print(operacao.getOps())

## Processa as operacoes
processar = IProcMgr.IProcMgt(id(operacao))
processar.process()

