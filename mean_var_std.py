import numpy as np
def calculate(arry):
    
    nparray=np.array(arry)
    splitarray=nparray.reshape(3,3)
    mean0=splitarray.mean(axis=0)
    mean1=splitarray.mean(axis=1)
    meanflattend=splitarray.mean()
    variance0=splitarray.var(axis=0)
    variance1=splitarray.var(axis=1)
    varianceflattend=splitarray.var()
    stddev0=splitarray.std(axis=0)
    stddev1=splitarray.std(axis=1)
    stddevflattend=splitarray.std()
    mininmun0=splitarray.min(axis=0)
    mininmun1=splitarray.min(axis=1)
    mininmunflattend=splitarray.min()
    maximum0=splitarray.max(axis=0)
    maximum1=splitarray.max(axis=1)
    maximumflattend=splitarray.max()
    sumarray0=splitarray.sum(axis=0)
    sumarray1=splitarray.sum(axis=1)
    sumarrayflattend=splitarray.sum()
    FINAL_DICTIONARY={
        'Mean':[mean0.tolist(),mean1.tolist(),meanflattend.tolist()],
        'Variance':[variance0.tolist(),variance1.tolist(),varianceflattend.tolist()],
        'Std Deviation':[stddev0.tolist(),stddev1.tolist(),stddevflattend.tolist()],
        'Minimum':[mininmun0.tolist(),mininmun1.tolist(),mininmunflattend.tolist()],
        'Maxium':[maximum0.tolist(),maximum1.tolist(),maximumflattend.tolist()],
        'Sum':[sumarray0.tolist(),sumarray1.tolist(),sumarrayflattend.tolist()]
    }
    return FINAL_DICTIONARY
