import requests as r 
import pandas as pd
import sys

def read_data(file):
  # reading in the data
  df = pd.read_csv(file)
  jsondata = df.to_json(orient='records', lines=True).splitlines()
  return jsondata

def upload_data(json):
  # loading the data and using a counter to store each car as a json object
  counter = -1
  for i in json:
    counter+=1
    upload= r.put(url = f'https://homework1dsci551-default-rtdb.firebaseio.com/cars/{counter}.json', data =f'{i}')
  if upload.status_code == 200:
    print("upload successful")
  else:
    print("upload failed")

if __name__ == "__main__":
  assert len(sys.argv[1]) > 1, "Please give a valid CSV"
  path_file = sys.argv[1]
  dataframe = read_data(path_file)
  upload_data(dataframe)
