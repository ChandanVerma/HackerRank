class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        N = self.__elements
        for i in range(len(N)):
            for j in range(len(N)):
                current_difference = abs(N[i] - N[j])
                self.maximumDifference = max(current_difference, self.maximumDifference)

        return self.maximumDifference


	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)