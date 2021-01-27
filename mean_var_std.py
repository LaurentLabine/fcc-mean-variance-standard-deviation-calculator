import numpy as np

def calculate(list):

  if(len(list)< 9):
    raise ValueError("List must contain nine numbers.")

  res = {'mean':[], 'variance':[], 'standard deviation': [] , 'max':[], 'min':[], 'sum':[]}
  nparr = np.array(list)
  nparr = np.reshape(nparr,(-1,3))
  
  res["mean"].append(np.mean(nparr,axis=0).tolist())
  res["mean"].append(np.mean(nparr,axis=1).tolist())
  res["mean"].append(np.mean(nparr).tolist())
  
  res["variance"].append(np.var(nparr,axis=0).tolist())
  res["variance"].append(np.var(nparr,axis=1).tolist())
  res["variance"].append(np.var(nparr).tolist())
  
  res["standard deviation"].append(np.std(nparr,axis=0).tolist())
  res["standard deviation"].append(np.std(nparr,axis=1).tolist())
  res["standard deviation"].append(np.std(nparr).tolist())
  
  res["max"].append(np.max(nparr,axis=0).tolist())
  res["max"].append(np.max(nparr,axis=1).tolist())
  res["max"].append(np.max(nparr).tolist())
  
  res["min"].append(np.min(nparr,axis=0).tolist())
  res["min"].append(np.min(nparr,axis=1).tolist())
  res["min"].append(np.min(nparr).tolist())
  
  res["sum"].append(np.sum(nparr,axis=0).tolist())
  res["sum"].append(np.sum(nparr,axis=1).tolist())
  res["sum"].append(np.sum(nparr).tolist())

  return res
