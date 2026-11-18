class calculator:
    """ Class calculator that has 3 static vector methods
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = (V1[0] * V2[0]) + (V1[1] * V2[1]) + (V1[2] * V2[2])
        print(res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res: list[float] = [x + y for x, y in zip(V1, V2)]
        print(res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res: list[float] = [x - y for x, y in zip(V1, V2)]
        print(res)
