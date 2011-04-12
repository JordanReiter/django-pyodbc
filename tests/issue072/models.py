
from django.db import models

class SampleRecord(models.Model):
    name = models.CharField(max_length=50)
    expo = models.TextField()
    start = models.DateTimeField()
    counter = models.PositiveIntegerField()
    
    
__test__ = {'API_TESTS': """
>>> from datetime import datetime

>>> SampleRecord.objects.create(name="Test1", expo="Could be very long, this ain't.", start=datetime.datetime(2011, 4, 12), counter=1)
>>> SampleRecord.objects.create(name="Test2", expo="Could be very long, this isn't.", start=datetime.datetime.now(2011, 5, 12), counter=2)
>>> SampleRecord.objects.create(name="Test3", expo="Could be very long, this is not.", start=datetime.datetime.now(2011, 6, 12), counter=3)
>>> records = SampleRecord.objects.all()
>>> records.count()
3
>>> len(list(records))
3
>>> matches = SampleRecord.objects.filter(expo__icontains="ain't")
>>> matches.count()
1
>>> len(list(matches))
1


"""}
