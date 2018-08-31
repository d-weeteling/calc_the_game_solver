import sys

class Game:

    def __init__(self, value_start, value_wanted, rounds_total, ops):
        """
        A Game instance must consist of the following entities:

        DATA:

        - value_start    :: constant - int
        - value_current  :: var - int
        - value_wanted   :: constant - int

        - rounds_total   :: constant - int
        - rounds_current :: var - int

        - ops            :: constant - a dict of transition functions

        METHODS:

        - transition(fn) :: function - apply one of the transition functions
        - has_won()      :: function - check if user has won
        - has_lost()     :: function - check if user has lost
        """

        self.value_start    = value_start
        self.value_current  = value_start
        self.value_wanted   = value_wanted

        self.rounds_total   = rounds_total
        self.rounds_current = 0

        self.ops            = ops


    def transition(self, fnName):
        """
        We update self.current_value by applying the passed-in function to it:
        """
        fn = self.ops[fnName]
        self.value_current = fn(self.value_current)
        self.rounds_current += 1


    def has_won(self):
        return not self.has_lost() and self.value_current == self.value_wanted


    def has_lost(self):
        return self.rounds_current > self.rounds_total


    def get_phase(self):
        if self.has_won():
            return "WON"
        elif self.has_lost():
            return "LOST"
        else:
            return "PENDING"


    def __str__(self):
        result  = "+-----------------------------\n"
        result += "| round nr.......: %i/%i\n" % \
            (self.rounds_current, self.rounds_total)
        result += "| value_current..: %i\n" % self.value_current
        result += "| value_wanted...: %i\n" % self.value_wanted
        result += "| operations.....: %s\n" % ", ".join(self.ops.keys())
        result += "| phase..........: %s\n" % self.get_phase()
        result += "+-----------------------------\n\n"
        return result


class Solver:

    def __init__(self, init_game):
        self.init_game      = init_game
        self.games          = [([], init_game)]
        self.ops            = init_game.ops
        self.value_wanted   = init_game.value_wanted
        self.rounds_total   = init_game.rounds_total
        self.rounds_current = 0
        self.has_won        = False
        self.win_sequence   = None


    def progress(self):
        self.rounds_current += 1
        new_games = []

        for game in self.games:
            for fn_name, fn in self.ops.items():
                new_ops_sequence = game[0][:]
                new_ops_sequence.append(fn_name)
                new_value_start = fn(game[1].value_current)
                new_game = Game(
                    new_value_start,
                    self.value_wanted,
                    self.rounds_total - self.rounds_current,
                    self.ops
                )
                self.has_won = new_game.get_phase() == 'WON'
                if self.has_won:
                    self.win_sequence = new_ops_sequence
                    self.print_solution()
                    sys.exit(0)

                new_games.append((new_ops_sequence, new_game))

        self.games = new_games


    def solve(self):
        while self.rounds_current < self.rounds_total:
            self.progress()

        if not self.has_won:
            print("Did not found solution in %i round(s)! Exiting..." % \
                self.rounds_current)
            sys.exit(1)


    def print_solution(self):
        val = self.init_game.value_start
        for i, op_name in enumerate(self.win_sequence):
            move = i + 1
            old_val = val
            val = self.ops[op_name](val)
            print("round %i) %i \t=> %s \t=> %i" % \
                (move, old_val, op_name, val))
        print()


    def __str__(self):
        result = ""
        for game in self.games:
            prefix  = "+-----------------------------\n"
            prefix += "| %s\n" % ", ".join(game[0])
            game_rep = prefix + str(game[1])
            result += game_rep
        return result


















