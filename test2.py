


def start_tests():
    print("---List Test---")

    number=[1,2,3,4,5,6,7,8,9,10,]
    # read from the list 
    print(number[0])
    print(number[1])
    print(number[2])


    # add elements to the list
    number.append(12)
    print(number)

    # for loop

    for n in number: #prints every item in the list
        print(n)

    # for loop from 0 to 20
    for nums in range(0,21):  # for a range of numbers
        print(nums)


# 1 print numbers lower than 50
# 2 count how many numbers are lower than 50
# 3 the sum of all numbers
# 4 the sum of all numbers greater than zero
# count how many zeros there are



def test1():
    print("test 1")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]

    count=0

    sum=0
    sum_not_zero=0
    zeroes=0

    for n in prices:
        sum += n

        if n>0:
            sum_not_zero+=1
        
        if n==0:
            zeroes +=1

        if n<50:
            print(n)
            count+=1
    
    print(f"There are {count} prices lower than $50")
    






def test2():
    users =  [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        },
    ]
    # count=0
    
    print(len(users)) # print the number of users
    for user in users:    
        print (user["name"])



    print("---------------")
    for user in users:
        if user["color"].lower() == "pink":
            print(user["name"])

    
        
#     if user<0:
#                 print(user)
#                 count+=1
# print (f"there are {count} users in ")

def test3():
    print("--------------Test 3-------------")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]

    solution = prices[0]
    for price in prices:
        if price > solution:
            solution = price
            
    print("The greatest number is" +  str(solution))

start_tests()
test1()
test2()
test3()
