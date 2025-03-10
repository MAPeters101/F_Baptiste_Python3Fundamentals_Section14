'''
Question 1
Given these two lists:

widgets = [f'w{i}' for i in range(1, 21)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]
Write a function that uses the zip function to generate a dictionary with keys
from the widgets, and values from the skus, i.e.:

{
  'w1': 'sku1',
  'w2': 'sku2',
  ...
  'w20': 'sku20'
}
'''