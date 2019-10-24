import numpy as np

class AudioSeries(object):
	
	def __init__ (self, lag = 5, threshold = 5, influence = 0.5):
		self.signals = np.array([])
		self.lag = lag
		self.threshold = threshold
		self.influence = influence
		self.currPos = 0
		self.trend = 0

	def add_value(self, num: int):
		self.signals = np.append(self.signals, num)
		self.update_trend()
		
	def update_trend(self):
		if len(self.signals) > self.lag + self.currPos:
			self.trend = self.get_avg_change(self.signals[self.currPos:self.currPos+self.lag])
			self.currPos = self.currPos + 1


	def get_avg_change(self, list):
		x = np.arange(len(list))
		return np.polyfit(x, list, 1)[0]

	def get_trend(self):
		simp_trend = int(self.trend)
		if simp_trend != 0:
			print(simp_trend)

