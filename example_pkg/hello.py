from markdown import markdown

class YoDude:
    """
    A class with the hello method.

    :param intro: intro portion
    """

    intro: str=" YoDude " #: The intro for the hello

    def __init__(self, intro: str=None):
        if intro is not None:
            self.intro = intro
        self.intro = self.intro.strip()

    def hello(self, person: str="Nobody") -> None:
        """
        Say hello to person

        :param person: Say hello to the person
        """
        print(markdown(f"{self.intro.strip()} {person.strip()}"))
