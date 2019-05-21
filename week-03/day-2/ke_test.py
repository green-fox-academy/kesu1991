import unittest
from ke_work import apples, sum_method, is_anagram, count, fibo, Sharpie, Animal, cows_bulls

###### Test Apples
class TestApples(unittest.TestCase):

    def test_ifstring(self):
        a = apples("apple")
        self.assertEqual(a.get_apple(), "apple")

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestApples('test_ifstring'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)


###### Test Sum
class TestSum(unittest.TestCase):

    def test_sum_empty_list(self):
        s = sum_method([])
        self.assertEqual(s.get_sum(), 0)

    def test_sum_one_element(self):
        s = sum_method([3])
        self.assertEqual(s.get_sum(), 3)

    def test_sum_multiple_element(self):
        s = sum_method([1,2,3])
        self.assertEqual(s.get_sum(), 6)
    
    def test_sum_None_element(self):
        s = sum_method(None)
        self.assertEqual(s.list_int, None)

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestSum('test_sum_empty_list'))
    suite.addTest(TestSum('test_sum_one_element'))
    suite.addTest(TestSum('test_sum_multiple_element'))
    suite.addTest(TestSum('test_sum_None_element'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)


###### Test Anagram
class TestAnagram(unittest.TestCase):

    def test_anagram(self):
        self.assertEqual(is_anagram("dog","god"), True)

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestAnagram('test_anagram'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)


###### Test Count Letters
class TestCountLetters(unittest.TestCase):

    def test_count_letters(self):
        self.assertEqual(count("stronggest"), {'g': 2, 'o': 1, 'n': 1, 'e': 1, 't': 2, 's': 2, 'r': 1})

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestCountLetters('test_count_letters'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)


###### Test Fibonacci
class TestFibonacci(unittest.TestCase):

    def test_fibonacci_positive_integer(self):
        self.assertEqual(fibo(4), 3)
        self.assertEqual(fibo(5), 5)
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(3), 2)

    def test_fibonacci_negative_integer(self):
        self.assertEqual(fibo(-4), False)
    
    def test_fibonacci_string(self):
        self.assertEqual(fibo("4"), 3)
        
if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestFibonacci('test_fibonacci_positive_integer'))
    suite.addTest(TestFibonacci('test_fibonacci_negative_integer'))
    suite.addTest(TestFibonacci('test_fibonacci_string'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)


###### Test Sharpie
class TestSharpie(unittest.TestCase):

    def test_sharpie_positive_integer(self):
        s = Sharpie("red", 50.0)
        self.assertEqual(s.use(10), ("red", 50, 90))

    def test_sharpie_string_input(self):
        s = Sharpie("red", "50")
        self.assertEqual(s.use("10"), ("red", 50, 90))
    
    def test_sharpie_negative_input(self):
        s = Sharpie("red", -50)
        self.assertEqual(s.use(-10), ("red", 50, 90))

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestSharpie('test_sharpie_positive_integer'))
    suite.addTest(TestSharpie('test_sharpie_string_input'))
    suite.addTest(TestSharpie('test_sharpie_negative_input'))
    #suite.addTest(TestSharpie('test_sum_None_element'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)


###### Test Animal
class TestAnimal(unittest.TestCase):

    def test_animal_positive_integer(self):
        s = Animal(40, 40)
        self.assertEqual(s.eat(2), 38)

    def test_animal_string_input(self):
        s = Animal("40", "40")
        self.assertEqual(s.drink("2"), 38)

    def test_animal_negative_input(self):
        s = Animal(-40, -40)
        self.assertEqual(s.play(-2)[0], 42)

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestAnimal('test_animal_positive_integer'))
    suite.addTest(TestAnimal('test_animal_string_input'))
    suite.addTest(TestAnimal('test_animal_negative_input'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)

###### Test Cow and Bull Games
class TestCowBull(unittest.TestCase):

    def test_CowBull_play_game(self):
        p = cows_bulls()
        p.makeNumber()
        self.assertEqual(p.playgame([4,6,3,6]) , "Game Over!")

if __name__ == '__main__':

    # Create test set
    suite = unittest.TestSuite()
    suite.addTest(TestCowBull('test_CowBull_play_game'))

    # Run test set
    runner = unittest.TextTestRunner()
    runner.run(suite)

