import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + "\\..")
import ModelingFramework
import time
import numpy as np

def basic_3d_function(state_variables):
    coeff = .5
    new_values = {}
    for var_name, var_value in state_variables.items():
        if var_name == "var1":
            new_value = (coeff * var_value) + state_variables.get("var2")
            new_values.update({var_name:new_value})
        if var_name == "var2":
            new_value = (-coeff * state_variables.get("var1")) + var_value
            new_values.update({var_name:new_value})
        if var_name == "var3":
            new_value = -state_variables.get("var1") - state_variables.get("var2") + var_value
            new_values.update({var_name:new_value})
    return new_values

def test_function2(state_vars):
    coeff = .5
    new_values = np.zeros(state_vars.shape)
    new_values[0] = (coeff * state_vars[0]) + state_vars[1]
    new_values[1] = (-coeff * state_vars[0]) + state_vars[1]
    return new_values

def sweep_values():
    sweep = []
    for x in range(-2,2,1):
        for y in range(-2,2,1):
           # for z in range(-2,2,1):
            sweep.append([x,y])
    sweep = np.array(sweep)
    return sweep

def run_model():
    sweep = sweep_values()
    model = ModelingFramework.ComplexSysModelingFramework(var1=0,var2=0)
    steps = 30
    start = time.time()
    model.run_pop(steps, sweep, test_function2)
    execution_time = time.time() - start
    print("Execution Time: ", execution_time)
    model.visualize_results(title = "Test Function 2", plot_type="PHASE_SPACE", sweeps = len(sweep))

run_model()