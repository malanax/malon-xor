
while True:
  try:
    age = int(input('Enter age:'))
    result = 10/age

   # raise ValueError('Cut it out')      # we manually raise an error. A value error                                          which enters the except of Value Error.
                                        # If we comment that exception, we raise the red error that's not chatched by that

  except ZeroDivisionError as err:
    print(f"Enter e number that's not 0. {err}")
    break
  #except ValueError as err:
  #  print(f'Enter a number! {err}')
  #  continue
  else:
    print(f'Thank you! The result is: {result}')
    break
  finally:
    print('Ok, we are done!')
  print('Can you hear me?')  # This never gets printed because  all the cases are                                   breaking or continuing
