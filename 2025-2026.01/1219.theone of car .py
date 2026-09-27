# 定义一个汽车类
class Car:
    """ 汽车类，包含制造商、型号、年份、价格四个属性"""
    def __init__(self, make, model, year, price):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__price = price

    def get_make(self):
        """获取汽车制造商"""
        return self.__make 
    def get_model(self):
        """获取汽车型号"""
        return self.__model 
    def get_year(self):
        """获取汽车年份"""
        return self.__year 
    def get_price(self):
        """获取汽车价格"""
        return self.__price
    def set_price(self, new_price):
        """更新汽车价格"""
        self.__price = new_price
    def __str__(self):
        """返回汽车的描述信息"""
        return f"{self.__year} {self.__make} {self.__model} - 价格：{self.__price}元"

# 创建一个汽车销售系统，多家门店多个系统
class CarSalesSystem:
#********** Begin *********#
    def __init__(self):
        self.cars = []  # 初始化汽车库存列表
        self.salespeople = []  # 初始化销售员列表

    def add_car(self, car: Car):
        self.cars.append(car)   
    def add_salesperson(self, salesperson):
        self.salespeople.append(salesperson)
    def sell_car(self, car_index:int):
        if 0 <= car_index < len(self.cars):
            sold_car = self.cars.pop(car_index)
            return sold_car
        return None
        
            
#请补充完成汽车销售类。
#********** End *********#
    def __str__(self):#打印所有库存
        outStr = ''
        for cari in self.cars: 
            outStr += str(cari) + '\n'
        return '现有库存车，如下：\n' + outStr


class Person:
#********** Begin *********#
#请补充完成Person类。
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level
#********** End *********#

# 定义一个经理类，负责管理销售价格
class Manager(Person):  
#********** Begin *********#
    def __init__(self, name, id, level):
        super().__init__(name, id, level)
    def set_price(self, car:Car, new_price:float):
        car.set_price(new_price)
#请补充完成Manager类。
#********** End *********#
    def input_car(self, sellSys:CarSalesSystem):
        while True:
            info = input().split()#空格分，输入制造商、型号、年份、价格四个属性
            if not info:#空输入退出
                break
            info[2] = int(info[2])
            info[3] = float(info[3])#万为单位
            car = Car(*info)
            sellSys.add_car(car)

        
# 定义一个销售员类
class Salesperson(Person):
#********** Begin *********#
    def __init__(self, name, id, level, commission_rate, sellSys:CarSalesSystem):
        super().__init__(name, id, level)
        self.commission_rate = commission_rate
        self.sellSys = sellSys
        self.commission = 0.0  # 初始化佣金总额为0.0
        self.soldlist = []  # 初始化已售汽车列表
        sellSys.add_salesperson(self)
    def sell_car(self, car_index:int):
        car = self.sellSys.sell_car(car_index)
        if car is None:
        
            return
        comm = car.get_price() * self.commission_rate
        self.commission += comm
        self.soldlist.append(car)
#请补充完成Salesperson类。
#********** End *********#
        print(f"{self.name}销售了一辆{car.get_make()} {car.get_model()}，获得佣金{comm}元。")
        

if __name__ == '__main__':
    
    store1 = CarSalesSystem()#1号店销售系统
    
    manager1 = Manager('老王', '001', 'Manager')
    
    seller1 = Salesperson('小张', '101', 'Seller', 0.01, store1)
    seller2 = Salesperson('小明', '102', 'Seller', 0.02, store1)
    
    manager1.input_car(store1)
    print(store1)
    
    car_index = 1
    car1 = store1.cars[car_index] #选一辆车
    print(car1)
    manager1.set_price(car1, 100)
    print(car1)
    
    seller1.sell_car(car_index)
    car_index = 2
    car2 = store1.cars[car_index] #选一辆车
    print(car2)
    seller1.sell_car(car_index)
    print('销售员{}当月佣金总共{}元。'.format(seller1.name, seller1.commission))
    
    car_index = 0
    car3 = store1.cars[car_index] #选一辆车
    seller2.sell_car(car_index)
    print('销售员{}当月佣金总共{}万元。'.format(seller2.name, seller2.commission))
    

    print(store1)