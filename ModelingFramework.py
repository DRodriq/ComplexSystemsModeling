import matplotlib.pyplot as plt
import unittest
import math


class ComplexSysModelingFramework:
    def __init__(self, var1, **kwargs):
        self.var1 = var1
        self.__dict__.update(kwargs)

        result = [[var1]]
        for key, val in kwargs.items():
            if(key.count("var")):
                result[0].append(val)
        self.results = result

    def run(self, func):
        curr_state_dict = dict()
        state_var_list = [[key,value] for key, value in self.__dict__.items() if key.count("var") != 0]
        for i in range(len(state_var_list)):
            curr_state_dict[state_var_list[i][0]] = state_var_list[i][1]
        updated_values = func(curr_state_dict)
        for key in self.__dict__:
            if key in updated_values:
                self.__dict__[key] = updated_values[key]
        self.update_results()

    def update_results(self):
        result = []
        for key, val in self.__dict__.items():
            if(key.count("var")):
                result.append(val)
        self.results.append(result)

    def visualize_results(self, plot_type = "STANDARD"):
        plt.title("Results")
        if(plot_type == "PHASE_SPACE"):
            var_results = []
            for i in range(len(self.results[-1])):
                var_result = [result[i] for result in self.results]
                var_results.append(var_result)
            if(len(var_results) == 2):
                plt.plot(var_results[0], var_results[1])
        else:
           plt.plot(self.results) 
        plt.show()

    def sum_variables(self):
        sum = 0
        for key, val in self.__dict__.items():
            if(key.count("var")):
                sum = sum + val
        return sum
    
    def get_variables_list(self):
        vars = []
        for key, val in self.__dict__.items():
            if(key.count("var")):
                vars.append([key,val])
        return(vars)
        
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
        model = ComplexSysModelingFramework(1, var2=10, var3=5, var4=4)
        correct_result = [["var1", 1],["var2", 10],["var3", 5],["var4", 4]]
        self.assertEqual(model.get_variables_list(), correct_result, "Incorrect Variables")
        print("PASS!")
    
    def test_var_results(self):
        print("Running Test 2: test_var_results")
        model = ComplexSysModelingFramework(1, var2=10, var3=5, var4=4)
        correct_result = [[1, 10, 5, 4]]
        self.assertEqual(model.results, correct_result, "Incorrect Results")
        print("PASS!")

    def test_sum_variables(self):
        print("Running Test 3: test_sum_variables")
        model = ComplexSysModelingFramework(1, var2=10, var3=5, var4=4)
        self.assertEqual(model.sum_variables(), 20, "Incorrect Sum")
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