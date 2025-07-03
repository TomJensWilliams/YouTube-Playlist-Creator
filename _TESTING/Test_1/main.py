import os
my_environ = os.environ
my_path = my_environ["PATH"]
my_user = my_environ.get("USER")
my_nonexistant_variable = my_environ.get("Nonexistant-variable")
my_api_key = my_environ.get("API_KEY")
print(my_environ)
print()
print(my_path)
print()
print(my_user)
print()
print(my_nonexistant_variable)
print()
print(my_api_key)