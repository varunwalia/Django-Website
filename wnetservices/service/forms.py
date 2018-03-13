from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit , Layout , Button,Fieldset,ButtonHolder ,HTML , MultiField,Div,Reset,Field
from crispy_forms.bootstrap import (
									StrictButton ,
									 FormActions,
									 AppendedText,
									 PrependedText,
									 PrependedAppendedText,
									 FieldWithButtons,)

from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Name')
	contact = forms.IntegerField(label='Contact no.')
	email = forms.EmailField(label='Email')
	query = forms.CharField(max_length = 200)
	choice = forms.TypedChoiceField(
        label = "Type of Requirement?",
        choices = ((1, "WebDesign & Development"), (0, "Ecommerce Solution") ,(3,'SEO'), (4,'Mobile App Development'), (5,'Logo Design & Graphic')),
        coerce = lambda x: bool(int(x)),
        widget = forms.CheckboxSelectMultiple,
        initial = '1',
        required = True,
    )


	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		# self.helper = FormHelper()
		# self.helper.form_id = 'id-ContactForm'
		# self.helper.form_class = 'form-inline'
		# # self.helper.label_class=  'col-lg-2'
		# # self.helper.field_class = 'ocl-lg-8'
		# self.helper.form_method = 'POST'
		# self.helper.form_action = 'contact'

		# self.helper.layout = Layout(
		# 	'name' , 
		# 	'contact',
		# 	'email',
		# 	'query',
		# 	FormActions(
		# 				Submit('save', 'Save changes'),
		# 				Button('cancel', 'Cancel')
		# 				)

		# 	)

		self.helper = FormHelper()
		self.helper.form_class=  'form-inline'
		self.helper.layout = Layout(
			Fieldset(
				'ContactForm',

				# AppendedText('name', 'Write YOur Name Here' ,active=True), 
				Field('name', placeholder = 'Enter Name:'),
				Div('choice' , active=True),
				
				Div('contact' , style="background:white;margin:10px ; padding:10px;" , title="Provide Contact" , css_class='form_contact' ),
				'email', 
				        HTML("""
            <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
        """),
				PrependedText('query','Kya poochna Chahte ho? '),
						),
			  FormActions(   #ButtonHolder 
				Submit('submit' , 'Submit' , css_class = 'button white'),
				Reset('clear', "Clear")),
			  	# StrictButton('Go', css_class='btn-success')

			)