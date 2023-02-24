class Stats():
    """Statisitick"""

    def __init__(self):
        """Initiliasation statistick"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Statistick of Game"""
        self.guns_left = 2
        self.score = 0
