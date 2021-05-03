from django.db import models

class Infos(models.Model):
    YES_OR_NO = (
        ('Y','YES'),
        ('N','NO')
    )
    week = models.IntegerField(verbose_name = '주차')
    name = models.CharField(max_length = 128, verbose_name = '이름')
    team = models.CharField(max_length = 128, verbose_name = '팀 이름')
    lec_check = models.CharField(
        max_length = 2, verbose_name = '강의체크',
        choices = YES_OR_NO
    )
    att_check = models.CharField(
        max_length = 2, verbose_name = '출석체크',
        choices = YES_OR_NO
    )
    ass_check = models.CharField(
        max_length = 2, verbose_name = '과제체크',
        choices = YES_OR_NO
    )
    register_date = models.DateTimeField(auto_now_add=True, verbose_name = '등록날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = '마지막수정일')

    def __str__(self):
        return f"주차 : {self.week}, 이름 : {self.name}, 팀 이름 : {self.team}"

    class Meta:
        db_table = 'Info_table'
        verbose_name = ''
        verbose_name_plural = '정보들'

class Team(models.Model):
    week = models.IntegerField(verbose_name = '주차')
    first = models.CharField(max_length = 128, verbose_name = '1등 팀')
    second = models.CharField(max_length = 128, verbose_name = '2등 팀')
    third = models.CharField(max_length = 128, verbose_name = '3등 팀')
    
    register_date = models.DateTimeField(auto_now_add=True, verbose_name = '등록날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = '마지막수정일')

    def __str__(self):
        return f"주차 : {self.week}, 1등 : {self.first}, 2등 : {self.second}, 3등 : {self.third}"

    class Meta:
        db_table = 'Team_table'
        verbose_name = ''
        verbose_name_plural = '팀정보들'

