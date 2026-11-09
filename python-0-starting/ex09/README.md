# ft_package

Is a small python package containing the function count_in_list

# Installation
### Build the package
```python
python -m build
```

### Install the package

```python 
pip install ./dist/ft_package-0.0.1.tar.gz
```
or
```python 
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

# Basic usage :
```python 
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
print(count_in_list([], "toto")
```