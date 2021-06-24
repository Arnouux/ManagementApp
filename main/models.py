from django.db import models
import json

class Tool(models.Model):
    name = models.CharField(max_length=50)

    def getDates(self):
        return self.dates.start_date,self.dates.end_date

    def __str__(self):
        if self.dates.exists() :
            if len(self.dates.all()) == 1:
                return str(self.name) + " (1 réservation)"
            elif len(self.dates.all()) > 1:
                return str(self.name) + " (" + str(len(self.dates.all())) +" réservations)"
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
        return "{}-{}".format(self.start_date.strftime("%d/%m/%y"),
                              self.end_date.strftime("%d/%m/%y"))
