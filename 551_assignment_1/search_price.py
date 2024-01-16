import requests as r
import sys


def query(user_number1,user_number2):
  try:
    data = r.get(f'https://homework1dsci551-default-rtdb.firebaseio.com/cars/.json?orderBy="price"&startAt={user_number1}&endAt={user_number2}')
    if data.status_code == 200:
      print("response successful")
      return data.json()
    else:
      print("response unsuccessful")
      sys.exit(1)

  except:
    print('search failed')
    sys.exit(1)


def data_list(data):
    list1 = []

    for key, value in data.items():
        list1.append(value['car_ID'])

    final_data = sorted(list1)
    return final_data






if __name__ == "__main__":

    user_number1 = sys.argv[1]
    user_number2 = sys.argv[2]

    data = query(user_number1,user_number2)
    finalized_data = data_list(data)

    if finalized_data:
        print(finalized_data)
    else:
        print("No cars found with the given range")
    
    






