from flask import Flask,render_template,request
from pymongo import MongoClient
import smtplib

app = Flask(__name__)

cluster = MongoClient('mongodb+srv://korrapatichaitanya5:chay@cluster0.x9t9zgx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cluster['goods']
userinfo = db['usersinfo']

server = smtplib.SMTP('smtp.gmail.com',587)
sender_email = 'korrapatichaitanya5@gmail.com'
sender_pass = 'zgrfbllzmlscvcwv'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crops')
def crops():
    return render_template('crops.html')

@app.route('/marketcomparsion')
def marketcomparsion():
    return render_template('marketcomparsion.html')

@app.route('/seasonsprice')
def seasonsprice():
    return render_template('seasonsprice.html')

@app.route('/areas')
def areas():
    return render_template('areas.html')

@app.route('/userinfo')
def usersinfo():
    return render_template('userinfo.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/bookTransport',methods=['post'])
def bookTransport():
    email = request.form['email']
    crop = request.form['crop']
    farmerName = request.form['fname']
    area = request.form['area']
    reason = request.form['reason']
    date = request.form['date']
    usermsg = """Subject: Booking Confirmation \n
    Thanks for using our service. for other information kindly contact this number
    Phone : 8639711683
    """
    ownermsg = """Subject: New Order
    Name : {0} \n
    Email: {1} \n
    Area : {2} \n
    Date : {3} \n
    Reason : {4}\n
    Crop : {5}.

    """.format(farmerName,email,area,date,reason,crop)
    server.starttls()
    server.login(sender_email,sender_pass)
    server.sendmail(sender_email,email,usermsg)
    server.sendmail(sender_email,sender_email,ownermsg)
    server.quit()
    return render_template('index.html')

@app.route('/contact',methods=['post'])
def docontact():
    email = request.form['email']
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    emsg = """Subject: Thanks For connecting \n
    Hello {0}, Thanks for showing interest towards to our services.
    we are thrilled  know that you are interested to collaborate with us.
    let's take a path with us and continue your journey with us.
    """.format(name)
    ownermsg = """Subject: New contact connection\n
    Name : {1} \n
    Email : {0} \n
    Phone : {2} \n
    Message : {3}.
    """.format(email,name,phone,message)
    userinfo.insert_one({'name':name,'email':email,"phone":phone,"message":message})
    server.starttls()
    server.login(sender_email,sender_pass)
    server.sendmail(sender_email,email,emsg)
    server.sendmail(sender_email,sender_email,ownermsg)
    server.quit()
    return render_template('contact.html',ack='Mail sent')

@app.route('/ap')
def ap():
    return render_template('ap.html')
@app.route('/ap_anantapur')
def ap_anantapur():
    return render_template('ap_anantapur.html')
@app.route('/ap_chittoor')
def ap_chittor():
    return render_template('ap_chittoor.html')
@app.route('/ap_eastgodavari')
def ap_eastgodavari():
    return render_template('ap_eastgodavari.html')
@app.route('/ap_guntur')
def ap_guntur():
    return render_template('ap_guntur.html')
@app.route('/ap_kadapa')
def ap_kadapa():
    return render_template('ap_kadapa.html')
@app.route('/ap_krishna')
def ap_krishna():
    return render_template('ap_krishna.html')
@app.route('/ap_kurnool')
def ap_kurnool():
    return render_template('ap_kurnool.html')
@app.route('/ap_nellore')
def ap_nellore():
    return render_template('ap_nellore.html')
@app.route('/ap_parakasam')
def ap_parakasam():
    return render_template('ap_parakasam.html')
@app.route('/ap_srikakulam')
def ap_srikakulam():
    return render_template('ap_srikakulam.html')
@app.route('/ap_westgodavari')
def ap_westgodavari():
    return render_template('ap_westgodavari.html')

@app.route('/assam')
def assam():
    return render_template('assam.html')



@app.route('/arunachal')
def arunachal():
    return render_template('arunachal.html')



@app.route('/gujarat')
def gujarath():
    return render_template('gujarat.html')



@app.route('/karnataka')
def karnataka():
    return render_template('karnataka.html')

@app.route('/kerala')
def kerala():
    return render_template('kerala.html')

@app.route('/telangana')
def telnagana():
    return render_template('telangana.html')

@app.route('/madhy_pradesh')
def madhya_pradesh():
    return render_template('madhy_pradesh.html')

@app.route('/uttar_pradesh')
def uttar_pradesh():
    return render_template('uttar_pradesh.html')

@app.route('/maharashtra')
def maharashtra():
    return render_template('maharashtra.html')

@app.route('/tamil_nadu')
def tamil_nadu():
    return render_template('tamil_nadu.html')

@app.route('/meghalaya')
def meghalaya():
    return render_template('meghalaya.html')
@app.route('/west_bengal')
def west_bengal():
    return render_template('west_bengal.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
