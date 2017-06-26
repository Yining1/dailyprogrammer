# today, your challenge is to create a program that will take a series of numbers (5, 3, 15), and find how those numbers
# can add, subtract, multiply, or divide in various ways to relate to eachother.
# This string of numbers should result in 5 * 3 = 15, or 15 /3 = 5, or 15/5 = 3.
# When you are done, test your numbers with the following strings:
# 4, 2, 8
# 6, 2, 12
# 6, 2, 3
# 9, 12, 108
# 4, 16, 64
# For extra credit, have the program list all possible combinations.
# for even more extra credit, allow the program to deal with strings of greater than three numbers.
# For example, an input of (3, 5, 5, 3) would be 3 * 5 = 15, 15/5 = 3. When you are finished,
# test them with the following strings.
# 2, 4, 6, 3
# 1, 1, 2, 3
# 4, 4, 3, 4
# 8, 4, 3, 6
# 9, 3, 1, 7

# I apologize, this one's really clunky

class numbers:
    def __init__(self, input):
        self.input = [int(i) for i in input.split(", ")]

    def sort(self):
        counter = 0
        while (counter < 3):
            if (self.input[counter] + self.input[(counter + 1) % 3] == self.input[(counter + 2) % 3]):
                print str(self.input[counter]) + " + " + str(self.input[(counter + 1) % 3]) +  " = " + \
                      str(self.input[(counter + 2) % 3])
            if (self.input[counter] - self.input[(counter + 1) % 3] == abs(self.input[(counter + 2) % 3])):
                if (self.input[counter] - self.input[(counter + 1) % 3] <= 0):
                    print str(self.input[(counter + 1) % 3]) + " - " + str(self.input[counter]) + " = " + \
                          str(self.input[(counter + 2) % 3])
                else:
                    print str(self.input[counter]) + " - " + str(self.input[(counter + 1) % 3]) + " = " + \
                          str(self.input[(counter + 2) % 3])
            if (self.input[counter] * self.input[(counter + 1) % 3] == self.input[(counter + 2) % 3]):
                print str(self.input[counter]) + " * " + str(self.input[(counter + 1) % 3]) + " = " + \
                      str(self.input[(counter + 2) % 3])
                print str(self.input[(counter + 2) % 3]) + " / " + str(self.input[counter]) + \
                          " = " + str(self.input[(counter + 1) % 3])
                print str(self.input[(counter + 2) % 3]) + " / " + str(self.input[(counter + 1) % 3]) + \
                      " = " + str(self.input[counter])
            counter += 1

if __name__ == '__main__':
    decipher = numbers("4, 16, 20")
    decipher.sort()

