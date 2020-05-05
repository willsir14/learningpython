# Decorator is basically wrapper for function as Gift paper is wrapper for the GIFT

def special_gift(ordinary_gift):
    def gift_wrapper(paper_color):
        print("I am making gift prettier with")
        print(ordinary_gift(paper_color))
    return gift_wrapper

@special_gift
def ordinary_gift(paper):
    return paper
ordinary_gift("Blue paper")

# Following line code is equivalent to @special_gift
# ordinary_gift = special_gift(ordinary_gift)
# ordinary_gift("Red paper")

