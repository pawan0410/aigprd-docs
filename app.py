from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import send_from_directory
from extensions import db
from extensions import mail
import config
import datetime
import utils
import os

from models import Employee, Manager



app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/success")
def success():
    return render_template('thankyou.html')


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(utils.UPLOAD_DIR, filename, as_attachment=True)


@app.route('/employee', methods=['POST'])
def save_employee_form():
    emp_name = request.form.get('emp_name')
    emp_code = request.form.get('emp_code')
    emp_email = request.form.get('emp_email')
    job_function = request.form.get('job_function')
    date = request.form.get('date')
    reviewer_name = request.form.get('reviewer_name')
    reviewer_code = request.form.get('reviewer_code')
    self_assessment1 = request.form.get('self_assessment1')
    self_assessment1_comment1 = request.form.get('self_assessment1_comment1')
    self_assessment2 = request.form.get('self_assessment2')
    self_assessment2_comment2 = request.form.get('self_assessment2_comment2')
    self_assessment3 = request.form.get('self_assessment3')
    self_assessment3_comment3 = request.form.get('self_assessment3_comment3')
    self_assessment4 = request.form.get('self_assessment4')
    self_assessment4_comment4 = request.form.get('self_assessment4_comment4')
    self_assessment5 = request.form.get('self_assessment5')
    self_assessment5_comment5 = request.form.get('self_assessment5_comment5')
    self_assessment6 = request.form.get('self_assessment6')
    self_assessment6_comment6 = request.form.get('self_assessment6_comment6')
    rev_email = request.form.get('rev_email')

    employee_form = Employee(
        emp_code=emp_code,
        emp_name=emp_name,
        emp_email=emp_email,
        job_function=job_function,
        date=date,
        reviewer_name=reviewer_name,
        reviewer_code=reviewer_code,
        self_assessment1=self_assessment1,
        self_assessment1_comment1=self_assessment1_comment1,
        self_assessment2=self_assessment2,
        self_assessment2_comment2=self_assessment2_comment2,
        self_assessment3=self_assessment3,
        self_assessment3_comment3=self_assessment3_comment3,
        self_assessment4=self_assessment4,
        self_assessment4_comment4=self_assessment4_comment4,
        self_assessment5=self_assessment5,
        self_assessment5_comment5=self_assessment5_comment5,
        self_assessment6=self_assessment6,
        self_assessment6_comment6=self_assessment6_comment6,
        rev_email=rev_email,
        IP_addr=request.remote_addr,
        Location=request.form.get('location'),
        UserAgent=request.user_agent.browser,
        OperatingSystem=request.user_agent.platform,
        Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    )

    db.session.add(employee_form)
    db.session.commit()

    utils.send_link_as_mail(
        emp_name=emp_name,
        rev_email=rev_email,
        reviewer_code=reviewer_code,
        emp_code=emp_code,

    )
    return redirect('/success')


@app.route("/document/<string:emp_code>/<string:reviewer_code>")
def document(emp_code, reviewer_code):
    the_document = Employee.query.filter(Employee.emp_code == emp_code,
                                         Employee.reviewer_code == reviewer_code)\
        .order_by(Employee.id.desc()).first()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    return render_template('document.html', the_document=the_document, base_dir=BASE_DIR)


@app.route("/manager", methods=['POST'])
def save_managerdata():
    emp_code1 = request.form.get('emp_code1')
    reviewer_name1 = request.form.get('reviewer_name1')
    reviewer_code1 = request.form.get('reviewer_code1')

    manager_assessment1 = request.form.get('manager_assessment1')
    manager_assessment1_comment1 = request.form.get('manager_assessment1_comment1')

    achieved_score1 = request.form.get('achieved_score1')

    manager_assessment2 = request.form.get('manager_assessment2')
    manager_assessment2_comment2 = request.form.get('manager_assessment2_comment2')

    achieved_score2 = request.form.get('achieved_score2')

    manager_assessment3 = request.form.get('manager_assessment3')
    manager_assessment3_comment3 = request.form.get('manager_assessment3_comment3')

    achieved_score3 = request.form.get('achieved_score3')

    manager_assessment4 = request.form.get('manager_assessment4')
    manager_assessment4_comment4 = request.form.get('manager_assessment4_comment4')

    achieved_score4 = request.form.get('achieved_score4')

    manager_assessment5 = request.form.get('manager_assessment5')
    manager_assessment5_comment5 = request.form.get('manager_assessment5_comment5')

    achieved_score5 = request.form.get('achieved_score5')

    manager_assessment6 = request.form.get('manager_assessment6')
    manager_assessment6_comment6 = request.form.get('manager_assessment6_comment6')

    achieved_score6 = request.form.get('achieved_score6')

    total_achieved_score = request.form.get('total_achieved_score')

    manager_final_comment = request.form.get('manager_final_comment')
    manager_final_rating = request.form.get('manager_final_rating')

    rev_email1 = request.form.get('rev_email1')

    signature = utils.save_signature(request.form.get('signature'), 'reviewer_name1', 'signature')

    manager_form = Manager(

        emp_code1=emp_code1,
        reviewer_name1=reviewer_name1,
        reviewer_code1=reviewer_code1,
        manager_assessment1=manager_assessment1,
        manager_assessment1_comment1=manager_assessment1_comment1,

        achieved_score1=achieved_score1,

        manager_assessment2=manager_assessment2,
        manager_assessment2_comment2=manager_assessment2_comment2,

        achieved_score2=achieved_score2,

        manager_assessment3=manager_assessment3,
        manager_assessment3_comment3=manager_assessment3_comment3,

        achieved_score3=achieved_score3,

        manager_assessment4=manager_assessment4,
        manager_assessment4_comment4=manager_assessment4_comment4,

        achieved_score4=achieved_score4,

        manager_assessment5=manager_assessment5,
        manager_assessment5_comment5=manager_assessment5_comment5,

        achieved_score5=achieved_score5,

        manager_assessment6=manager_assessment6,
        manager_assessment6_comment6=manager_assessment6_comment6,

        achieved_score6=achieved_score6,

        total_achieved_score=total_achieved_score,

        manager_final_comment=manager_final_comment,
        manager_final_rating=manager_final_rating,

        signaturepath=signature,

        IP_addr=request.remote_addr,
        Location=request.form.get('location'),
        UserAgent=request.user_agent.browser,
        OperatingSystem=request.user_agent.platform,
        Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    )

    db.session.add(manager_form)
    db.session.commit()
    utils.send_manager_link_as_mail(

        rev_email1=rev_email1,
        reviewer_code1=reviewer_code1,
        emp_code1=emp_code1,

    )
    return redirect('/success')


