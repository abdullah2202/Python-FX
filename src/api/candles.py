from api.env import api_details
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import numpy as np

class Candles():

   instrument = 'XAU_USD'
   candle_list = []
   api = API(access_token=api_details.oanda_token)
   granularity = 'M30'

   def __init__(self):
      pass

   def getHigh(self, shift):
      return self.getCandleInfo(shift, 'h')

   def getLow(self, shift):
      return self.getCandleInfo(shift, 'l')
   
   def getOpen(self, shift):
      return self.getCandleInfo(shift, 'o')
   
   def getClose(self, shift):
      return self.getCandleInfo(shift, 'c')
   
   def getVolume(self, shift):
      return self.getCandleMeta(shift, 'volume')

   def setGranularity(self, granularity):
      self.granularity = granularity
   
   def getGranularity(self):
      return self.granularity
   
   def setInstrument(self, instrument):
      self.instrument = instrument

   def getInstrument(self):
      return self.instrument
   
   def isBearish(self, shift):
      candle = self.getCandleMeta(shift, 'mid')
      return candle['o'] > candle['c']
   
   def isBullish(self, shift):
      candle = self.getCandleMeta(shift, 'mid')
      return candle['c'] >= candle['o']

   def getCandleInfo(self, shift, type):
      num_of_candles = shift + 1
      params = {'granularity' : self.getGranularity(), 'count' : num_of_candles}
      r = instruments.InstrumentsCandles(instrument=self.getInstrument(), params=params)
      self.api.request(r)
      candles = np.flip(r.response['candles'])
      return candles[shift]['mid'][type]

   def getCandleMeta(self, shift, type):
      num_of_candles = shift + 1
      params = {'granularity' : self.getGranularity(), 'count' : num_of_candles}
      r = instruments.InstrumentsCandles(instrument=self.getInstrument(), params=params)
      self.api.request(r)
      candles = np.flip(r.response['candles'])
      return candles[shift][type]

   def getCandleData(self, num_of_candles):
      params = {'granularity' : self.getGranularity(), 'count' : num_of_candles}
      r = instruments.InstrumentsCandles(instrument=self.getInstrument(), params=params)
      self.api.request(r)
      candles = np.flip(r.response['candles'])
      return candles
      

