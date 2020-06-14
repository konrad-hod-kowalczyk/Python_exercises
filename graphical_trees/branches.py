class branch():
  def __init__(self,num,tab):
    self.number=num
    self.tuple=[]
    for i in range(len(tab)):
      self.tuple.append(tab[i])