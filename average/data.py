"""
    Arthur: Adanna Obibuaku
    Purpose: This module is used for gathering data. That is 30 data plots to be later used for
             boxplots.
    Date:   29/03/21
"""

import default

TITLE_LR = "Learning Rate"
TITLE_BATCH_SIZE = "Batch Size"
TITLE_NUM_EPOCHES = "Number Of Epoches"
TITLE_TIME_STEP = "Time Step"

def thiry_data_items(title, model, filename, **para):
    """
        thirty_data_item: This denotes will gather the 30 plots data loss item corresponding to the parameter
        Args:
            title (string) : This will show the title for the plots being gathered
            model (class <LossUtilities>) : This will show the model being used
            filename (string) : This will save the filename
            ***para: This denotes the parameter that will be used.
    """
    print("--- %s  ---" % (title))
    values = list(para.values())
    if len(values) > 0:
        data, df = model.loss(len(values[0]), **para)
        df.to_csv(filename, index=False)

# This is the methods will perform the collection of data plots ...

def newton(lr, batch_size, num_epoches):
    if lr:
        para = {"lr" : [0.1, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]}
        thiry_data_items(TITLE_LR, default.NewtonsLoss(),"../data/boxplots/newton/lr.csv", **para)

    if batch_size:
        para = {"batch_size" : [50, 100, 150, 200, 250, 300]}
        thiry_data_items(TITLE_BATCH_SIZE, default.NewtonsLoss(),"../data/boxplots/newton/batch_size.csv", **para)

    if num_epoches:
        para = {"num_epoches" : [50, 100, 150, 200, 250, 300]}
        thiry_data_items(TITLE_NUM_EPOCHES, default.NewtonsLoss(),"../data/boxplots/newton/num_epoches.csv", **para)

def van(lr, batch_size, num_epoches, time_step):
    if lr:
        para = {"lr" : [0.5, 0.005, 0.0005, 0.00005, 0.000005, 0.0000005]}
        thiry_data_items(TITLE_LR, default.VanDerPol(),"../data/boxplots/van/lr.csv", **para)

    if batch_size:
        para = {"batch_size" : [15, 20, 25, 30, 35, 40]}
        thiry_data_items(TITLE_BATCH_SIZE, default.VanDerPol(),"../data/boxplots/van/batch_size.csv", **para)

    if num_epoches:
        para = {"num_epoches" : [50, 100, 150, 200, 250, 300]}
        thiry_data_items(TITLE_NUM_EPOCHES, default.VanDerPol(),"../data/boxplots/van/num_epoches.csv", **para)

    if time_step:
        para = {"time_step" : [0.1, 0.01, 0.001]}
        thiry_data_items(TITLE_TIME_STEP, default.VanDerPol(),"../data/boxplots/van/time_step.csv", **para)

def laub(lr, batch_size, num_epoches, time_step):
    if lr:
        para = {"lr" : [0.0001, 0.00005, 0.000005, 0.0000005, 0.00000005, 0.000000005]}
        thiry_data_items(TITLE_LR, default.laub(),"../data/boxplots/laub/lr.csv", **para)

    if batch_size:
        para = {"batch_size" : [500, 550, 600, 650, 700, 750]}
        thiry_data_items(TITLE_BATCH_SIZE, default.laub(),"../data/boxplots/laub/batch_size.csv", **para)

    if num_epoches:
        para = {"num_epoches" : [10, 20, 30, 40, 50, 60]}
        thiry_data_items(TITLE_NUM_EPOCHES, default.laub(),"../data/boxplots/laub/num_epoches.csv", **para)

    if time_step:
        para = {"time_step" : [0.1, 0.01, 0.001]}
        thiry_data_items(TITLE_TIME_STEP, default.VanDerPol(),"../data/boxplots/laub/time_step.csv", **para)


if __name__== "__main__":
    # Add data here for plots you want to collect
    print("..Collecting data..")
    laub(True, True, True, True)