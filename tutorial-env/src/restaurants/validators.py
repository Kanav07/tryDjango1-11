from django.core.exceptions import ValidationError

# def clean_email(value):
# 	if ".edu" in value:
# 		raise ValidationError("Not a valid email")


CATEGORIES = [	'Indian', 
				'American', 
				'Hyderabadi', 
				'Italian', 
				'Cafe',
				'Mughlai',
				'South-Indian',
				'North-Indian',
				'Fusion',
				'Continental',
				'European',
				'Fast Food',
				'Punjabi',
				'Rajasthani']

def validate_category(value):
	if not value in CATEGORIES:
		raise ValidationError(f"{value} not is CATEGORIES")