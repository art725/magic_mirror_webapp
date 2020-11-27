from flask import Flask, render_template, request, redirect
import mariadb

app = Flask(__name__)

conn = mariadb.connect(
    user="paul",
    password="lubu",
    host="localhost",
    database="familydb"
)

# default endpoint for web application
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':

        #fetch data from webpage
        form_details = request.form
        name = form_details['name']
        weight = form_details['weight']
        date = form_details['date']
        
        #need a routine to check quality of input, for example, make sure a date is entered
        #also need to change the case of data to ensure it's consistent
        #establish database connection
        cur = conn.cursor()

        # sql commands
        add_detail = ("INSERT INTO weight "
                        "(name, weight, date) "
                        "VALUES (%s, %s, %s)")

        detail_data = (name, weight, date)

        cur.execute(add_detail, detail_data)
        conn.commit()
        cur.close()

        #return 'data entered'
        return redirect('/display')
    return render_template('weight_entry.html')

# display table on a webpage
@app.route('/display')
def weighttable():
    cur = conn.cursor()
    query = "SELECT * FROM weight"
    cur.execute(query)
    db = cur.fetchall()
    return render_template('display.html',db=db)

@app.route('/chores')
def chores():
    cur = conn.cursor()

@app.route('/')
def index():
    df = pd.read_sql_query(
    '''select * from pi_stats''', conn)

    legend = 'Monthly Data'
    labels = df['date_time']
    values = df['cpu_temp_degf']
    return render_template('index.html', values=values, labels=labels, legend=legend)

if __name__ == '__main__':
    app.run(debug=True)