import os

# access system environment variable as a whole.
print(os.environ)
print("\n")

# access a specifically named attribute (from the data contained in "environ")
print(os.getenv('NUMBER_OF_PROCESSORS'))
