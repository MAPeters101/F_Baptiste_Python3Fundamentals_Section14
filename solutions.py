'''
Question 1
Given these two lists:

widgets = [f'w{i}' for i in range(1, 21)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]
Write a function that uses the zip function to generate a dictionary with keys from the widgets, and values from the skus, i.e.:

{
  'w1': 'sku1',
  'w2': 'sku2',
  ...
  'w20': 'sku20'
}
Solution
Let's see what's contained in widgets and skus:

print(widgets)
['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'w11', 'w12', 'w13', 'w14', 'w15', 'w16', 'w17', 'w18', 'w19', 'w20']
print(skus)
['sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8', 'sku9', 'sku10', 'sku11', 'sku12', 'sku13', 'sku14', 'sku15', 'sku16', 'sku17', 'sku18', 'sku19', 'sku20']
We can use the zip function to create tuples with the widgets and their corresponding skus:

print(list(zip(widgets, skus)))
[('w1', 'sku1'), ('w2', 'sku2'), ('w3', 'sku3'), ('w4', 'sku4'), ('w5', 'sku5'), ('w6', 'sku6'), ('w7', 'sku7'), ('w8', 'sku8'), ('w9', 'sku9'), ('w10', 'sku10'), ('w11', 'sku11'), ('w12', 'sku12'), ('w13', 'sku13'), ('w14', 'sku14'), ('w15', 'sku15'), ('w16', 'sku16'), ('w17', 'sku17'), ('w18', 'sku18'), ('w19', 'sku19'), ('w20', 'sku20')]
What we really want though is a dictionary.

We could use a dictionary comprehension to do this:

{widget: sku for widget, sku in zip(widgets, skus)}
{'w1': 'sku1',
 'w2': 'sku2',
 'w3': 'sku3',
 'w4': 'sku4',
 'w5': 'sku5',
 'w6': 'sku6',
 'w7': 'sku7',
 'w8': 'sku8',
 'w9': 'sku9',
 'w10': 'sku10',
 'w11': 'sku11',
 'w12': 'sku12',
 'w13': 'sku13',
 'w14': 'sku14',
 'w15': 'sku15',
 'w16': 'sku16',
 'w17': 'sku17',
 'w18': 'sku18',
 'w19': 'sku19',
 'w20': 'sku20'}
But, recall that the dict object is capable of handling a sequence of 2-element sequences:

dict([('a', 10), ('b', 20)])
{'a': 10, 'b': 20}
So, we can actually use this instead of a comprehension:

dict(zip(widgets, skus))
{'w1': 'sku1',
 'w2': 'sku2',
 'w3': 'sku3',
 'w4': 'sku4',
 'w5': 'sku5',
 'w6': 'sku6',
 'w7': 'sku7',
 'w8': 'sku8',
 'w9': 'sku9',
 'w10': 'sku10',
 'w11': 'sku11',
 'w12': 'sku12',
 'w13': 'sku13',
 'w14': 'sku14',
 'w15': 'sku15',
 'w16': 'sku16',
 'w17': 'sku17',
 'w18': 'sku18',
 'w19': 'sku19',
 'w20': 'sku20'}
Let's finally write our function:

def widget_skus(widgets, skus):
    return dict(zip(widgets, skus))
print(widget_skus(widgets, skus))
{'w1': 'sku1', 'w2': 'sku2', 'w3': 'sku3', 'w4': 'sku4', 'w5': 'sku5', 'w6': 'sku6', 'w7': 'sku7', 'w8': 'sku8', 'w9': 'sku9', 'w10': 'sku10', 'w11': 'sku11', 'w12': 'sku12', 'w13': 'sku13', 'w14': 'sku14', 'w15': 'sku15', 'w16': 'sku16', 'w17': 'sku17', 'w18': 'sku18', 'w19': 'sku19', 'w20': 'sku20'}
Question 2
Given the following data:

suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']
Write a function that given those two inputs, returns a list with all 52 cards, consisting of tuples (rank, suit), i.e.

[
  [('2', 's'), ('3', 's'), ..., ('K', 's'), ('A', 's')],
  [('2', 'h'), ('3', 'h'), ..., ('K', 'h'), ('A', 'h')],
  ...
]
Solution
Let's first see what suits and ranks contain:

suits
'shdc'
ranks
['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
Let's start writing our function to generate the deck of cards:

def deck(suits, ranks):
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return deck
And let's see what we get:

deck(suits, ranks)
[('2', 's'),
 ('3', 's'),
 ('4', 's'),
 ('5', 's'),
 ('6', 's'),
 ('7', 's'),
 ('8', 's'),
 ('9', 's'),
 ('10', 's'),
 ('J', 's'),
 ('Q', 's'),
 ('K', 's'),
 ('A', 's'),
 ('2', 'h'),
 ('3', 'h'),
 ('4', 'h'),
 ('5', 'h'),
 ('6', 'h'),
 ('7', 'h'),
 ('8', 'h'),
 ('9', 'h'),
 ('10', 'h'),
 ('J', 'h'),
 ('Q', 'h'),
 ('K', 'h'),
 ('A', 'h'),
 ('2', 'd'),
 ('3', 'd'),
 ('4', 'd'),
 ('5', 'd'),
 ('6', 'd'),
 ('7', 'd'),
 ('8', 'd'),
 ('9', 'd'),
 ('10', 'd'),
 ('J', 'd'),
 ('Q', 'd'),
 ('K', 'd'),
 ('A', 'd'),
 ('2', 'c'),
 ('3', 'c'),
 ('4', 'c'),
 ('5', 'c'),
 ('6', 'c'),
 ('7', 'c'),
 ('8', 'c'),
 ('9', 'c'),
 ('10', 'c'),
 ('J', 'c'),
 ('Q', 'c'),
 ('K', 'c'),
 ('A', 'c')]
So that's not quite what we want, we want each suit to be a separate list - let's fix that:

def deck(suits, ranks):
    deck = []
    for suit in suits:
        cards = []
        for rank in ranks:
            cards.append((rank, suit))
        deck.append(cards)
    return deck
And let's try that now:

print(deck(suits, ranks))
[[('2', 's'), ('3', 's'), ('4', 's'), ('5', 's'), ('6', 's'), ('7', 's'), ('8', 's'), ('9', 's'), ('10', 's'), ('J', 's'), ('Q', 's'), ('K', 's'), ('A', 's')], [('2', 'h'), ('3', 'h'), ('4', 'h'), ('5', 'h'), ('6', 'h'), ('7', 'h'), ('8', 'h'), ('9', 'h'), ('10', 'h'), ('J', 'h'), ('Q', 'h'), ('K', 'h'), ('A', 'h')], [('2', 'd'), ('3', 'd'), ('4', 'd'), ('5', 'd'), ('6', 'd'), ('7', 'd'), ('8', 'd'), ('9', 'd'), ('10', 'd'), ('J', 'd'), ('Q', 'd'), ('K', 'd'), ('A', 'd')], [('2', 'c'), ('3', 'c'), ('4', 'c'), ('5', 'c'), ('6', 'c'), ('7', 'c'), ('8', 'c'), ('9', 'c'), ('10', 'c'), ('J', 'c'), ('Q', 'c'), ('K', 'c'), ('A', 'c')]]
OK, so this works, but notice how we implemented our code - we started by creating empty lists, and then appending things to them - when we see things like that, and assuming the code is not too complicated, we really should look at comprehensions.

So, let's re-write our function to use comprehensions.

First, for the individual suits, we could generate the cards in the suit this way:

s = 'h'
[(r, s) for r in ranks]
[('2', 'h'),
 ('3', 'h'),
 ('4', 'h'),
 ('5', 'h'),
 ('6', 'h'),
 ('7', 'h'),
 ('8', 'h'),
 ('9', 'h'),
 ('10', 'h'),
 ('J', 'h'),
 ('Q', 'h'),
 ('K', 'h'),
 ('A', 'h')]
And then we would nest this inside another comprehension that loops through each suit:

[
    [(r, s) for r in ranks]
    for s in suits
]
[[('2', 's'),
  ('3', 's'),
  ('4', 's'),
  ('5', 's'),
  ('6', 's'),
  ('7', 's'),
  ('8', 's'),
  ('9', 's'),
  ('10', 's'),
  ('J', 's'),
  ('Q', 's'),
  ('K', 's'),
  ('A', 's')],
 [('2', 'h'),
  ('3', 'h'),
  ('4', 'h'),
  ('5', 'h'),
  ('6', 'h'),
  ('7', 'h'),
  ('8', 'h'),
  ('9', 'h'),
  ('10', 'h'),
  ('J', 'h'),
  ('Q', 'h'),
  ('K', 'h'),
  ('A', 'h')],
 [('2', 'd'),
  ('3', 'd'),
  ('4', 'd'),
  ('5', 'd'),
  ('6', 'd'),
  ('7', 'd'),
  ('8', 'd'),
  ('9', 'd'),
  ('10', 'd'),
  ('J', 'd'),
  ('Q', 'd'),
  ('K', 'd'),
  ('A', 'd')],
 [('2', 'c'),
  ('3', 'c'),
  ('4', 'c'),
  ('5', 'c'),
  ('6', 'c'),
  ('7', 'c'),
  ('8', 'c'),
  ('9', 'c'),
  ('10', 'c'),
  ('J', 'c'),
  ('Q', 'c'),
  ('K', 'c'),
  ('A', 'c')]]
So let's now use that inside our function:

def deck(suits, ranks):
    deck = [
        [(r, s) for r in ranks]
        for s in suits
    ]
    return deck
print(deck(suits, ranks))
[[('2', 's'), ('3', 's'), ('4', 's'), ('5', 's'), ('6', 's'), ('7', 's'), ('8', 's'), ('9', 's'), ('10', 's'), ('J', 's'), ('Q', 's'), ('K', 's'), ('A', 's')], [('2', 'h'), ('3', 'h'), ('4', 'h'), ('5', 'h'), ('6', 'h'), ('7', 'h'), ('8', 'h'), ('9', 'h'), ('10', 'h'), ('J', 'h'), ('Q', 'h'), ('K', 'h'), ('A', 'h')], [('2', 'd'), ('3', 'd'), ('4', 'd'), ('5', 'd'), ('6', 'd'), ('7', 'd'), ('8', 'd'), ('9', 'd'), ('10', 'd'), ('J', 'd'), ('Q', 'd'), ('K', 'd'), ('A', 'd')], [('2', 'c'), ('3', 'c'), ('4', 'c'), ('5', 'c'), ('6', 'c'), ('7', 'c'), ('8', 'c'), ('9', 'c'), ('10', 'c'), ('J', 'c'), ('Q', 'c'), ('K', 'c'), ('A', 'c')]]
So this works fine, but we can use the zip function to make this even simpler.

Of course we cannot just zip suits and ranks since suits only contains 4 characters:

list(zip(suits, ranks))
[('s', '2'), ('h', '3'), ('d', '4'), ('c', '5')]
But, what we could do is repeat each character in suits thirteen times, and zip each of those with the ranks.

suits[0]
's'
suits[0] * 13
'sssssssssssss'
And we can zip that instead:

print(list(zip(ranks, suits[0] * 13)))
[('2', 's'), ('3', 's'), ('4', 's'), ('5', 's'), ('6', 's'), ('7', 's'), ('8', 's'), ('9', 's'), ('10', 's'), ('J', 's'), ('Q', 's'), ('K', 's'), ('A', 's')]
Now all we need to do is repeat this for each suit:

print([list(zip(ranks, suit * 13)) for suit in suits])
[[('2', 's'), ('3', 's'), ('4', 's'), ('5', 's'), ('6', 's'), ('7', 's'), ('8', 's'), ('9', 's'), ('10', 's'), ('J', 's'), ('Q', 's'), ('K', 's'), ('A', 's')], [('2', 'h'), ('3', 'h'), ('4', 'h'), ('5', 'h'), ('6', 'h'), ('7', 'h'), ('8', 'h'), ('9', 'h'), ('10', 'h'), ('J', 'h'), ('Q', 'h'), ('K', 'h'), ('A', 'h')], [('2', 'd'), ('3', 'd'), ('4', 'd'), ('5', 'd'), ('6', 'd'), ('7', 'd'), ('8', 'd'), ('9', 'd'), ('10', 'd'), ('J', 'd'), ('Q', 'd'), ('K', 'd'), ('A', 'd')], [('2', 'c'), ('3', 'c'), ('4', 'c'), ('5', 'c'), ('6', 'c'), ('7', 'c'), ('8', 'c'), ('9', 'c'), ('10', 'c'), ('J', 'c'), ('Q', 'c'), ('K', 'c'), ('A', 'c')]]
So we can rewrite our function this way:

def deck(suits, ranks):
    return [list(zip(ranks, suit * 13)) for suit in suits]
print(deck(suits, ranks))
[[('2', 's'), ('3', 's'), ('4', 's'), ('5', 's'), ('6', 's'), ('7', 's'), ('8', 's'), ('9', 's'), ('10', 's'), ('J', 's'), ('Q', 's'), ('K', 's'), ('A', 's')], [('2', 'h'), ('3', 'h'), ('4', 'h'), ('5', 'h'), ('6', 'h'), ('7', 'h'), ('8', 'h'), ('9', 'h'), ('10', 'h'), ('J', 'h'), ('Q', 'h'), ('K', 'h'), ('A', 'h')], [('2', 'd'), ('3', 'd'), ('4', 'd'), ('5', 'd'), ('6', 'd'), ('7', 'd'), ('8', 'd'), ('9', 'd'), ('10', 'd'), ('J', 'd'), ('Q', 'd'), ('K', 'd'), ('A', 'd')], [('2', 'c'), ('3', 'c'), ('4', 'c'), ('5', 'c'), ('6', 'c'), ('7', 'c'), ('8', 'c'), ('9', 'c'), ('10', 'c'), ('J', 'c'), ('Q', 'c'), ('K', 'c'), ('A', 'c')]]
Question 3
Write a function that receives two arguments:

a list of numbers
a keyword-only argument reverse that defaults to False and indicates an ascending sort, but a value of True indicates a descending sort
Your function should return three values:

a list of the numbers, but sorted (ascending/descending depending on value of reverse)
the minimum value in the list (this is not affected by the value of reverse)
the maximum value in the list (this is not affected by the value of reverse)
Solution
Let's create some sample data first:

data = [10, 3, -5, 3.14, 100, 1]
we can sort this data using the sorted function, as well as specify whether the order shoudl be ascending or descending:

sorted(data)
[-5, 1, 3, 3.14, 10, 100]
sorted(data, reverse=True)
[100, 10, 3.14, 3, 1, -5]
We can find the minimum using the min function:

min(data)
-5
And the maximum using the max function:

max(data)
100
Now, let's just package this up into a function:

def list_info(data, *, reverse=False):
    sorted_data = sorted(data, reverse=reverse)
    minimum = min(data)
    maximum = max(data)
    return sorted_data, minimum, maximum
And let's try it out with our data:

list_info(data)
([-5, 1, 3, 3.14, 10, 100], -5, 100)
list_info(data, reverse=True)
([100, 10, 3.14, 3, 1, -5], -5, 100)
'''