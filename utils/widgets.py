from django.contrib.gis import forms as gisforms
from django.forms.widgets import SelectMultiple

from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class PointWidget(gisforms.OSMWidget):
    template_name = 'utils/custom-openlayers.html'
    default_lat = -30.056548
    default_lon = -51.1827426
    zoom = 12
    scale_text = False
    mouse_position = False

    def __init__(self, attrs=None):
        if attrs:
            attrs.update(self.local_attrs)
        else:
            attrs = self.local_attrs
        super(PointWidget, self).__init__(attrs)

    @property
    def local_attrs(self):
        return {
            'zoom': self.zoom,
            'scale_text': self.scale_text,
            'mouse_position': self.mouse_position,
        }


class ServicesMultipleWidget(SelectMultiple):
    def __init__(self, *args, **kwargs):
        super(ServicesMultipleWidget, self).__init__(*args, **kwargs)
        self.services = {}

    def build_services_duration(self, employee, services):
        for service in services:
            try:
                duration = employee.employeeservice_employee.get(
                    service=service, is_active=True).duration_value
            except:
                duration = service.duration
            self.services[str(service.pk)] = duration

    def render_option(self, selected_choices, option_value, option_label):
        duration = self.services.get(str(option_value), None)
        duration_html = mark_safe(' data-duration="{0}" '.format(duration))

        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html(
            '<option value="{0}"{1}{2}>{3}</option>',
            option_value,
            selected_html,
            duration_html,
            force_text(option_label)
        )
