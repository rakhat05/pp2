#1 
import datetime 
x = datetime.datetime.now() 
print(f"{x.year}.{x.month}.{x.day-5} {x.hour}:{x.minute}:{x.second}") 

#2 
import datetime 
x = datetime.datetime.now() 
print(f"{x.year}.{x.month}.{x.day+1} {x.hour}:{x.minute}:{x.second}") 

#3 
import datetime 
x = datetime.datetime.now() 
print(f"{x.year}.{x.month}.{x.day} {x.hour}:{x.minute}:{x.second}  {x.strftime("%f")}") 

#4 
import datetime 
x = datetime.datetime.now() 
x_seconds = x.timestamp() 
any_data = datetime.datetime(2024,2,16,10,12,10) 
any_data_seconds = any_data.timestamp() 
print(abs(x_seconds - any_data_seconds))
