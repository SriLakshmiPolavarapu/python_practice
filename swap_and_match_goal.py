class Swap:
    def checkGoal(self, s, goal):
        if len(s) != len(goal):
            return "not buddy string"

        for i in range(len(s) - 1):
            temp = s[i]
            s = s[:i] + s[i+1] + temp + s[i+2:]

            if s == goal:
                return "Buddy String"

        return "not a Buddy String"

if __name__ == "__main__":
    obj = Swap()
    s = input("Enter string = ")
    goal = input("Enter goal string  = ")

    res = obj.checkGoal(s, goal)
    print(res)
