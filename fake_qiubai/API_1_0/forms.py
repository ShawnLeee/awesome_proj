# encoding: utf-8
from django import forms
from captcha.fields import CaptchaField


class VoteForm(forms.Form):
    involved_type = forms.IntegerField(required=False)
    involved_post_id = forms.IntegerField(required=False)
    involved_reply_id = forms.IntegerField(required=False)
    involved_user_id = forms.IntegerField(required=False)
    status = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super(VoteForm, self).clean()

        status = cleaned_data.get('status')
        involved_type = cleaned_data.get('involved_type')
        involved_post_id = cleaned_data.get('involved_post_id')
        involved_reply_id = cleaned_data.get('involved_reply_id')
        involved_user_id = cleaned_data.get('involved_user_id')

        if status is None:
            raise forms.ValidationError("Missing parameter status.")
        if involved_user_id is None:
            raise forms.ValidationError("Missing parameter involved_user_id.")
        if involved_type is None:
            raise forms.ValidationError("Missing parameter involved_type.")

        if status != 1 and status != 0:
            raise forms.ValidationError("status value should be 1(vote) or 0(downvote).")

        if involved_type != 1 and involved_type != 2:
            raise forms.ValidationError("involved_type should be 1(for post) or 2(for reply).")

        if involved_type == 1 and involved_post_id is None:
            raise forms.ValidationError("Missing parameter involved_post_id.")

        if involved_type == 2 and involved_reply_id is None:
            raise forms.ValidationError("Missing parameter involved_reply_id.")

        return cleaned_data








