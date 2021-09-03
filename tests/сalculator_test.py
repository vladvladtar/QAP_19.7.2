import pytest #импорт библиотеки PyTest, предварительно библиотеку необходимо установить

from app.сalculator_vlad import Calculator # импорт кода тестируемого приложения

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): #проверка корректности умножения, позитивниый тест
        assert self.calc.multiply(self, 3, 7) == 21

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 5, 4) == 21 #проверка корректности умножения, негативный тест

    def test_division_calculate_correctly(self): #проверка корректности деления, позитивниый тест
        assert self.calc.division(self, 21, 7) == 3

    def test_adding_calculate_correctly(self): #проверка корректности сложения, позитивниый тест
        assert self.calc.adding(self, 3, 7) == 10

    def test_subtraction_calculate_correctly(self): #проверка корректности вычитания, позитивниый тест
        assert self.calc.subtraction(self,21, 7) == 14
