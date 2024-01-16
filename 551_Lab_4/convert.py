import json
import sys


def writing_to_json(userinput):
  with open(f"{userinput}") as file:
    data = json.load(file)

  new_dictionary = {}
  for key in data:
    # print(key)
    for datatype, values in data[key].items():
      if datatype=="S":
        new_dictionary[key]=str(values)
      elif datatype == "N":
        if values.isdigit():
          new_dictionary[key]=int(values)
        else:
          new_dictionary[key] = float(values)
      elif datatype == "SS":
        result = [str(r) for r in values]
        new_dictionary[key]=result
      elif datatype == 'NS':
        list1 = []
        for i in values:
          if i.isdigit():
            list1.append(int(i))
          else:
            list1.append(float(i))
        new_dictionary[key] = list1
      elif datatype == 'L':
        list2 = []
        for output in values:
          for key,values in output.items():
            if key == 'S':
              list2.append(str(values))
            elif values.isdigit():
              list2.append(int(values))
            else:
              list2.append(float(values))
        new_dictionary[key]=list2
      elif datatype == "BOOL":
          new_dictionary[key] = json.dumps(values)
      else:
        dictionary_of_dictionaries ={}

        for i,x in values.items():
          # i is the key, x is the enclosed dictionary
          for l,j in x.items():
            # l is the datatype, j is the value
            if l =='S':
              dictionary_of_dictionaries[i]= str(j)
            elif l.isdigit():
              dictionary_of_dictionaries[i]= int(j)
            else:
              dictionary_of_dictionaries[i]= float(j)          
        new_dictionary[key]= dictionary_of_dictionaries
        return new_dictionary







if __name__ == "__main__":
  dictionary = writing_to_json(sys.argv[1])
  with open(f"{sys.argv[2]}", 'w') as fp:
      json.dump(dictionary,fp)
