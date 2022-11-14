def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
   
    def get_cheapest_fruit(data: str) -> str:
        d = []
        a = []
        ans = 0
        ans1 = ''
    row = data.split("\n")[1:]
    for i in row:
        d.append(float(i.split(',')[1]))
        a.append(str(i.split(",")[0]))

    ans = d[0]
    ans1 = a[0]
    for i in range(len(d)-1):
        if d[i] < ans:
            ans = d[i]
            ans1 = a[i]

    return ans1

data = open("fruits.csv").read()
print(get_cheapest_fruit(data))