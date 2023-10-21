import unittest

from tester_base import TesterBase


class TestTask1(TesterBase):
    """
    Test methods for each Pokemon Class
    """

    # Test Charmander
    def test_charmander_string(self):
        from pokemon import Charmander


        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test the Charmander string method
            s = str(c)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(
                    f"String method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_charmander_name(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test get name method of Charmander
            s = c.get_name()
            if s != "Charmander":
                self.verificationErrors.append(
                    f"get_name method did not return correctly: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_name method failed. {e}")

    def test_charmander_attack(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test get attack method of Charmander
            s = c.get_attack()
            if s != 7:
                self.verificationErrors.append(
                    f"get_attack method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_attack method failed. {e}")

    def test_charmander_defence(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test get defence method of Charmander
            s = c.get_defence()
            if s != 4:
                self.verificationErrors.append(
                    f"get_defence method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_defence method failed. {e}")

    def test_charmander_speed(self):
        from pokemon import Charmander

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test get speed method of Charmander
            s = c.get_speed()
            if s != 8:
                self.verificationErrors.append(
                    f"get_speed method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_speed method failed. {e}")

    def test_charmander_attacked_damage(self):
        from pokemon import Charmander
        from pokemon import Bulbasaur
        from pokemon import Squirtle

        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}"
            )
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}"
            )
        try:
            # Test Charmander's calculate attacked damage method
            out = c.calculate_attacked_damage(b)
            if out != 6:
                self.verificationErrors.append(
                    f"calculate_attacked_damage method did not return correct hp: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"calculate_attacked_damage method failed. {e}"
            )
        try:
            c = Charmander()
            out = c.calculate_attacked_damage(s)
            if out != -1:
                self.verificationErrors.append(
                    f"calculated_attacked_damage did not return correct hp: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"calculate_attacked_damage method failed. {e}"
            )

    # Test Bulbasaur
    def test_bulbasaur_string(self):
        """
        Test Bulbasaur Class
        """
        from pokemon import Bulbasaur

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test Bulbasaur string method
            s = str(b)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(
                    f"String method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_bulbasaur_name(self):
        from pokemon import Bulbasaur

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check the get name method of Bulbasaur
            s = b.get_name()
            if s != "Bulbasaur":
                self.verificationErrors.append(
                    f"get_name method did not return correctly: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_name method failed. {e}")

    def test_bulbasaur_attack(self):
        from pokemon import Bulbasaur

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test the get attack value of Bulbasaur
            s = b.get_attack()
            if s != 5:
                self.verificationErrors.append(
                    f"get_attack method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_attack method failed. {e}")

    def test_bulbasaur_defence(self):
        from pokemon import Bulbasaur

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}."
            )
            return
        try:
            # Test the get defence method of Bulbasaur
            s = b.get_defence()
            if s != 5:
                self.verificationErrors.append(
                    f"get_defence method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_defence method failed. {e}")

    def test_bulbasaur_speed(self):
        from pokemon import Bulbasaur

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check the get speed method of Bulbasaur
            s = b.get_speed()
            if s != 7:
                self.verificationErrors.append(
                    f"get_speed method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_speed method failed. {e}")

    def test_bulbasaur_attacked_damage(self):
        from pokemon import Charmander
        from pokemon import Bulbasaur
        from pokemon import Squirtle

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}."
            )
            return
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}"
            )
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}"
            )
        try:
            # Test Bulbasaur's calculate attacked damage method
            out = b.calculate_attacked_damage(c)
            if out != -5:
                self.verificationErrors.append(
                    f"calculate_attacked_damage method did not return correct hp: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"calculate_attacked_damage method failed. {e}"
            )
        try:
            b = Bulbasaur()
            out = b.calculate_attacked_damage(s)
            if out != 8:
                self.verificationErrors.append(
                    f"calculated_attacked_damage did not return correct hp: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"calculate_attacked_damage method failed. {e}"
            )

    # Test Squirtle
    def test_squirtle_string(self):
        """
        Check Squirtle Pokemon class
        """
        from pokemon import Squirtle

        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check squirtle string method
            out = str(s)
            if out != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(
                    f"String method did not return correct string: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_squirtle_name(self):
        from pokemon import Squirtle

        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check get name method of Squirtle
            out = s.get_name()
            if out != "Squirtle":
                self.verificationErrors.append(
                    f"get_name method did not return correctly: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_name method failed. {e}")

    def test_squirtle_attack(self):
        from pokemon import Squirtle

        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check get attack method of Squirtle
            out = s.get_attack()
            if out != 4:
                self.verificationErrors.append(
                    f"get_attack method did not return correct string: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_attack method failed. {e}")

    def test_squirtle_defence(self):
        from pokemon import Squirtle

        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check get defence method of Squirtle
            out = s.get_defence()
            if out != 7:
                self.verificationErrors.append(
                    f"get_defence method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_defence method failed. {e}")

    def test_squirtle_speed(self):
        from pokemon import Squirtle

        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}."
            )
            return
        try:
            # Check get speed method of Squirtle
            out = s.get_speed()
            if out != 7:
                self.verificationErrors.append(
                    f"get_speed method did not return correct string: {s}"
                )
        except Exception as e:
            self.verificationErrors.append(f"get_speed method failed. {e}")

    def test_squirtle_attacked_damage(self):
        from pokemon import Charmander
        from pokemon import Bulbasaur
        from pokemon import Squirtle

        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(
                f"Squirtle could not be instantiated: {str(e)}."
            )
            return
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(
                f"Charmander could not be instantiated: {str(e)}"
            )
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(
                f"Bulbasaur could not be instantiated: {str(e)}"
            )
        try:
            # Test calculate attacked damage method for Squirtle
            out = s.calculate_attacked_damage(c)
            if out != 7:
                self.verificationErrors.append(
                    f"calculate_attacked_damage method did not return correct hp: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"calculate_attacked_damage method failed. {e}"
            )
        try:
            s = Squirtle()
            out = s.calculate_attacked_damage(c)
            if out != 7:
                self.verificationErrors.append(
                    f"calculate_attacked_damage method did not return correct hp: {out}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"calculate_attacked_damage method failed. {e}"
            )

    def test_MissingNo(self):
        """
        tester for MissingNo.
        """
        from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo

        m1 = MissingNo()  # creating MissingNo pokemon
        # testing MissingNo's name getter
        try:
            name = MissingNo.get_name(m1)
            if name != "MissingNo":
                self.verificationErrors.append(
                    f"MissingNo's name getter returns wrong name str: {name}"
                )
        except Exception as e:
            self.verificationErrors.append(f"MissingNo's name getter failed: {str(e)}.")

        # testing MissingNo's speed getter
        try:
            speed = MissingNo.get_speed(m1)
            if speed != 7:
                self.verificationErrors.append(
                    f"MissingNo's speed getter returns wrong speed: {speed}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's speed getter failed: {str(e)}."
            )

        # testing MissingNo's speed setter
        try:
            m1.set_speed(10)
            if m1.get_speed() != 10:
                self.verificationErrors.append(
                    f"MissingNo's speed setter (10) did not set correctly: {MissingNo.get_speed(m1)}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's speed setter failed: {str(e)}."
            )

        # testing MissingNo's attack getter
        try:
            attack = MissingNo.get_attack(m1)
            if attack != 5:
                self.verificationErrors.append(
                    f"MissingNo's attack getter returns wrong attack: {attack}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's attack getter failed: {str(e)}."
            )

        # testing MissingNo's attack setter
        try:
            MissingNo.set_attack(m1, 10)
            if MissingNo.get_attack(m1) != 10:
                self.verificationErrors.append(
                    f"MissingNo's attack setter (10) did not set correctly: {MissingNo.get_attack(m1)}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's attack setter failed: {str(e)}."
            )

        # testing MissingNo's type getter
        try:
            poke_type = MissingNo.get_poke_type(m1)
            if poke_type is not "None":
                self.verificationErrors.append(
                    f"MissingNo's type getter returns wrong type: {poke_type}"
                )
        except Exception as e:
            self.verificationErrors.append(f"MissingNo's type getter failed: {str(e)}.")

        m2 = MissingNo()
        # testing MissingNo's level up method.
        # The stats will scale when level up
        try:
            MissingNo.level_up(m2)
            if MissingNo.get_level(m2) != 2:
                self.verificationErrors.append(
                    f"MissingNo's up level did not increase "
                    f"level properly: {MissingNo.get_level(m2)}"
                )
            if MissingNo.get_speed(m2) != 8:
                self.verificationErrors.append(
                    f"MissingNo's up level did not increase "
                    f"speed by 1: {MissingNo.get_speed(m2)}"
                )
            if MissingNo.get_attack(m2) != 6:
                self.verificationErrors.append(
                    f"MissingNo's up level did not increase "
                    f"attack by 1: {MissingNo.get_attack(m2)}"
                )
            if MissingNo.get_hp(m2) != 9:
                self.verificationErrors.append(
                    f"MissingNo's up level did not increase "
                    f"HP by 1: {MissingNo.get_attack(m2)}"
                )
            if MissingNo.get_defence(m2) != 6:
                self.verificationErrors.append(
                    f"MissingNo's up level did not increase "
                    f"defence by 1: {MissingNo.get_defence(m2)}"
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's up level method failed: {str(e)}."
            )

        # testing MissingNo's calculate damage taken method.
        try:
            charmander1 = Charmander()
            bulbasaur1 = Bulbasaur()
            squirtle1 = Squirtle()
            MissingNo.calculate_attacked_damage(m2, charmander1)
            if MissingNo.get_hp(m2) == 8 and MissingNo.get_level == 1:
                self.verificationErrors.append(
                    f"MissingNo's damage calculation method does not work (via superpower) or "
                    f"decrease HP, or did not increase level (via superpower)."
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's damage calculation method failed: {str(e)}."
            )
        try:
            charmander1 = Charmander()
            bulbasaur1 = Bulbasaur()
            squirtle1 = Squirtle()
            MissingNo.calculate_attacked_damage(m2, bulbasaur1)
            if MissingNo.get_hp(m2) == 8 and MissingNo.get_level == 1:
                self.verificationErrors.append(
                    f"MissingNo's damage calculation method does not work (via superpower) or "
                    f"decrease HP, or did not increase level (via superpower)."
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's damage calculation method failed: {str(e)}."
            )
        try:
            charmander1 = Charmander()
            bulbasaur1 = Bulbasaur()
            squirtle1 = Squirtle()
            MissingNo.calculate_attacked_damage(m2, squirtle1)
            if MissingNo.get_hp(m2) == 8 and MissingNo.get_level == 1:
                self.verificationErrors.append(
                    f"MissingNo's damage calculation method does not work (via superpower) or "
                    f"decrease HP, or did not increase level (via superpower)."
                )
        except Exception as e:
            self.verificationErrors.append(
                f"MissingNo's damage calculation method failed: {str(e)}."
            )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)
