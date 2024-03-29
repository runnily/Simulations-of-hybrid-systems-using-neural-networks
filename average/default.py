from utilities import LossUtilities, np, sys
from torch import Tensor
from itertools import product
sys.path.insert(1, '../')
from simulations import van_der_pol_oscillator, laub_loomis, lorenz_system

"""
    Arthur: Adanna Obibuaku
    Purpose: This will module is used for define the abstract class. Each class defined correspond to a
             Model. Within the class it define their default inputs and simulation method, for defining
             a simulation when needed.
    Date:   29/03/21
"""

class NewtonsLoss(LossUtilities):
    """
        This is used for reperesenting the newton cooling loss
    """
  
    def default_model_inputs(self):
        default_lr = 0.0001
        default_batch_size = 32
        default_time_step = 1
        default_num_epoches = 10
        filename = "../data/train/newtons_cooling_law.csv"
        inputs = self.inputs_to_tensor(filename, [0,1])
        targets = self.inputs_to_tensor(filename, [2])
        number_inputs = 2
        number_classes = 1
        
        return default_lr, default_batch_size, default_time_step, default_num_epoches, number_inputs, number_classes, inputs, targets

class VanDerPol(LossUtilities):

    """
        This is used for repersenting the van der pool systems.
    """

    def simulations(self, delta):
        """
            simualations:
                This defines how many simulations to performs
            Args:
                This is the delta to go up by
        """
        df_simulations = van_der_pol_oscillator(20.1 ,delta, False)
        inputs = df_simulations[['time','initial_x','initial_y']].to_numpy(dtype='float32')
        outputs = df_simulations[['x','y']].to_numpy(dtype='float32')
        return Tensor(inputs), Tensor(outputs)

    def default_model_inputs(self):
        """
            default_model_inputs:
                This defines the inputs of the model.
        """
        default_lr = 0.0005
        default_batch_size = 15
        default_time_step = 0.001
        default_num_epoches = 20
        filename = "../data/train/van.csv"
        inputs = self.inputs_to_tensor(filename, [0,3,4])
        targets = self.inputs_to_tensor(filename, [1,2])
        number_inputs = 3
        number_classes = 2
        
        return default_lr, default_batch_size, default_time_step, default_num_epoches, number_inputs, number_classes, inputs, targets

class Laub(LossUtilities):
    """
        Laub:
            This performs laub function
    """

    def simulations(self, delta):
        """
            Simulations:    
                This is the simulations defined for the laub
        """
        df_simulations = laub_loomis(delta, 500, False)
        inputs = df_simulations[['time','initial_x','initial_y','initial_z','initial_w','initial_p','initial_q','initial_m']].to_numpy(dtype='float32')
        outputs = df_simulations[['x','y','z','w','p','q','m']].to_numpy(dtype='float32')  
        return Tensor(inputs), Tensor(outputs)

    def default_model_inputs(self):
        """
            default_model_inputs:
                This are the default model inputs
        """
        default_lr = 0.0001
        default_batch_size = 500
        default_time_step = 0.01
        default_num_epoches = 10
        filename = "../data/train/laub.csv"
        inputs = self.inputs_to_tensor(filename, [0,8,9,10,11,12,13,14])
        targets = self.inputs_to_tensor(filename, [1,2,3,4,5,6,7])
        number_inputs = 8
        number_classes = 7  
        return default_lr, default_batch_size, default_time_step, default_num_epoches, number_inputs, number_classes, inputs, targets
