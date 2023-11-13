import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + "\\..")
import ModelingFramework

def test_function1(state_variables):
    a = 1.1
    new_values = {}
    for var_name, var_value in state_variables.items():
        if var_name == "var1":
            new_value = var_value * a
            new_values.update({var_name:new_value})
    return new_values

def test_function2(state_variables):
    coeff = .5
    new_values = {}
    for var_name, var_value in state_variables.items():
        if var_name == "var1":
            new_value = (coeff * var_value) + state_variables.get("var2")
            new_values.update({var_name:new_value})
        if var_name == "var2":
            new_value = (-coeff * state_variables.get("var1")) + var_value
            new_values.update({var_name:new_value})
    return new_values

def run_model():
    model = ModelingFramework.ComplexSysModelingFramework(var1=1,var2=1)
    steps = 50
    for i in range(steps):
        model.run(test_function2)
    #model.visualize_results("PHASE_SPACE")
    model.visualize_results()

run_model()