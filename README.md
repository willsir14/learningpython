* Learning Python
** Decorator of python
*** Decorator is basically function enhancer 
*** Metaphor of decorator can be gift wrapper of the gift
*** Lets consider a simple example
#+BEGIN_SRC python
  def prettier(func):
      print("Inside prettier")
      def wrapper():
          print("Making pretty")
          func()
      return wrapper

  @prettier
  def ordinary_gift():
      print("My ordinary gift")

  ordinary_gift()

  print("Also This will produce same result")

  # @prettier is syntactic sugar of following
  ordinary_gift = prettier(ordinary_gift)
  ordinary_gift()
#+END_SRC
