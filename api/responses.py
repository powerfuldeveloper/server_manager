from rest_framework.response import Response


class OkResponse(Response):
    def __init__(self, *args, **kwargs):
        if kwargs.get('data'):
            data = kwargs.get('data')
            data['ok'] = True
        else:
            data = {
                "ok": True
            }
        kwargs['data'] = data
        super().__init__(*args, **kwargs)


class NotOkResponse(Response):
    def __init__(self, *args, **kwargs):
        if kwargs.get('data'):
            data = kwargs.get('data')
            data['ok'] = False
        else:
            data = {
                "ok": False
            }
        kwargs['data'] = data
        super().__init__(*args, **kwargs)
