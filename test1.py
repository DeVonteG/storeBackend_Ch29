


def run_test():
    print("Test 1-dictionary")


    me={
        "first": "DeVonte",
        "last": "Gray",
        "age": 30,
        "hobbies":["Video games","music"],
        "address":{
            "street": "Flour St.",
            "number": "1234",
            "city": "London",
            "state": "GA",
            "zip": "31047"
        }

    }
    print(me)
    print(me["first"] + " " + me["last"])


    # change values
    me["age"] = me["age"] + 1
    me["age"] = 99

    # add new keys
    me["preferred_color"]="Blue"
    print(me)

    # read if exist
    if "middle_name" in me:  #checks for existence
        print(me["middle_name"])

    print("-----------------address--------------------")

    address= me["address"]
    print(address)
    print("--------------address type------------")
    print(type(address))

    print("----------formatted strings--------------------")

    print(f'{address["number"]} {address["street"]}. {address["city"]},{address["state"]}, {address["zip"]}')

    


run_test()