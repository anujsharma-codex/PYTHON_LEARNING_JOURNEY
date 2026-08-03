import pandas as pd

class Data_Quality:
	def __init__(self, dh_obj):
		self.df = dh_obj.df
	
	def get_missing_values(self):
		missing_values = {}
		cols = ["Year","Month","Day","Hour","GHI","DHI","DNI","Temperature","Wind Speed"]
		for col in cols:
			missing_values[col] = [self.df[col].isna().sum(), self.df[col].isna().mean()*100]
		return pd.DataFrame(missing_values, index = ["Missing Count", "Missing %"])

	def get_duplicate_calculation(self):
		return self.df.duplicated().sum()

	def get_duplicate_rows(self):
		return pd.DataFrame(self.df[self.df.duplicated(keep = 'first') ])

	def get_datatype_report(self):
		return pd.DataFrame(self.df.dtypes, columns = ["Datatype"])

	def get_stat_summary(self):
		return self.df.describe()

	def get_zero_count(self):
		zero_count_dict = ((self.df == 0).sum()).to_dict()
		return zero_count_dict

	def get_negative_count(self):
		non_negative_cols = ["Year", "Month", "Day", "Hour", "GHI", "DHI", "DNI", "Wind Speed"]
		unexpected_negatives = (self.df[non_negative_cols] < 0).sum()
		return pd.DataFrame(unexpected_negatives)
		
class DataHandling:
	def __init__(self, ofile, nfile):
		self.ofile = ofile
		self.nfile = nfile
		self.df = self.data_ingestion()

	def data_ingestion(self):
		file_location = "data/"+self.ofile
		#df = pd.read_csv(file_location, skiprows = 2) commented now for testing purpose
		df = pd.read_csv(file_location)
		return df

	def filter_cols(self):
		cols = ["Year","Month","Day","Hour","GHI","DHI","DNI","Temperature","Wind Speed"]
		if all(col in self.df.columns for col in cols):
			self.df = self.df[cols]
		else:
			return False

	def handle_missing_values(self):
		self.df = self.df.dropna(subset = ["Year", "Month", "Day"])
		
	def handle_duplicate_values(self):
		self.df = self.df.drop_duplicates()
		
	def handle_outliers(self):
		cols = ["GHI","DNI","DHI","Wind Speed"]
		self.df[cols] = self.df[cols].clip(lower = 0)
		
	def handle_datatypes(self):
		cols = ["GHI","DHI","DNI","Temperature","Year","Month","Day","Hour","Minute"]
		existing_cols = [c for c in cols if c in self.df.columns]
		self.df[existing_cols] = self.df[existing_cols].apply(pd.to_numeric, errors = "coerce")
		
	def data_feeding(self):
		self.df.to_csv("data/"+self.nfile)
		return "data/"+self.nfile