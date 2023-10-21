import unittest

from tester_base import TesterBase


class TestTask1(TesterBase):
    # Test methods inside pokemon_base that are not abstract
    def test_set_hp(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try the set hp method
            c.set_HP(10)
            if c.get_HP() != 10:
                self.verificationErrors.append(
                    f"HP did not get set correctly: {c.get_HP()}"
                )
        except Exception as e:
            self.verificationErrors.append(f"set_HP method failed. {e}")

    def test_get_hp(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try the get hp method
            s = c.get_HP()
            if s != 7:
                self.verificationErrors.append(
                    f"get_hp method did not return hp correctly: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_hp method failed. {e}")

    def test_set_level(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try the set level method
            c.set_level(5)
            if c.get_level() != 5:
                self.verificationErrors.append(
                    f"get_level method did not return correct level: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_level method failed. {e}")

    def test_get_level(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try the get level method
            s = c.get_level()
            if s != 1:
                self.verificationErrors.append(
                    f"get_level method did not return correct level: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_level method failed. {e}")

    def test_level_up(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try the level up method which may be used during battle
            c.level_up()
            if c.get_level() != 2:
                self.verificationErrors.append(
                    f"get_level method did not level up correctly: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_level method failed. {e}")

    def test_get_poke_type(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Try to get pokemon's poke type
            s = c.get_poke_type()
            if s != "Fire":
                self.verificationErrors.append(
                    f"get_poke_type method did not return correct hp: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_poke_type method failed. {e}")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)
