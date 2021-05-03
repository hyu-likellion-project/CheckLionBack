from django import forms
from datetime import datetime, timedelta


start_time = datetime(2021, 3, 25, 0, 0, 0)
WEEK_NUM = int( (datetime.now() - start_time).days ) // 7 + 3

class InfoForm(forms.Form):
    YES_OR_NO = (
        ('Y','YES'),
        ('N','NO')
    )
    week = forms.IntegerField(
        error_messages = {'required':'주차를 입력하세요.'},
        label = '주차',
        initial=WEEK_NUM
    )
    name = forms.CharField(
        error_messages = {'required':'이름을 입력하세요.'},
        max_length=128, label = '이름'
    )
    team = forms.CharField(
        error_messages = {'required':'팀 이름을 입력하세요.'},
        max_length=128, label = '팀 이름'
    )
    lec_check = forms.TypedChoiceField(choices = YES_OR_NO, empty_value='Y', label = '강의체크')
    att_check = forms.TypedChoiceField(choices = YES_OR_NO, empty_value='Y', label = '출석체크')
    ass_check = forms.TypedChoiceField(choices = YES_OR_NO, empty_value='Y', label = '과제체크')