import os

from django.views.generic.base import TemplateResponseMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class AjaxMixin(TemplateResponseMixin):
    template_name_ajax_suffix = '_ajax'

    def get_template_names(self):
        """
        For each filename in the template names, suffix it with _ajax. In
        general, the non-ajax template will include the ajax template for
        non-ajax calls.
        """
        original_template_names = super(AjaxMixin, self).get_template_names()
        if not self.request.is_ajax():
            return original_template_names
        else:
            template_names = []
            for filename in original_template_names[::-1]:
                name, ext = os.path.splitext(filename)
                ajax_filename = ''.join([name, self.template_name_ajax_suffix, ext])
                template_names.insert(0, filename)
                template_names.insert(0, ajax_filename)
            return template_names

    def form_invalid(self, form):
        """
        Changes the status code of the response to 422 (UNPROCESSABLE
        ENTITY). This is used to trigger the error method on jquery.
        """
        return self.render_to_response(
            self.get_context_data(form=form), status=422)
