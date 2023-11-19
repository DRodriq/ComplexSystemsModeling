import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + "\\..")
import ModelingFramework
import time
import numpy as np

"""
    Equations as described in "Introduction to the Modeling and Analysis of Complex Systems" 
    by Hiroki Sayama
"""
def logistics_growth_function(state_vars):
    R = .1
    K = 10
    new_values = np.zeros(state_vars.shape)
    new_values[0] = state_vars[0] + (R * state_vars[0] * (1 - ((state_vars[0]/K))))
    return new_values

def logistic_map(state_vars):
    r = 2.9
    new_values = np.zeros(state_vars.shape)
    new_values[0] = r*state_vars[0] *(1-state_vars[0])
    return new_values

def predator_prey_dynamics(state_vars):
    r = b = d = c = 1
    K = 5
    new_values = np.zeros(state_vars.shape)
    new_values[0] = state_vars[0] + (state_vars[0] * ((1- (state_vars[0]/K))))
    new_values[0] = new_values[0] - (state_vars[0] * (1-(1/(state_vars[1] + 1))))
    new_values[1] = state_vars[1] - (d*state_vars[1]) + (c*state_vars[0] * state_vars[1])
    return new_values

def run_model():
    model = ModelingFramework.ComplexSysModelingFramework(plot_title = "Logistics Growth", var1=1, var2=2)
    steps = 100
    start = time.time()
    for i in range(steps):
        #model.run(logistics_growth_function)
        model.run(predator_prey_dynamics)
    execution_time = time.time() - start
    print("Execution Time: ", execution_time)
   # model.visualize_results(title = "Predator Prey Dynamics", plot_type = "PHASE_SPACE")
    model.visualize_results(plot_type="PHASE_SPACE")
    model.pretty_print_state()

run_model()



