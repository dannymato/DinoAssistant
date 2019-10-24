import numpy as np

class AudioSeries(object):
	
	def __init__ (self, lag = 5, threshold = 5, influence = 0.5):
		self.signals:np.array = np.array()
		self.lag = lag
		self.threshold = threshold
		self.influence = influence
		self.currPos = 0

	def add_value(self, num: int):
		np.append(self.signals, [num])
		#recalculate std dev
		
	def update_trend(self, parameter_list):
		if len(self.signals) > lag + self.currPos:
			self.trend = self.get_avg_change(self.signals[self.currPos:self.currPos+lag])
									

	def get_avg_change(self, list):
		x = np.arange(len(list))
		return np.polyfit(x, list, 1)


	
