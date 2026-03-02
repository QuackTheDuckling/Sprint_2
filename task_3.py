class PointsForPlace:
    def get_points_for_place(self, place):
        self.place = place
        if self.place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif self.place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            points = 101 - self.place
            return points

class PointsForMeters:
    def get_points_for_meters(self, meters):
        self.meters = meters
        if self.meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            points = self.meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 