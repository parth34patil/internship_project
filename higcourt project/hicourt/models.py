from django.db import models

# Defines the Item model, which represents a case in a court.
class Item(models.Model):
    # The name of the case or party involved.
    name = models.CharField(max_length=100)
    
    # A unique identifier for the case, stored as a large number.
    case_number = models.DecimalField(max_digits=20, decimal_places=0)
    
    # The date associated with the case (e.g., filing date).
    date = models.DateField()
    
    # The current status of the case (e.g., 'pending', 'closed').
    case_status = models.CharField(max_length=100)
    
    # The name of the court where the case is being heard.
    court_name = models.CharField(max_length=100)
    
    # The names of the judges assigned to the case.
    judges = models.CharField(max_length=100)
    
    # A string field to store one or more hearing dates.
    # Consider using a separate model or a `models.TextField()` if the data
    # becomes long or requires structured storage.
    hearing_dates = models.CharField(max_length=100)
    
    # The city where the court is located.
    city = models.CharField(max_length=100)
    
    # The __str__ method provides a human-readable representation of the object.
    # Here, it returns the name of the item.
    def __str__(self):
        return self.name