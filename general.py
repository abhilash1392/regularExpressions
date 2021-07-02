import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

cat
bat
tat
pat

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

abhilash1392@gmail.com

321-555-4321
123.555.1234
123*555*1234
800-555-4321
900.555.1234



Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''
# sentence = 'Start Start a sentence and then bring it to an end the'

pattern = re.compile(r'')

matches = pattern.finditer(urls)
sub_urls = pattern.sub(r'\2.\3',urls)

print(sub_urls)
