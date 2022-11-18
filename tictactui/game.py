class Game:
    def getValue(self,player : str) -> int:
        raise NotImplementedError()
    def getTurn(self) -> str:
        raise NotImplementedError()
    def getWinner(self) -> str:
        raise NotImplementedError()
    def getMoves(self) -> list:
        raise NotImplementedError()
    def applyMove(self, move: str):
        raise NotImplementedError()
