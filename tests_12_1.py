import runner
import unittest


class RunnerTest(unittest.TestCase):
    """
    Метод setUp используется для инициализации общих объектов tom и jon,
    чтобы не создавать их заново для каждого теста.
    Два метода, walk_multiple_times и run_multiple_times, добавлены
    для выполнения повторяющихся действий с использованием циклов,
    что делает код короче и легче читаемым.
    """

    def setUp(self):
        self.tom = runner.Runner('Tom')
        self.jon = runner.Runner('Jon')

    def walk_multiple_times(self, runner_instance, times):
        for _ in range(times):
            runner_instance.walk()

    def run_multiple_times(self, runner_instance, times):
        for _ in range(times):
            runner_instance.run()

    def test_walk(self):
        self.walk_multiple_times(self.tom, 10)
        self.assertEqual(self.tom.distance, 50)

    def test_run(self):
        self.run_multiple_times(self.jon, 10)
        self.assertEqual(self.jon.distance, 100)

    def test_challenge(self):
        self.walk_multiple_times(self.tom, 10)
        self.run_multiple_times(self.jon, 10)
        self.assertNotEqual(self.tom.distance, self.jon.distance)


if __name__ == '__main__':
    unittest.main()
