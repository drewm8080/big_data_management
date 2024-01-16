
import requests as r 
import pandas as pd
import json
import sys
import regex as re 

def read_data(file):
  # reading the data into a json
  df = pd.read_csv(file)
  jsondata = df.to_json(orient='records', lines=True).splitlines()
  return jsondata

def upload_data(json):
  # creating the firebase
  counter = -1
  for i in json:
    counter+=1
    upload= r.put(url = f'https://homework1q3-default-rtdb.firebaseio.com/cars/{counter}.json', data =f'{i}')
  if upload.status_code == 200:
    print("upload successful")
  else:
    print("upload failed")

def get_data(data):
  #getting the data from the firebase
  data = r.get('https://homework1q3-default-rtdb.firebaseio.com/cars/.json?orderBy="price"&startAt=0&endAt=50000000000000')
  data = data.json()
  return data

def split_words_dictionary(data):
  #splitting the cars into seperate words based on white spaces and punctuation
  dictionary ={}
  for key,value in data.items():
    result = re.findall(r"[\w'\"]+|[,.!?]", value['CarName'].lower())
    dictionary[value['car_ID']]=result
  return dictionary

def list_of_lists(dictionary):
  # turning the dictionary into a list of lists to be manipulated
  result = [[k, v] for k,v in dictionary.items()]
  return result

def inverted_dictionary(list_of_dictionary):
  # inverting the dictionary
  final_dictionary = {}
  for x in list_of_dictionary:
    for i in x[1]:
      try: # Key exists in dictionary and value is a list
        final_dictionary[i.lower()].append(x[0])
      except KeyError: # Key does not yet exist in dictionary
        final_dictionary[i.lower()] = x[0]
      except AttributeError: # Key exist in dictionary and value is not a list 
        final_dictionary[i.lower()] = [final_dictionary[i.lower()], x[0]]
  return final_dictionary
  
def upload_inverted_dictionary(final_dictionary):
  final_dictionary_upload = json.dumps(final_dictionary)
  upload= r.put(url = 'https://homework1q3-default-rtdb.firebaseio.com/inverted/.json', data = final_dictionary_upload)
  print("Done! Your data has been uploaded")

if __name__ == "__main__":
  assert len(sys.argv[1]) > 1, "Please give a valid CSV"
  path_file = sys.argv[1]
  dataframe = read_data(path_file)
  data = upload_data(dataframe)
  dictionary = get_data(data)
  split_words_dictionary = split_words_dictionary(dictionary)
  list_of_dictionary = list_of_lists(split_words_dictionary)
  final_dictionary = inverted_dictionary(list_of_dictionary)
  upload_inverted_dictionary(final_dictionary)
  
  
  
  


