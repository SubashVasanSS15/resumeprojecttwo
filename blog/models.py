from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
     
    # to know and display the names of the blogs in the admin page used to do modifications easily
    def __str__(self):
        return self.title 

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')