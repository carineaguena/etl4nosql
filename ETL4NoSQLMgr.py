'''
Created on 3 de nov de 2017

@author: carineaguena
'''
# Adiciona as interfaces do framework
import IDataMgr
import IModelMgr
import IOpMgr
import IProcMgr

## Determina as bases de dados usadas
dataFonte = IDataMgr.IDataMgt("localhost","root","12346")
print(dataFonte.connection())

## Cria a amostra dos dados a serem manipulados
amostra = IModelMgr.IModelMgt(dataFonte.id)
print(amostra.readData())

## Cria as operacoes a serem executadas
operacao = IOpMgr.IOpMgt(amostra.id)
operacao.putOps(amostra.createOp())

## Processa as operacoes
processar = IProcMgr.IProcMgt(operacao.id)
processar.process()

