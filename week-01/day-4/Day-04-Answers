###### Reversed admin
print(re.search(r'[aA]dmin','Zdmin'))

###### Numbers below 100
print(re.search(r'^(100|[1-9]?[0-9])$','101'))

###### Hungarian mobile numbers
print(re.search(r'^(\+36|00 36) [0-9]{2} [0-9]{3} [0-9]{4}$',
                '+36 20 3173 4717'))
				
###### GFA email address
m = re.match(r'(.*?)@greenfox\.?academy(\.com)?','John.doe@greenfoxacademy.com')
print(m.group(1))

###### Mobile numbers
print(re.search(r'^(\+|00\s?)(\d{1,3}\s){1,3}\d{6,14}',
                '+86 13587456340'))
				
###### Image source
m = re.search(r'\ssrc="((?s).*)">$',
                '<img src="./images/cat-01.png">')
print(m.group(1))

