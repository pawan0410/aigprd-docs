from extensions import db

class Employee(db.Model):
    __tablename__ = 'employee_form'

    id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(255))
    emp_email = db.Column(db.String(255))
    emp_code = db.Column(db.String(255))
    job_function = db.Column(db.String(255))
    date = db.Column(db.Date)
    reviewer_name = db.Column(db.String(255))
    reviewer_code = db.Column(db.String(255))
    self_assessment1=db.Column(db.String(255))
    self_assessment1_comment1 = db.Column(db.String(255))
    self_assessment2 = db.Column(db.String(255))
    self_assessment2_comment2 = db.Column(db.String(255))
    self_assessment3 = db.Column(db.String(255))
    self_assessment3_comment3 = db.Column(db.String(255))
    self_assessment4 = db.Column(db.String(255))
    self_assessment4_comment4 = db.Column(db.String(255))
    self_assessment5 = db.Column(db.String(255))
    self_assessment5_comment5 = db.Column(db.String(255))
    self_assessment6 = db.Column(db.String(255))
    self_assessment6_comment6 = db.Column(db.String(255))
    rev_email = db.Column(db.String(255))
    signaturepath1 = db.Column(db.String(255))
    IP_addr = db.Column(db.String(255))
    Location = db.Column(db.String(255))
    UserAgent = db.Column(db.String(255))
    OperatingSystem = db.Column(db.String(255))
    Time = db.Column(db.DateTime)


class Manager(db.Model):
    __tablename__ = 'manager_form'

    id = db.Column(db.Integer, primary_key=True)
    emp_code1 = db.Column(db.String(255))
    reviewer_name1 = db.Column(db.String(255))
    reviewer_code1 = db.Column(db.String(255))
    manager_assessment1=db.Column(db.String(255))
    manager_assessment1_comment1 = db.Column(db.String(255))

    achieved_score1 = db.Column(db.String(255))

    manager_assessment2 = db.Column(db.String(255))
    manager_assessment2_comment2 = db.Column(db.String(255))

    achieved_score2 = db.Column(db.String(255))

    manager_assessment3 = db.Column(db.String(255))
    manager_assessment3_comment3 = db.Column(db.String(255))

    achieved_score3 = db.Column(db.String(255))

    manager_assessment4 = db.Column(db.String(255))
    manager_assessment4_comment4 = db.Column(db.String(255))

    achieved_score4 = db.Column(db.String(255))

    manager_assessment5 = db.Column(db.String(255))
    manager_assessment5_comment5 = db.Column(db.String(255))

    achieved_score5 = db.Column(db.String(255))

    manager_assessment6 = db.Column(db.String(255))
    manager_assessment6_comment6 = db.Column(db.String(255))

    achieved_score6 = db.Column(db.String(255))

    total_achieved_score = db.Column(db.String(255))

    manager_final_comment = db.Column(db.String(255))
    manager_final_rating = db.Column(db.String(255))

    rev_email1 = db.Column(db.String(255))
    signaturepath = db.Column(db.String(255))

    IP_addr = db.Column(db.String(255))
    Location = db.Column(db.String(255))
    UserAgent = db.Column(db.String(255))
    OperatingSystem = db.Column(db.String(255))
    Time = db.Column(db.DateTime)
