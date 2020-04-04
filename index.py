## pip install bovespa, para instalar o pacote.
import bovespa

## Coloque o caminho do arquivo.txt no 'path'.
bf = bovespa.File(path="/content/drive/My Drive/DataFiles/COTAHIST_A2019.TXT")

## Classe para transformar os dados em objetos Python.
class parseObject:
  def __init__(self, date=None, stock_code=None, price_open=None, price_close=None, price_mean=None, price_high=None, price_low=None, volume=None, quantity=None):
    self.date = date
    self.stock_code = stock_code
    self.price_open = price_open
    self.price_close = price_close
    self.price_mean = price_mean
    self.price_high = price_high
    self.price_low = price_low
    self.volume = volume
    self.quantity = quantity

## Função que recebe o nome da ação e retorna todos os dados
def extractData(stockName):
  allData = []
  for data in bf.query(stock=stockName):
    allData.append(parseObject(data.date, data.stock_code, float(data.price_open), float(data.price_close), float(data.price_high), float(data.price_low), float(data.volume), float(data.quantity)))
  return allData

## Exemplo de extração.
data = extractData("ITSA4")

## pip install pandas, para instalar o pacote.
import pandas as pd

## Listas das variáveis que você quer analisar.
date = []
price = []

## Iteracão dos dados, adicione todas as listas definidas acima.
for a in data:
  date.append(a.date)
  price.append(a.price_close)

## Nome dos campos na esquerda, valores na direita.
objectData = {
    'Date': date,
    'Price': price
}

## Transformando no DataFrame
df = pd.DataFrame(objectData)
