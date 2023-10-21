import unittest

from tester_base import TesterBase, captured_output


class TestTask2(TesterBase):
    """
    Test for methods in file poke_team.py
    """

    def test_limit(self):
        from poke_team import PokeTeam

        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(
                f"Ash's team could not be instantiated: {str(e)}."
            )
            return
        try:
            with captured_output("4 4 1\n1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert (
                str(team)
                == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
            )
        except AssertionError:
            self.verificationErrors.append(
                f"PokeTeam does not handle limit correctly. {str(team)}"
            )

    def test_get_battle_mode(self):
        from poke_team import PokeTeam

        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(
                f"Ash's team could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try to get current battle mode
            s = team.get_battle_mode()
            if s != 0:
                self.verificationErrors.append(
                    f"Get battle mode returns incorrect integer: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_battle_mode method failed. {e}")

    def test_choose_team(self):
        """
        Try to choose team for PokeTeam
        """
        from poke_team import PokeTeam

        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(
                f"PokeTeam could not be instantiated: {str(e)}."
            )
            return
        try:
            with captured_output("7 1 1\n1 1 1") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

    def test_assign_team(self):
        """
        Checking the assign team method of poke_team.py
        """
        from poke_team import PokeTeam

        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(
                f"PokeTeam could not be instantiated: {str(e)}."
            )
            return
        try:
            with captured_output("1 1 1") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        try:
            team.assign_team(1, 1, 1)
        except Exception as e:
            self.verificationErrors.append(
                f"assign_team did not work properly: {str(e)}"
            )
            return

    ### ADD TESTS HERE


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask2)
    unittest.TextTestRunner(verbosity=0).run(suite)
