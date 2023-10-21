import unittest

from tester_base import TesterBase, captured_output

class TestTask3(TesterBase):

    def test_battle_1(self):
        from battle import Battle

        try:
            b = Battle("Keith", "Lucas")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 0 1\n1 3 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "It's a draw"
        except AssertionError:
            self.verificationErrors.append(f"It should be a draw: {result}.")

    def test_battle_2(self):
        from battle import Battle

        try:
            b = Battle("James", "Will")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("3 1 0\n1 1 2") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "James"
        except AssertionError:
            self.verificationErrors.append(f"James should win: {result}.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)