
import pandas as pd

class OutfitRecommender:
  def __init__(self,csv_path):
    self.data = pd.read_csv(csv_path)

  def recommend(self,Color=None,Occasion=None):
    result=self.data
    
    if Color:
      result=result[result['Color'].str.lower()==Color.lower()]
    if Occasion:
      result=result[result['Occasion'].str.lower()==Occasion.lower()]
    return result['Outfit'].tolist()
  