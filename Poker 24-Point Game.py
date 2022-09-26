
from itertools import product, permutations

def remove(temp):
    characters = "()"
    string = temp
    #============ 去兩個括號 =====================
    string = ''.join(x for x in string if x not in characters)
    sum = eval(string)
    if sum == 24:
        return True, string
    #============== 去第一個括號 ===================
    string = temp
    num = 0
    for i in range(len(string)):
        if string[i] == '(': num = num + 1
        elif string[i] == ')': num = num - 1

        if string[i] == '(' and num == 1 :
            ss = string[:i] + string[i+1:]
        elif string[i] == ')' and num == 0:
            ss = ss[:i-1] + ss[i-1+1:]
            break
    sum = eval(ss)
    if sum == 24:
        return True, ss
    #================ 去第二個括號 =========================
    num = 0
    ss = temp
    string = temp
    done = False
    for i in range(len(string)):
        if string[i] == '(': num = num + 1
        elif string[i] == ')': num = num - 1

        if string[i] == '(' and num == 2 :
            ss = string[:i] + string[i+1:]
            done = True
        elif string[i] == ')' and num == 1:
            ss = ss[:i-1] + ss[i-1+1:]
            break
    right = left = 0
    if done == False:
        for i in range(len(string)):
            if string[i] == '(' :
                left = left + 1
            elif string[i] == ')' :
                right = right + 1
            if left == 2:
                ss = string[:i] + string[i + 1:]
                left = left + 1
            elif right == 2:
                ss = ss[:i-1 ]
                break
    sum = eval(ss)
    if sum == 24:
        return True, ss

    return False, ss

def addBrackets(new_list):
    temp = new_list.copy()
    bracket = []
    for i in range(5):
        if i == 0: #1+(2+(3+4))
            temp.insert(2, '(')
            temp.insert(5, '(')
            temp.insert(9, ')')
            temp.insert(9, ')')
        elif i == 1: #1+((2+3)+4)
            temp.insert(2, '(')
            temp.insert(2, '(')
            temp.insert(7, ')')
            temp.insert(10, ')')
        elif i == 2: #(1+2)+(3+4)
            temp.insert(0, '(')
            temp.insert(4, ')')
            temp.insert(6, '(')
            temp.insert(10, ')')
        elif i == 3: #(1+(2+3))+4
            temp.insert(0, '(')
            temp.insert(3, '(')
            temp.insert(7, ')')
            temp.insert(8, ')')
        elif i == 4: #((1+2)+3)+4
            temp.insert(0, '(')
            temp.insert(1, '(')
            temp.insert(5, ')')
            temp.insert(8, ')')

        str = "".join(temp)
        bracket.append(str)

        temp.clear()
        temp = new_list.copy()

    return bracket

def combinationGenerator(formula):
    operator = list(product('+-*/', repeat=3))
    new_list = []
    for i in range(len(operator)):
        new_list.extend( [ formula[0],operator[i][0],formula[1],operator[i][1],
                       formula[2],operator[i][2],formula[3] ] )
        bracket = addBrackets(new_list) # 括號
        for j in range(len(bracket)):
            try:
                sum = eval(bracket[j])
            except:
                sum = 0
            new_list.clear()
            if sum == 24:
                done, ss = remove(bracket[j])
                if done == True:
                    ss = ss + "=24"
                    return True, ss
                else:
                    bracket[j] = bracket[j] + "=24"
                    return True, bracket[j]
    return False, "No Solution!"


if __name__ == '__main__':
    n = 0
    formula = []
    while True:
        while True:
            num1,num2,num3,num4 = input("Input four number: ").split()
            if int(num1) == 0 and int(num2) == 0 and int(num3) == 0 and int(num4) == 0:
                quit()
            try:
                if int(num1) > 13 or int(num1) < 1:
                    print("1st Out Of Range!")
                elif int(num2) > 13 or int(num2) < 1:
                    print("2nd Out Of Range!")
                elif int(num3) > 13 or int(num3) < 1:
                    print("3rd Out Of Range!")
                elif int(num4) > 13 or int(num4) < 1:
                    print("4th Out Of Range!")
                else:
                    formula.append(num1)
                    formula.append(num2)
                    formula.append(num3)
                    formula.append(num4)
                    break
            except:
                print("Error Input!")

        p = list(permutations(formula))
        for j in p:
            done, ans = combinationGenerator(j)
            if done == True:
                break
        print(ans)
        n = 0
        done = False
        formula.clear()



