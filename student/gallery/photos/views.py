from django.views.generic import TemplateView

# Create your views here.
class PhotoView(TemplateView):
    template_name='photo.html'

    def get_context_data(self, **kwargs):
        name=kwargs['name']
        image= f'static/images/{name}'
        return {'photo':image}
    