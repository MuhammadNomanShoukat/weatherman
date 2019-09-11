from django.db import models

# ======================================= FileData Model ============================================
class FileData(models.Model):
    # file_name = models.ForeignKey(FileName,on_delete=models.CASCADE,default="")
    file_name = models.CharField(max_length=200,default="")
    max_temp = models.IntegerField(default=0)
    min_temp = models.IntegerField(default=0)
    max_humd = models.IntegerField(default=0)
    min_humd = models.IntegerField(default=0)
    mean_humd = models.IntegerField(default=0)
    # avg_max_temp = models.IntegerField(default=0)
    # avg_min_temp = models.IntegerField(default=0)
    # avg_humd = models.IntegerField(default=0)

    """ this function returning file name """
    def __str__(self):
        return r"File name is :{0}".format(self.file_name)
