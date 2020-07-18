from powerfuldeveloper_psutils.docker.docker_processor import DockerMixin
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.responses import OkResponse, NotOkResponse


class DockerViewSet(DockerMixin, viewsets.ViewSet):

    @action(methods=['post'], detail=False)
    def image_list(self, request):

        image_list = self.docker.images(
            show_all=request.data.get('show_all') == '1'
        )

        return Response(data=image_list)

    @action(methods=['post'], detail=False)
    def container_list(self, request):

        image_list = self.docker.ps(
            show_all=request.data.get('show_all') == 1
        )

        return Response(data=image_list)

    def _docker_actions(self, request, start=False, stop=False, kill=False):
        container = request.data.get('container')

        try:

            if start:
                container = self.docker.start(container)
            elif stop:
                container = self.docker.stop(container)
            elif kill:
                container = self.docker.kill(container)

            result_id = container.communicate()[0].decode('utf-8').strip()

            return OkResponse(data={
                "id": result_id
            })
        except:
            pass

        return NotOkResponse()

    @action(methods=['put'], detail=False)
    def start(self, request):
        return self._docker_actions(request, start=True)

    @action(methods=['put'], detail=False)
    def stop(self, request):
        return self._docker_actions(request, stop=False)

    @action(methods=['put'], detail=False)
    def kill(self, request):
        return self._docker_actions(request, kill=False)
