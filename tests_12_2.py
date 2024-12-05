import runner_and_tournament as run
import unittest


class TournamentTest(unittest.TestCase):
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

    def test_tournament_run_1(self):
        tournament = run.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[1] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    def test_tournament_run_2(self):
        tournament = run.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[2] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    def test_tournament_run_3(self):
        tournament = run.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[3] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
