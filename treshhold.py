class treshhold():
    def __init__(self, treshold):
        self.timer = 0
        self.treshold = treshold

    def can_be_used(self):
        self.timer -= 1
        if self.timer > 0:
            return False
        self.timer += self.treshold
        return True
