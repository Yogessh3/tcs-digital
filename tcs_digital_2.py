class Property:
  def __init__(self,propertyType,value,maxBidNumber):
      self.propertyType=propertyType
      self.value=value
      self.maxBidNumber=maxBidNumber
class Tender:
  def __init__(self,bidName,propertyType,bidPrice):
    self.bidName=bidName
    self.propertyType=propertyType
    self.bidPrice=bidPrice
def bidProperty(properties,tenders):
  for tender in tenders:
    maxbuy=None
    maxPrice=0
    tenderAns=[]
    for property in properties:
      if(property.propertyType.lower()==tender.propertyType.lower()):
        if(tender.bidPrice>maxPrice):
          maxbuy=tender.bidName
          maxPrice=tender.bidPrice
    if(maxbuy is not None):
      tenderAns.append(maxbuy)
    else:
      for i in range(len(properties)):
        if(properties[i].propertyType.lower()==tender.propertyType.lower()):
          del properties[i] 
  return tenderAns
props=[]
tend=[]
N=int(input())
for test in range(N):
  propertyType=input()
  value=int(input())
  maxbidNumber=int(input())
  P=Property(propertyType,value,maxbidNumber)
  props.append(P)
T=int(input())
for test in range(T):
  bidName=input()
  propertyType=input()
  bidPrice=int(input())
  Ten=Tender(bidName,propertyType,bidPrice)
  tend.append(Ten)
answer=bidProperty(props,tend)
if len(answer)==0:
  print("Property not found")
else:
  print(*answer)
for property in props:
  print(property.propertyType)

        

  

