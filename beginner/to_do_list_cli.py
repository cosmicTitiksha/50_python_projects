# This program is a CLI based to-do list, have fun trying it!!!!!!!


list_of_tasks = []
def insert():
  task = input("Enter task: ")
  list_of_tasks.append(task)
  return list_of_tasks

def delete(list_of_tasks):
  print(list_of_tasks)
  element = int(input("What element you want to remove?: "))
  del list_of_tasks[element-1]
  return list_of_tasks

   
while True:
  query = input("What task do you perform ? (insert/delete/exit): ").lower()

  if query == 'insert':
    print(insert())

  elif query == 'delete':
    print(delete(list_of_tasks))
    print("Task deleted Successfully!")
  
  elif query == 'exit':
    break
  
  else:
    print("Invalid Entry.")
