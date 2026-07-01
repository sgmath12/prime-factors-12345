class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    factors.append(2)
                    number //= 2
            elif number == 6 :
                divisor = 2
                while number > 1 :
                    while number % divisor == 0 :
                        factors.append(divisor)
                        number //= divisor
                    divisor += 1
            else:
                factors.append(number)
        return factors