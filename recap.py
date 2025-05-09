
def Hello():
    print('hello from python')

def test_1():
    name = 'Jeff'
    last = 'name'

    print(name + ' ' + last)

def test_if(age):
    if age < 21:
        print('you can not drink')
    else:
        print('please have a beer')

def test_for():
    nums = [2,4,3,157,8]
    total = 0
    for num in nums:
        total += num
        print(num)
    print('The total sum is: ' + str(total))

def test_dict():
    dog = { 
        'name': 'lola',
        'age': 3
    }
    print(dog)
    print(dog['name'])

def test_list():
    products = [
    {"title": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
    {"title": "Yoga Mat", "price": 19.99, "category": "Fitness"},
    {"title": "Coffee Maker", "price": 49.99, "category": "Home Appliances"},
    {"title": "Bluetooth Headphones", "price": 79.99, "category": "Electronics"},
    {"title": "Running Shoes", "price": 59.99, "category": "Footwear"},
    {"title": "Desk Lamp", "price": 22.50, "category": "Office Supplies"}
]
    
    total = 0
    for item in products: #scan each item in products
        item['title']     #find the title in each item
        print(item['title'])  #print the title

        total += item['price']
        
    print('The total sum is: ' + str(total))


Hello()
test_1()
test_if(19)
test_for()
test_dict()
test_list()