from flask_wtf import Form
from wtforms import *
from wtforms import validators
from flask_wtf.file import FileAllowed

class SchoolForm(Form):
    id = HiddenField('id')
    name = StringField('学校名称',validators=[validators.Length(min=1,max=50)])
    area_id = SelectField('所在区县',coerce=int)
    teachdesc = TextAreaField('师资力量')
    address = StringField('address')
    schooltype_id = SelectField('类型',coerce=int)
    website = StringField('web')
    distinguish = TextAreaField('特色')
    leisure = TextAreaField('活动')
    threashold = TextAreaField('条件')
    partner = StringField('对口学校')
    artsource = StringField('情况')
    feedesc = StringField('标准')
    longitude = DecimalField('longitude',place=4)
    latitude = DecimalField('latitude',place=4)
    feature_ids = SelectMultipleField('特色',coerce=int)
    image = FileField('img',validators=[FileAllowed['jpg','png'],'Images only'])
