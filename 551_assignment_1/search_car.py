import requests as r 
import pandas as pd
import json
import regex as re
import sys

def split_words_dictionary(user_input):
  #splitting the cars into seperate words based on white spaces and punctuation
  words = re.findall(r"[\w'\"]+|[,.!?]", user_input.lower())
  return words

def data_to_dictionary(words):
  # getting the car_id from the firebase
  empty_dictionary={}
  for i in words:
    url  = r.get(f'https://homework1q3-default-rtdb.firebaseio.com/inverted/.json?orderBy="$key"&equalTo="{i}"')
    url = url.json()
    for key,value in url.items():
      empty_dictionary[key] = value

  return empty_dictionary

def sorted_list(dictionary):
  # getting the full list of car_ids to be ready to sort them by count
  list_of_all_numbers = []
  for key,value in dictionary.items():
    for number in value:
      list_of_all_numbers.append(number)
  return list_of_all_numbers

def final_result(list_of_numbers):
  # counting and sorting by number of cars
  result = sorted(set(list_of_numbers), key = lambda ele: list_of_numbers.count(ele))
  result.reverse()
  return result


if __name__ == "__main__":
  user_input = sys.argv[1]
  words = split_words_dictionary(user_input)
  dictionary = data_to_dictionary(words)
  list_of_numbers = sorted_list(dictionary)
  final_result = final_result(list_of_numbers)
  if len(final_result)>0:
    #list has a number
    print(final_result)
  else:
    #list is empty
    print("No cars found")
  
