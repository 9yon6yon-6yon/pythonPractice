class motor:
    def __init__(self, startButton, stopButton, changeDir, changeSpeed):
        self._startButton = startButton
        self._stopButton = stopButton
        self._changeDir = changeDir
        self._changeSpeed = changeSpeed

    def turnOn(self):
        if self._stopButton == 1:
            self._startButton = 0
        self._startButton = True
        print('Motor is turned on')

    def turnOff(self):
        if self._startButton == 1:
            self._stopButton = 0
        self._stopButton = True
        print('Motor is turned off')

    def changeSpeed(self, value):
        self._changeSpeed = value
        print('Speed changed')

    def changeRotationDirection(self,value):
        self._changeDir = value
        print('Direction changed')


fan = motor(0,0,0,0)
fan.turnOn()
fan.changeSpeed(50)
fan.changeRotationDirection(1)
