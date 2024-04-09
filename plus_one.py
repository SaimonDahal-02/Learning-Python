class NewClass: 
    def is_two_digit(self, n):
        return 10 <= n < 100
    
    def plusOne(self, a):
        for i in reversed(range(len(a))):
            sum = a[i] + 1 
            if self.is_two_digit(sum):
                ones = sum % 10
                tens = sum // 10
                a[i] = ones
                if i == 0 and tens !=0:
                    a.insert(0, tens)
            else:
                ones = sum % 10
                tens = sum // 10
                a[i] = ones
                break

        print('a:', a)


s = NewClass()
s.plusOne([1, 2, 3])
s.plusOne([6, 2, 9])
s.plusOne([8, 9])
s.plusOne([9, 9, 9, 9])