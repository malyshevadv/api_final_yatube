from rest_framework import mixins, viewsets

class CreateRetrieveViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):

    pass
