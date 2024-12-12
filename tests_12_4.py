import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r1 = Runner('Tom', -5)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r2 = Runner(2)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',
                            exc_info=True)



