
import numpy as np

def evalCheckboardNeighbours(individual,nCB,mCB):
    
    checkboard=np.reshape(individual, (-1, mCB))
    counter=0
    for i,row in enumerate(checkboard):
        for j,entry in enumerate(row):
            if (i>0 and entry!=checkboard[i-1][j]):
                counter=counter+1
            if (i<nCB-1 and entry!=checkboard[i+1][j]):
                counter=counter+1
            if (j>0 and entry!=checkboard[i][j-1]):
                counter=counter+1
            if (j<mCB-1 and entry!=checkboard[i][j+1]):
                counter=counter+1
    return counter,

'''
 def fourPeaks(buff,n) 
{ 



  int *p; 
  int head_1, tail_0, min, max; 
    
  T_FourPeaks = Funpars[0]; 
  
  p=buff; 
  head_1=0; 
  while(*p) 
    { 
      head_1 ++; 
      p++; 
    } 
  p=buff+n-1; 
  tail_0=0; 
  while(*p==0) 
    { 
      tail_0++; 
      p--; 
    } 
  if(head_1>tail_0) 
    { 
      min=tail_0; max=head_1; 
    } 
  else
    { 
      min=head_1; max=tail_0; 
    } 
  if(min>T_FourPeaks) 
    return (100+max); 
  else
    return (max); 
}
    '''