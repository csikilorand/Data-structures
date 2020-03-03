class Element():
    def __init__(self, element):
        self.element = element

    def get_element(self):
        return self.element

class Dynamic_Array():
    def __init__(self, element):
        self.capacity = 1
        self.length = self.capacity
        self.elements = [None] * self.capacity
        self.elements[0] = element

    def add_element(self, element):
           if self.capacity >= self.length:
               self.__resize__()
           self.elements[self.capacity] = element
           self.capacity += 1
  
    def __resize__(self):
        self.length = 2* self.length
        new_array = [None] * self.length
        for i in range(self.capacity):
            new_array[i] = self.elements[i]
        self.elements = new_array
    
    def add_element_index(self, element, index):
        if index > self.capacity:
            raise Exception('Index out of bound')
        if self.capacity >= self.length:
            self.__resize__()
        new_array = [None] * self.length
        i =0
        while i < index:
            new_array[i] = self.elements[i]
            i += 1
        new_array[index] = element
        while i != self.capacity:
            new_array[i+1] = self.elements[i]
            i += 1
        self.capacity += 1
        self.elements = new_array
    
    def remove_last_element(self):
        self.elements[self.capacity] = None
        self.capacity -= 1    

    def remove_element_index(self, index):
        new_array = [None] * (self.length-1)
        for i in range(self.capacity):
            if i != index :
                new_array[i] = self.elements[i]

        self.capacity -= 1

    def clear_array(self):
        for i in range(self.capacity):
            self.elements[i] = None
            self.capacity = 0
            self.length = self.capacit

    def remove_given_element(self, element):
        new_array = [None] * (self.length - 1)
        index =0
        for i in range(self.capacity):
            if self.elements[i].get_element() == element.get_element():
                index = i
                break
            else:
                new_array[i] = self.elements[i]
        
        while (index+1) < self.capacity:
            new_array[index]= self.elements[index+1]
            index += 1

        self.elements = new_array
            

        self.capacity -= 1        

    def print_array(self):
        for i in range(self.capacity):
            print(self.elements[i].get_element())

elem1 = Element(50)
elem2 = Element(60)
myDynamicArray = Dynamic_Array(elem1)
myDynamicArray.add_element(elem2)
myDynamicArray.add_element(Element(3))
myDynamicArray.add_element(Element(66))
myDynamicArray.add_element(Element(560))
myDynamicArray.add_element_index(element=Element('p'), index=3)
myDynamicArray.add_element_index(element=Element('s'), index=4)
myDynamicArray.remove_given_element(element=Element('p'))
myDynamicArray.print_array()