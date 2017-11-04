# Adiciona as interfaces do framework
import IDataMgr
import IModelMgr
import IOpMgr
import IProcMgr

## Configuracao da base de dados da Fonte
dataDB = IDataMgr.IDataMgt()
print(dataDB.connection())
print(dataDB.structureType())

## Configuracao da base de dados da APD
dataAPD = IDataMgr.IDataMgt()
print("::APD DB::")
print(dataDB.connection())
print(dataDB.structureType())

## Configuracao da base de dados do Destino
print("::Dst DB::")
dataDst = IDataMgr.IDataMgt()
print(dataDB.connection())
print(dataDB.structureType())

## Extrai amostra dos dados a serem manipulados
amostra = IModelMgr.IModelMgt(id(dataDB))
print(amostra.readData())

## Cria as operacoes a serem executadas
operacao = IOpMgr.IOpMgt(id(amostra))
while True:
    try:
        select = 1
        operacao.putOps(amostra.createOp())
        select = int(input("to continue press 1 or press another number:"))
    except ValueError:
        print("Not a valid input")
    else:
        if select != 1:
            break
print(operacao.getOps())

## Processa as operacoes
processar = IProcMgr.IProcMgt(id(operacao), operacao.getOps())

## Processa os dados das operacoes criadas e grava na APD
print(processar.process())
amostraAPD = IModelMgr.IModelMgt(id(dataAPD))
for x in processar.process(): 
            print(x)
            amostraAPD.writeData()

## Gerencia as operacoes

## Insere novas operacoes
operacao.putOps(amostraAPD.createOp())

## Remove operacoes
operacao.popOp(amostraAPD.createOp())

## Gravar os dados na base de destino
destino = IModelMgr.IModelMgt(id(dataDst))
print(amostraAPD.readData())
destino.writeData()
