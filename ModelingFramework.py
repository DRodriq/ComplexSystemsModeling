import matplotlib.pyplot as plt
import unittest
import math
import numpy as np


class ComplexSysModelingFramework:
    def __init__(self, **kwargs):
        self.sweeps = 1
        self.var_names = []
        initial_values = []
        for key, val in kwargs.items():
            if(key.count("var")):
                self.var_names.append(key)
                initial_values.append(val)
            if(key == "initial_values"):
                initial_values = val
        self.results = np.array(initial_values)
        self.results.shape = (1, len(self.results))

    def run(self, func):
        new_results = func(self.results[-1,:])
        self.results = np.vstack([self.results, new_results])

    def run_pop(self, iterations, values, func):
        self.results[0] = values[0]
        for i in range(len(values)):
            self.set_values(values[i])
            for j in range(iterations):
                self.run(func)

    def set_values(self, new_values):
        assert(new_values.shape[0] == self.results.shape[1])
        if(np.array_equal(self.results[-1,:], new_values) != True):
            self.results = np.vstack([self.results, new_values])
            self.sweeps = self.sweeps + 1

    def visualize_results(self, title="Title", plot_type = "STANDARD", sweeps = 1):
        plt.title(title)
       # plt.xlabel(xlab)
       # plt.ylabel(ylab)
        if(plot_type == "PHASE_SPACE"):
            if(len(self.results[-1]) == 2):
                    sub_results = np.array_split(self.results, self.sweeps, axis=0)
                    for i in range(len(sub_results)):                                     
                        plt.plot(sub_results[i][:,0], sub_results[i][:,1])
                    plt.xlabel(self.var_names[0])
                    plt.ylabel(self.var_names[1])
            if(len(self.results[-1]) == 3):
                ax = plt.axes(projection='3d')
                ax.plot3D(self.results[:,0], self.results[:,1], self.results[:,2])
        else:
            plt.plot(self.results)
        plt.show()

    def get_state_dict(self):
        state_vars = self.results[-1,:]
        state_dict = {}
        for i in range(len(state_vars)):
            state_dict.update({self.var_names[i]:state_vars[i]})
        return state_dict

    def pretty_print_state(self):
        print(self.get_state_dict())
    

class ExtendedComplexSysModelingFramework(ComplexSysModelingFramework):
    def __init__(self, var1, **kwargs):
        super().__init__(var1, **kwargs)

    def check_variable_exists(self, var_name):
        exists = True
        if var_name not in self.__dict__:
            exists = False
            print(("Please provide value for {}").format(var_name))
        return exists

    def add_variable(self, var_name, var_value):
        self.__dict__.update({var_name:var_value})
        self.update_results()

class ComplexSysModelingFramework_TEST(unittest.TestCase):
    def test_var_init(self):
        print("Running Test 1: test_var_init")
        model = ComplexSysModelingFramework(var1=1, var2=10, var3=5, var4=4)
        correct_result = {"var1": 1,"var2":10,"var3": 5,"var4": 4}
        self.assertEqual(model.get_state_dict(), correct_result, "Incorrect Variables")
        print("PASS!")

    def test_run(self):
        print("Running Test 4: test_run")
        model = ComplexSysModelingFramework(1, var2=10, var3=5, var4=4)
        model.run(ComplexSysModelingFramework_TEST.function_a)
        self.assertEqual(model.results[-1], [10,2.0,-0.9589242746631385,9], "Incorrect Sum")
        print("PASS!")       

    @staticmethod
    def function_a(state_dict):
        new_var1 = state_dict.get("var1") * state_dict.get("var2")
        new_var2 = state_dict.get("var2")/state_dict.get("var3")
        new_var3 = math.sin(state_dict.get("var3"))
        new_var4 = state_dict.get("var4") + 5
        return {"var1":new_var1,"var2":new_var2,"var3":new_var3,"var4":new_var4}

if __name__ == "__main__":
    unittest.main()