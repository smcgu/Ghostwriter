from django import forms

from crispy_forms.helper import FormHelper

from .models import Oplog, OplogEntry


class OplogCreateForm(forms.ModelForm):
    """
    Form used with the OplogCreate for creating new oplog entries.
    """

    class Meta:
        model = Oplog
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OplogCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "form-inline"
        self.helper.form_method = "post"
        self.helper.field_class = "h-100 justify-content-center align-items-center"


class OplogCreateEntryForm(forms.ModelForm):
    """
    Form used for creating entries in the oplog
    """

    class Meta:
        model = OplogEntry
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OplogCreateEntryForm, self).__init__(*args, **kwargs)
        # self.oplog_id = pk
        self.helper = FormHelper()
        self.helper.form_class = "form-inline"
        self.helper.form_method = "post"
        self.helper.field_class = "h-100 justify-content-center align-items-center"
