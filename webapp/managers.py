from django.db.models import Manager, QuerySet, Avg


class ReviewManager(Manager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db).all()

    def get_average(self):
        return self.get_queryset().aggregate(Avg('rate')).get('rate__avg')
