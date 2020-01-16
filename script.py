# Define your functions
def coffee_bot():
  print('Welcome to the cafe !')
  name = input('Can I get your name please ? ')
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {} !'.format(size,drink_type))
  print('Thanks, {} Your drink will be ready shortly.'.format(name))
def get_size():
  res = input('What size of drink can I get for you ? \n[a] Small \n[b] Medium \n[c] Large \n')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res =='c':
    return 'large'
  else: 
    print_message()
    get_size()
def print_message():
  print ('I\'m sorry, I did not understand your selection.       Please enter the corresponding letter for you response.')

def get_drink_type():
  res = input('What type of drink would you like ? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte')
  if res =='a':
    return 'brewed coffeee'
  elif res =='b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else : 
    print_message()
    get_drink_type()
def order_latte():
  res = input(' And what kind of milk for your latte ? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk')
  if res == 'a':
    return 'latte'
  elif res =='b':
    return 'non-fat'
  elif res =='c':
    return 'soy latte'
  else:
    print_message()
    order_latte()
# Call coffee_bot()!
coffee_bot()