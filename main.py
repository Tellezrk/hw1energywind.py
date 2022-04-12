###############################################################
# Progress Filename: Hw1
# Author: Kosumi Tellez Rangel
# Date: 4/11/22
# Description: This progress will compute how much an oregonian needs to power their daily life activities.
# Input: Average wind speed, radius, efficiency
# output: Max Power, Actual Power
###############################################################
import math

Ave_Wind_Speed = input ("Enter the average wind speed in m/s: ")
Blade_Radius = input ("Enter radius of the wind turbine in m: ")
turbine_area = float (Blade_Radius)**2 * (math.pi)
air_density = input ("Enter the density of the air: ")
max_turbine_power = float (Ave_Wind_Speed)**3 * 0.5 * float (turbine_area) * float(air_density)
print ("The max power of the turbine is", max_turbine_power, "W")
operating_efficiency = input ("Enter the operating effiency of the turbine as a decimal: ")
actual_turbine_power = float(max_turbine_power) * float(operating_efficiency)
print ("The actual power output of the wind turbine is", actual_turbine_power, "W")
