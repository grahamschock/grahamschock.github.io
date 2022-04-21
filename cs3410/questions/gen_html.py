import csv
page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>CS3410</title>
    <style>
      h1 {{text-align: center;
          line-height: 100px;
          height: 100px;
         }}
    </style>
</head>
<body>
  <div id = "question"> <h1> {question} </h1></div>
</body>

</html>
"""
questions = []
with open("1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        for i in row:
            if i != '':
                questions.append(i)
for i in range(len(questions)):
    html_txt = page.format(question = questions[i])
    f = open("question"+str(i+1)+".html", "w")
    f.write(html_txt)
    f.close()

# print(questions)
# print(page.format(question='Test'))
