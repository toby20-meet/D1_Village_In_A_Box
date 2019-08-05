def urlforify(string):
	return "{{url_for('static',filename='"+string+"')}}"

print(urlforify("simple-line-icons/css/simple-line-icons.css"))