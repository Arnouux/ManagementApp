from django.db import models
import json

class Tool(models.Model):
    name = models.CharField(max_length=50)

    def getDates(self):
        return self.dates.start_date,self.dates.end_date

    def __str__(self):
        if self.dates.exists() :
            ret = str(self.name) + " ("
            for d in self.dates.all():
                ret += str(d) + ', '
            return ret[:-2] + ')'
        else :
            return str(self.name) + " (Aucune réservation)"

    def __repr__(self):
        if Reservation.objects.get(tool=self) is not None :
            return str(self.name) + "(" + str(self.dates) + ")"
        else :
            return str(self.name) + "(Aucune réservation)"

class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    by_who = models.CharField(max_length=20)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="dates")

    def __str__(self):
        return "{}/{}/{}-{}/{}/{}".format(self.start_date.day,
                                            self.start_date.month,
                                            self.start_date.year,
                                            self.end_date.day,
                                            self.end_date.month,
                                            self.end_date.year,
                                            )
