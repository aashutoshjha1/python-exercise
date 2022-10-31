import os

def get_disk_size(path):
    if os.path.exists(path):
       get_stats = os.stat(path)
       total_size = get_stats.st_size
       print("total_size {0}    with file name {1}".format(total_size, path))
       if os.path.isdir(path):
            for filename in os.listdir(path):
                  child_path = os.path.join(path, filename)
                   
                  total_size += get_disk_size(child_path)
       return total_size
   
    else:
        print("wrong path")
      

path = "/Users/a0j0b83/walmart_repo"
print(get_disk_size(path))

