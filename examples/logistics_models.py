import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + "\\..")
import ModelingFramework

"""
    Equations as described in "Introduction to the Modeling and Analysis of Complex Systems" 
    by Hiroki Sayama
"""
def logistics_growth_function(state_variables):
    R = .1
    K = 10
    new_values = {}
    for var_name, var_value in state_variables.items():
        if var_name == "var1":
            new_value = var_value + (R * var_value * (1 - ((var_value/K))))
            new_values.update({var_name:new_value})
    return new_values

def predator_prey_dynamics(state_variables):
    r = b = d = c = 1
    K = 5
    new_values = {}
    for var_name, var_value in state_variables.items():
        if var_name == "var1":
            new_value = var_value + (var_value * ((1- (var_value/K))))
            new_value = new_value - (var_value * (1-(1/(state_variables.get("var2") + 1))))
            new_values.update({var_name:new_value})
        if var_name == "var2":
            new_value = var_value - (d*var_value) + (c*state_variables.get("var1") * var_value)
            new_values.update({var_name:new_value})
    return new_values

def run_model():
    model = ModelingFramework.ComplexSysModelingFramework(plot_title = "Logistics Growth", var1=1, var2=1)
    steps = 100
    for i in range(steps):
        #model.run(logistics_growth_function)
        model.run(predator_prey_dynamics)
    model.visualize_results("PHASE_SPACE")
    #model.visualize_results()

run_model()



