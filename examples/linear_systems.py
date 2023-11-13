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
    model = ModelingFramework.ComplexSysModelingFramework(plot_title = "Sweep Initial Values Example", var1=1,var2=1)
    steps = 30

    sweep = []
    for x in range(-20,21,5):
        for y in range(-20,21,5):
            var_dict = {}
            var_dict.update({"var1": x/10})
            var_dict.update({"var2": y/10})
            sweep.append(var_dict)

    for i in range(len(sweep)):
        for j in range(steps):
            model.run(test_function2)
        model.reinit_variables(sweep[i])
        

    model.visualize_results("PHASE_SPACE", len(sweep))

run_model()