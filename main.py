# Recitation Activity #3
# I completed this code in room:

class Button:
    '''
        >>> x = Button(3, 'A')
        >>> y = Button(8, 't')
        >>> x
        A
        >>> print(x)
        Button A at position 3
        >>> y*5
        'ttttt'
    '''

    def __init__(self, position, key):
        # YOUR CODE STARTS HERE
        pass


class Keyboard:
    """
        A sequence of Button objects in a Python list, storing these Buttons in a dictionary where the keys will be 
        integers that represent the position on the Keyboard, and the values will be the respective Button objects. 
        >>> b1 = Button(0, "H")
        >>> b2 = Button(1, "i")
        >>> b3 = Button(3, "m")
        >>> b4 = Button(4, "o")
        >>> b5 = Button(5, " ")
        >>> k = Keyboard([b1, b2, b3, b4, b5])
        >>> k.buttons[0].key
        'H'
        >>> k.press(1)
        'i'
        >>> k._type([0, 1])
        'Hi'
        >>> k._type([1, 0])
        'iH'
        >>> k._type([0, 1, 5, 3, 4, 3])
        'Hi mom'
        >>> b1.pressed
        3
        >>> b2.pressed
        4
    """

    def __init__(self, button_list):
    # YOUR CODE STARTS HERE
        self.button_list = button_list
        self.button_list = {}
        for i in self.button_list:
            self.buttons[i.position] = i
            
    def press(self, info):
        """ 
            Parameters:
              info: position of the button pressed
            Returns:
               Button's output
        """
        # YOUR CODE STARTS HERE
        self.buttons[info].pressed1+=1
        return self.buttons[info].key
    
    def _type(self, typing):
        """ 
            Parameters:
              typing: list of positions of buttons pressed
            Returns:
               Total output
        """
        # YOUR CODE STARTS HERE 
        newList = []
        for i in list1:
            newList.append(self.buttons[i].key)
        return ''.join(newList)
if __name__ == '__main__':
    import doctest
    doctest.testmod()