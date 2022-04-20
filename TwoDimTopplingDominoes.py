from misc import mex


class TwoDimTopplingDominoes:

    def __init__(self, moves):
        self.moves = moves
        self._value = None
        self.find_connected_components()

    def find_connected_components(self):
        self.components = []
        moves = self.moves.copy()
        current_component = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            current_component.append(move)
            for move in current_component:
                for direction in directions:
                    neighbor = (move[0] + direction[0], move[1] + direction[1])
                    if neighbor in self.moves and not neighbor in current_component:
                        current_component.append(neighbor)
                        if neighbor in moves:
                            moves.remove(neighbor)
            self.components.append(current_component.copy())
            current_component = []

    def move(self, move, direction):
        if move not in self.moves:
            raise ValueError
        if self._value:
            return self._value
        else:
            moves = self.moves.copy()
            while move in moves:
                moves.remove(move)
                move = (move[0] + direction[0], move[1] + direction[1])
            ans = TwoDimTopplingDominoes(moves)
            ans.get_value()
        return ans

    def get_value(self) -> int:
        if self._value:
            return self._value

        else:
            if len(self.components) > 1:
                value = 0
                for component in self.components:
                    subgame = TwoDimTopplingDominoes(component)
                    value = value ^ subgame.get_value()
            else:
                if len(self.moves) == 0:
                    return 0
                else:
                    subgames = []
                    for move in self.moves:
                        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            subgame = self.move(move, direction)
                            subgames.append(subgame.get_value())
                    self._value = mex(subgames)
        return self._value

    @classmethod
    def generateRect(cls, dim):
        moves = []
        for i in range(dim[0]):
            for j in range(dim[1]):
                moves.append((i, j))
        return TwoDimTopplingDominoes(moves)

    @classmethod
    def generateL(cls, up, right):
        moves = []
        for i in range(up):
            moves.append((0, i))
        for j in range(right):
            moves.append((j + 1, 0))
        return TwoDimTopplingDominoes(moves)


if __name__ == "__main__":
    x = TwoDimTopplingDominoes([(0, 0), (0, 1), (2, 0), (2, 1)])
    print(x.components)
