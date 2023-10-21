import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_battle_1(self):
        from battle import Battle
        try:
            b = Battle("Steve", "Remi")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 0\n0 2 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Remi"
        except AssertionError:
            self.verificationErrors.append(f"Remi should win: {result}.")
        try:
            assert str(b.team2) == "Squirtle's HP = 1 and level = 2, Bulbasaur's HP = 1 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team1)}")

    def test_battle_2(self):
        from battle import Battle
        try:
            b = Battle("Stephanie", "Jonathan")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 2\n1 0 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Stephanie"
        except AssertionError:
            self.verificationErrors.append(f"Stephanie should win: {result}.")
        try:
            assert str(b.team1) == "Squirtle's HP = 5 and level = 3, Squirtle's HP = 2 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    def test_fight(self):
        from battle import Battle
        try:
            b = Battle("Sam", "Ricky")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 0\n0 0 1") as (inp, out, err):
                b.rotating_mode_battle()
                result = b.fight(b.pokemon1, b.pokemon2)
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Bulbasaur"
        except AssertionError:
            self.verificationErrors.append(f"Bulbasaur should win: {result}.")
        try:
            with captured_output("1 0 0\n0 1 0") as (inp, out, err):
                b.rotating_mode_battle()
                result = b.fight(b.pokemon1, b.pokemon2)
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Charmander"
        except AssertionError:
            self.verificationErrors.append(f"Charmander should win: {result}.")

    def test_rotate(self):
        from battle import Battle
        try:
            b = Battle("Jack", "Taylor")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 0") as (inp, out, err):
                queue = b.team1.choose_team(1, None)
                b.team_array_1 = b.team1.assign_team(queue[0], queue[1], queue[2])
                b.rotate(b.team_array_1)
                result = b.team_array_1.array[b.team_array_1.front].NAME
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Bulbasaur"
        except AssertionError:
            self.verificationErrors.append(f"Bulbasaur should be at the front now: {result}.")
        try:
            with captured_output("0 1 1") as (inp, out, err):
                queue = b.team1.choose_team(1, None)
                b.team_array_1 = b.team1.assign_team(queue[0], queue[1], queue[2])
                b.rotate(b.team_array_1)
                result = b.team_array_1.array[b.team_array_1.front].NAME
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Squirtle"
        except AssertionError:
            self.verificationErrors.append(f"Squirtle should be at the front now: {result}.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)