class Solve:
    def __init__(self, days):
        self.arr = []
        self.days = days

    def list_of_way(self):
        arr = []
        self.find(self.days, "", arr)
        return arr

    def find(self, days, attendance_pattern, arr):
        if days == 0:
            arr.append(attendance_pattern)
        else:
            # At any given day there are only two possibalities
            self.find(days - 1, attendance_pattern + 'A', arr)  # absent in class
            self.find(days - 1, attendance_pattern + 'P', arr)  # present in class

obj = Solve(5)
way = obj.list_of_way()
total_missing_way = len(list(filter(lambda x: 'AAAA' in x, way)))
total_attend_way = len(way) - total_missing_way
print( total_missing_way, total_attend_wa
