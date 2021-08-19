class GestureRecognizer:
    def __init__(self) -> None:
        pass

    def getGestureType(self, finger_position):
        if self.__isOne(finger_position):
            return 3
        elif self.__isFist(finger_position):
            return 0
        elif self.__isRightSide(finger_position):
            return 1
        elif self.__isLeftSide(finger_position):
            return 2

    def __isFist(self, finger_position):
        if (finger_position[13][1] > finger_position[9][1] > finger_position[5][1] or\
            finger_position[13][1] < finger_position[9][1] < finger_position[5][1]) and\
            finger_position[9][2] < finger_position[12][2]:
            return True
        else:
            return False

    def __isRightSide(self, finger_position):
            #中指、大拇指指節x軸需以以下排序，食指第一指節需高於中指第一指節，小拇指第一指節需低於中指第一指節
        if finger_position[12][1] < finger_position[11][1] < finger_position[10][1] < finger_position[9][1] and\
            finger_position[4][1] < finger_position[3][1] < finger_position[2][1] < finger_position[1][1] and\
            finger_position[8][2] < finger_position[12][2] and finger_position[20][2] > finger_position[12][2]:
                return True
        else:
            return False

    def __isLeftSide(self, finger_position):
        if finger_position[12][1] > finger_position[11][1] > finger_position[10][1] > finger_position[9][1] and\
            finger_position[4][1] > finger_position[3][1] > finger_position[2][1] > finger_position[1][1] and\
            finger_position[8][2] < finger_position[12][2] and finger_position[20][2] > finger_position[12][2]:
            return True
        else:
            return False

    def __isOne(self, finger_position):
        if finger_position[8][2] < finger_position[7][2] < finger_position[6][2] < finger_position[5][2] and\
            finger_position[9][2] < finger_position[12][2]:
            return True
        else:
            return False