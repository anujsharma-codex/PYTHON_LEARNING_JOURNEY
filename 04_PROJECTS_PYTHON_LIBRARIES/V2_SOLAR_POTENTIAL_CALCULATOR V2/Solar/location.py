from Solar.solarcalculator import SolarSystem
from config import CITY,SUBSIDIES,STATE
from Solar.utils import Utils 
import numpy as np
class Location:
    def __init__(self,city,state,solar_system_obj,utils_obj):
        self.u_obj=utils_obj
        self.ss_obj=solar_system_obj
        self.city=self.u_obj.get_normalized_string(city)
        self.state=self.u_obj.get_normalized_string(state)  
    
    def get_city_latitude(self):
        return CITY[np.where(CITY["city_name"]==self.city)]["latitude"]
        #.get(self.city)
    
    def get_city_longitude(self):
        return CITY[np.where(CITY["city_name"]==self.city)]['longitude']
    
    def get_city_max_peak_sun_hours(self):
        return CITY[np.where(CITY["city_name"]==self.city)]["peak_sun_hours"]
    
    def get_combined_subsidy(self):
        row_indice=np.where(CITY["city_name"]==self.city)
        wattage_key = self.ss_obj.panel_wattage   # int number 1,2,3,4,5...
        col_indice=np.where(KW_BRACKETS==str(wattage_key)+"kW")
        city_subsidies = SUBSIDIES[row_indice,col_indice]
        return city_subsidies
    
    def get_state_export_rate(self):
        return STATE[np.where(STATE["state_name"]==self.state)]["export_rate"]
    
    def get_state_tariff(self):
        return STATE[np.where(STATE["state_name"]==self.state)]["tariff"]