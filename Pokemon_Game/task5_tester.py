import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_battle_1(self):
        from battle import Battle

        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "level")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            # Gen IV supremacy >:D
            assert result == "Brock"
        except AssertionError:
            self.verificationErrors.append(f"Brock should win: {result}.")
        try:
            assert str(b.team1) == "Squirtle's HP = 2 and level = 1, Bulbasaur's HP = 4 and level = 2, Bulbasaur's HP = 6 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    def test_battle_2(self):
        from battle import Battle

        try:
            b = Battle("Naka", "Jeffery")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 1 1\n1 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("attack", "defence")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            # Gen IV supremacy >:D
            assert result == "Jeffery"
        except AssertionError:
            self.verificationErrors.append(f"Jeffery should win: {result}.")
        try:
            assert str(b.team2) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 8 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)