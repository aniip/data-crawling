# set AIRFLOW__CORE__FERNET_KEY="et5zVzDgzyItkSEnpaHb0nj3Tp5d3sYV_4H-c_eyaIw="

from cryptography.fernet import Fernet  

fernet_key = Fernet.generate_key() 
print(fernet_key.decode())