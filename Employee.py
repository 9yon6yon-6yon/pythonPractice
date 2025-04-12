class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def accessMeetingRoom(self):
        print('Access to meeting room')

    def accessKitchen(self):
        print('Access to kitchen room')


class manager(employee):

    def __init__(self, businessNumber, *args, **kwargs):
        self.businessNumber = businessNumber
        super().__init__(*args, **kwargs)

    def accessPrivateMeetingRoom(self):
        print('Access to private meeting room')


employee1 = manager(55554, 'John doe', 43)
employee1.accessPrivateMeetingRoom()


employee12 = employee('Joe', 12)
employee12.accessMeetingRoom()
