from rest_framework import generics, permissions
import django_filters
from django_filters.rest_framework import FilterSet, CharFilter

from experiments.models import ProbeInsertion, TrajectoryEstimate
from experiments.serializers import (ProbeInsertionSerializer, TrajectoryEstimateSerializer,)

"""
Probe insertion objects REST filters and views
"""


class ProbeInsertionFilter(FilterSet):
    subject = django_filters.CharFilter('session__subject__nickname')
    date = django_filters.CharFilter('session__start_time__date')
    experiment_number = django_filters.CharFilter('session__number')
    name = django_filters.CharFilter('name')
    session = django_filters.UUIDFilter('session')

    class Meta:
        model = ProbeInsertion
        exclude = ['json']


class ProbeInsertionList(generics.ListCreateAPIView):
    queryset = ProbeInsertion.objects.all()
    serializer_class = ProbeInsertionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = ProbeInsertionFilter


class ProbeInsertionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProbeInsertion.objects.all()
    serializer_class = ProbeInsertionSerializer
    permission_classes = (permissions.IsAuthenticated,)


"""
Trajectory Estimates objects REST filters and views
"""


class TrajectoryEstimateFilter(FilterSet):
    provenance = CharFilter(method='provenance_filter')

    class Meta:
        model = TrajectoryEstimate
        exclude = ['json']

    def provenance_filter(self, queryset, name, value):
        choices = TrajectoryEstimate._meta.get_field('provenance').choices
        # create a dictionary string -> integer
        value_map = {v.lower(): k for k, v in choices}
        # get the integer value for the input string
        try:
            value = value_map[value.lower().strip()]
        except KeyError:
            raise ValueError("Invalid provenance, choices are: " +
                             ', '.join([ch[1] for ch in choices]))
        return queryset.filter(provenance=value)


class TrajectoryEstimateList(generics.ListCreateAPIView):
    queryset = TrajectoryEstimate.objects.all()
    serializer_class = TrajectoryEstimateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = TrajectoryEstimateFilter


class TrajectoryEstimateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrajectoryEstimate.objects.all()
    serializer_class = TrajectoryEstimateSerializer
    permission_classes = (permissions.IsAuthenticated,)
