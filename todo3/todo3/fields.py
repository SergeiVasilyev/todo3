from django import forms


# https://overcoder.net/q/42663/форма-django-с-возможностью-выбора-но-также-с-возможностью-свободного-текста
class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})
        self.attrs.update({'class':'form-control mb-2', 'placeholder':'enter category'}) # Добавил класс в Input, так как в forms виджеты не работают

    def render(self, name, value, attrs=None, renderer=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        print('self._name', self._name)
        try:
            for item in self._list:
                data_list += '<option value="%s">' % item
        except:
            data_list += '<option value="%s">' % self._list
        data_list += '</datalist>'

        return (text_html + data_list)