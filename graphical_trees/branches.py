class branch():
  def __init__(self,num,tab):  #class for each branch in tree, number of point and tuple of points it's the parent of
    self.number=num 
    self.tuple=[]
    for i in range(len(tab)):
      self.tuple.append(tab[i])
