import pandas as pd 
import lxml
from lxml import etree
from datetime import datetime
import sys
import regex as re

def read_file(fsimage):
  tree = etree.parse(open(f'{fsimage}'))
  return tree


def mtime_list(tree):
  mtime = tree.xpath('/fsimage/INodeSection/inode/mtime/text()')
  mtimeIntegers = list(map(int, mtime))
  date = []
  # getting all the mtime integers and converting to date
  for i in mtimeIntegers:
    date.append(datetime.utcfromtimestamp(i/1000).strftime('%m/%d/%Y %H:%M'))
  return date

def bytes_list(tree):
  # getting the filesize
  nodes_with_blocks = tree.xpath('/fsimage/INodeSection/inode[blocks[node()]]/id/text()')
  number_of_bytes=[]
  # oath of inodes and appending number of bytes list
  path_of_inodes = int(tree.xpath('count(/fsimage/INodeSection/inode)'))+1
  for i in range(path_of_inodes):
    number_of_bytes.append(tree.xpath(f'/fsimage/INodeSection/inode[{i}]//numBytes/text()'))
  # getting a final list of integers for the number of bytes
  number_of_bytes_list = [ int(l[0]) if l else 0 for l in number_of_bytes ]
  return number_of_bytes_list[1:]

def block_list(bytes_list):
  num_of_blocks_list = []
  for i in bytes_list:
    number_blocks = (i//134217728)+1
    # only 1 block
    if (i >0) and (i<134217728):
      num_of_blocks_list.append(1)
    # zero blocks
    elif i==0:
      num_of_blocks_list.append(0)
    # whole block list
    else:
      num_of_blocks_list.append(number_blocks)
  return num_of_blocks_list[0:]

def numberToPermission(permission):
  permission_values = [(4,"r"),(2,"w"),(1,"x")]
  result = ""
  # splitting the numbers and getting ready for converting the permissions
  split_numbers = [int(n) for n in str(permission)]
  for i in split_numbers:
    # creating the strings
    for (value, type_permission) in permission_values:
        if (i >= value):
            result = result + type_permission
            i = i - value
        else:
            result = result + '-'
  return result

def type_permission(tree):
  list_of_permissions = [] 
  permissions = tree.xpath('/fsimage/INodeSection/inode/permission/text()')
  for i in permissions:
    number = i.split(":")
    for x in number:
      if x.isdigit():
        list_of_permissions.append(int(x))
  return list_of_permissions

def permissions_into_list(list_of_permissions):
  full_list = []
  for i in list_of_permissions:
    full_list.append(numberToPermission(i))
  return full_list

def final_transformation_file_permissions(permissions_into_list):
  directoryOrFileList = []
  dorf = tree.xpath('/fsimage/INodeSection/inode/type/text()')
  for x in dorf:
    if x == "DIRECTORY":
      directoryOrFileList.append("d")
    else:
      directoryOrFileList.append("-")
  final_list = [x+y for x, y in zip(directoryOrFileList, permissions_into_list)]
  return final_list

def find_all_children(p):
  #finding all the child paths
    return (find_all_children(children_dictionary[p]) if p in children_dictionary else []) + [p]

def file_path(tree):
        
  parents = tree.xpath("/fsimage/INodeDirectorySection")
  directory = []
  for element in parents:
    directory.append(etree.tostring(element).decode('utf-8').splitlines())
  list_of_ids=[]
  for x in directory:
    for i in x:
      numbers = re.findall(r'\d+',i)
      list_of_ids.append(numbers)
  list_of_ids = list_of_ids[:-1]

  parent_children_dictionary = {}
  for x in list_of_ids:
      parent_children_dictionary[x[0]] = x[1:]


  empty_list= []
  for key,value in parent_children_dictionary.items():
    for values in value:
      empty_list.append((values,key))


  children_dictionary = {}
  for c,p in empty_list:
      children_dictionary[c] = p
  def find_all_children(p):
      return (find_all_children(children_dictionary[p]) if p in children_dictionary else []) + [p]


  list_of_paths_id = []
  ids = tree.xpath('/fsimage/INodeSection/inode/id/text()')
  for i in ids:
    list_of_paths_id.append(find_all_children(i))

  list_with_extra_slash = []
  for i in list_of_paths_id:
    string = ""
    for j in i:
      root = tree.xpath("/fsimage/INodeSection/inode[name[not(node())]]/id/text()")
      s = "".join(j)
      if s == (''.join(root)):
        string+="/"
      else:
        string+="/".join(tree.xpath(f'/fsimage/INodeSection/inode[id = {j}]/name/text()'))+"/"

    list_with_extra_slash.append(string)
      

      
  final_file_path = []
  for i in list_with_extra_slash[1:]:
    final_file_path.append(i[:-1])

  final_file_path.insert(0,"/")
  return final_file_path





def dataframe(file_path, mtime,num_blocks,num_bytes,permissions_into_list):
  df = pd.DataFrame({"Path":file_path,'ModificationTime': mtime,'BlocksCount':num_blocks ,'FileSize':num_bytes,'Permission':permissions_into_list})
  return df 



 
        

if __name__ == "__main__":
  user_input = sys.argv[1]
  tree = read_file(user_input)
  mtime = mtime_list(tree)
  num_bytes = bytes_list(tree)
  num_blocks = block_list(num_bytes)
  type_of_permissions = type_permission(tree)
  permissions_into_list = permissions_into_list(type_of_permissions)
  final_transformation_file_permissions = final_transformation_file_permissions(permissions_into_list)
  file_path = file_path(tree)
  dataframe = dataframe(file_path, mtime,num_blocks,num_bytes,permissions_into_list)
  dataframe.to_csv(f'{sys.argv[2]}', sep="\t",index= False)
  
  
                  
  
  
