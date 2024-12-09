import unittest
import runner
import runner_and_tournament as run
from functools import wraps


def skip_if_frozen(method):
    @wraps(method)  # Сохраняем метаданные исходных функций
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            raise unittest.SkipTest(f'Тесты в этом кейсе заморожены.')
        return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    """
    Метод setUp используется для инициализации общих объектов tom и jon,
    чтобы не создавать их заново для каждого теста.
    Два метода, walk_multiple_times и run_multiple_times, добавлены
    для выполнения повторяющихся действий с использованием циклов,
    что делает код короче и легче читаемым.
    """
    is_frozen = False

    def setUp(self):
        self.tom = runner.Runner('Tom')
        self.jon = runner.Runner('Jon')

    def walk_multiple_times(self, runner_instance, times):
        for _ in range(times):
            runner_instance.walk()

    def run_multiple_times(self, runner_instance, times):
        for _ in range(times):
            runner_instance.run()

    @skip_if_frozen
    def test_walk(self):
        self.walk_multiple_times(self.tom, 10)
        self.assertEqual(self.tom.distance, 50)

    @skip_if_frozen
    def test_run(self):
        self.run_multiple_times(self.jon, 10)
        self.assertEqual(self.jon.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        self.walk_multiple_times(self.tom, 10)
        self.run_multiple_times(self.jon, 10)
        self.assertNotEqual(self.tom.distance, self.jon.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = run.Runner('Усэйн', speed=10)
        self.runner2 = run.Runner('Андрей', speed=9)
        self.runner3 = run.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = run.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[1] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(self.all_results[1][2] == 'Ник')

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = run.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[2] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(self.all_results[2][2] == 'Ник')

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = run.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[3] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(self.all_results[3][3] == 'Ник')
