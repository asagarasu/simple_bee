from django.db import models

class Bee_robot(models.Model):    
    nectar = models.IntegerField(default=0)
    honey = models.IntegerField(default=0)
    fuel = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    speed = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    longitude  = models.FloatField(default=0.0)
    elevation = models.FloatField(default=0.0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        gps = "GPS(" + str(self.latitude) + "," + str(self.longitude) + "," + str(self.elevation) + ")"
        return gps + " v(" + str(self.isActive) + ")"

    def was_destructed(self):
        return self.damage >= 100

    def as_json(self):
        return dict(
            id=self.id, 
            nectar=self.nectar, 
            honey=self.honey,
            fuel=self.fuel, 
            damage=self.damage,
            status=self.status,
            speed=self.speed,
            latitude=self.latitude,
            longitude=self.longitude,
            elevation=self.elevation,
            is_active=self.is_active,
            )