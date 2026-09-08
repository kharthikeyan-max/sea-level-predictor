import unittest
import sea_level_predictor

class SeaLevelTestCase(unittest.TestCase):
def test_plot(self):
    ax = sea_level_predictor.draw_plot()

    self.assertEqual(
        ax.get_xlabel(),
        "Year"
    )

    self.assertEqual(
        ax.get_ylabel(),
        "Sea Level (inches)"
    )

    self.assertEqual(
        ax.get_title(),
        "Rise in Sea Level"
    )


if **name** == "**main**":
unittest.main()