@app.route("/final_form/<string:emp_code1>/<string:reviewer_code1>")
def final_document(emp_code1, reviewer_code1):
    the_final_document = Manager.query.filter(Manager.emp_code1 == emp_code1,
                                              Manager.reviewer_code1 == reviewer_code1)\
        .order_by(Manager.id.desc()).first()
    the_document = Employee.query.filter(Employee.emp_code == emp_code1,
                                         Employee.reviewer_code == reviewer_code1)\
        .order_by(Employee.id.desc()).first()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    return render_template('finaldocument.html', the_document=the_document, the_final_document=the_final_document,
                           base_dir=BASE_DIR)


@app.route("/save_final", methods=['POST'])
def save_finaldata():
    emp_code = request.form['emp_code1']
    reviewer_code = request.form['reviewer_code1'].strip()
    the_document = Employee.query.\
        filter(Employee.emp_code == emp_code, Employee.reviewer_code == reviewer_code).first()
    emp_code = the_document.emp_code
    reviewer_code = the_document.reviewer_code

    the_document = db.session.execute(
        """SELECT emp_name from employee_form WHERE reviewer_code='{}' """.format(reviewer_code)).first()

    emp_name = the_document[0]
    signature1 = utils.save_signature(request.form.get('signature1'), emp_name, 'signature1')

    db.session.execute("""
                   UPDATE employee_form SET signaturepath1='{}' WHERE emp_code='{}'
                   """.format(signature1, emp_code))
    db.session.commit()

    # db.session.execute("""
    #             UPDATE employee_form SET signaturepath1= signaturepath1 WHERE emp_code= emp_code
    #             """, {'signaturepath1': signature1, 'emp_code': emp_code})
    # db.session.commit()

    the_empdocument = Employee.query.filter(Employee.emp_code == emp_code).order_by("id desc").first()
    the_document = Manager.query.filter(Manager.emp_code1 == emp_code).order_by("id desc").first()

    file_name = utils.save_document_as_docx(
        emp_name=the_empdocument.emp_name,
        emp_code=the_empdocument.emp_code,
        emp_email=the_empdocument.emp_email,
        job_function=the_empdocument.job_function,
        date=the_empdocument.date,
        reviewer_name=the_empdocument.reviewer_name,
        reviewer_code=the_empdocument.reviewer_code,


        self_assessment1_comment1=the_empdocument.self_assessment1_comment1,
        self_assessment1=the_empdocument.self_assessment1,
        manager_assessment1=the_document.manager_assessment1,
        manager_assessment1_comment1=the_document.manager_assessment1_comment1,

        achieved_score1=the_document.achieved_score1,

        self_assessment2_comment2=the_empdocument.self_assessment2_comment2,
        self_assessment2=the_empdocument.self_assessment2,
        manager_assessment2=the_document.manager_assessment2,
        manager_assessment2_comment2=the_document.manager_assessment2_comment2,

        achieved_score2=the_document.achieved_score2,

        self_assessment3_comment3=the_empdocument.self_assessment3_comment3,
        self_assessment3=the_empdocument.self_assessment3,
        manager_assessment3=the_document.manager_assessment3,
        manager_assessment3_comment3=the_document.manager_assessment3_comment3,

        achieved_score3=the_document.achieved_score3,

        self_assessment4_comment4=the_empdocument.self_assessment4_comment4,
        self_assessment4=the_empdocument.self_assessment4,
        manager_assessment4=the_document.manager_assessment4,
        manager_assessment4_comment4=the_document.manager_assessment4_comment4,

        achieved_score4=the_document.achieved_score4,

        self_assessment5_comment5=the_empdocument.self_assessment5_comment5,
        self_assessment5=the_empdocument.self_assessment5,
        manager_assessment5=the_document.manager_assessment5,
        manager_assessment5_comment5=the_document.manager_assessment5_comment5,

        achieved_score5=the_document.achieved_score5,

        self_assessment6_comment6=the_empdocument.self_assessment6_comment6,
        self_assessment6=the_empdocument.self_assessment6,
        manager_assessment6=the_document.manager_assessment6,
        manager_assessment6_comment6=the_document.manager_assessment6_comment6,

        achieved_score6=the_document.achieved_score6,

        total_achieved_score=the_document.total_achieved_score,

        manager_final_comment=the_document.manager_final_comment,
        manager_final_rating=the_document.manager_final_rating,


        signature1=the_empdocument.signaturepath1,
        signature=the_document.signaturepath,

    )
    utils.send_document_as_mail(emp_name=the_empdocument.emp_name, file_name=file_name)
    return redirect('/success')
