from rest_framework.generics import ListAPIView
from apps.task2.models import Vacancy
from apps.task2.api_endpoint.vacancy.vacancy_list.serializers import VacancySerializer


class VacancyList(ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()

        salary = self.request.query_params("salary", None)
        salary_to = self.request.query_params("salary_to", None)
        salary_from = self.request.query_params("salary_from", None)
        print(salary, salary_to, salary_from)

        if not salary:
            if not salary_to:
                if not salary_from:
                    return queryset
                else:
                    return queryset.filter(salary_from_icontains=salary_from)
            else:
                return queryset.filter(salary_to_icontain=salary_to)
        else:
            return queryset.filter(salary_icontains=salary)


__all__ = [
    "VacancyList",
]
