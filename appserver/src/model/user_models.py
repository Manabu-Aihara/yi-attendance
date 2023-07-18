from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db, app

class User(db.Model):
    __tablename__ = "M_STAFFINFO"
    STAFFID = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    DEPARTMENT_CODE = db.Column(db.Integer, index=True, nullable=True)
    TEAM_CODE = db.Column(db.Integer, index=True, nullable=True)
    CONTRACT_CODE = db.Column(db.Integer, index=True, nullable=True)
    JOBTYPE_CODE = db.Column(db.Integer, index=True, nullable=True)
    POST_CODE = db.Column(db.Integer, index=True, nullable=True)
    LNAME = db.Column(db.String(50), index=True, nullable=True)
    FNAME = db.Column(db.String(50), index=True, nullable=True)
    LKANA = db.Column(db.String(50), index=True, nullable=True)
    FKANA = db.Column(db.String(50), index=True, nullable=True)
    POST = db.Column(db.String(10), index=True, nullable=True)
    ADRESS1 = db.Column(db.String(50), index=True, nullable=True)
    ADRESS2 = db.Column(db.String(50), index=True, nullable=True)
    TEL1 = db.Column(db.String(50), index=True, nullable=True)
    TEL2 = db.Column(db.String(50), index=True, nullable=True)
    BIRTHDAY = db.Column(db.DateTime(), index=True, nullable=True)
    INDAY = db.Column(db.DateTime(), index=True, nullable=True)
    OUTDAY = db.Column(db.DateTime(), index=True, nullable=True)
    STANDDAY = db.Column(db.DateTime(), index=True, nullable=True)
    SOCIAL_INSURANCE = db.Column(db.Integer, index=True, nullable=True)
    EMPLOYMENT_INSURANCE = db.Column(db.Integer, index=True, nullable=True)
    EXPERIENCE = db.Column(db.Integer, index=True, nullable=True)
    TABLET = db.Column(db.Integer, index=True, nullable=True)
    SINGLE = db.Column(db.Integer, index=True, nullable=True)
    SUPPORT = db.Column(db.Integer, index=True, nullable=True)
    HOUSE = db.Column(db.Integer, index=True, nullable=True)
    DISTANCE = db.Column(db.Float, index=True, nullable=True)
    REMARK = db.Column(db.String(100), index=True, nullable=True)
    M_LOGGININFOs = db.relationship('StaffLoggin', backref='M_STAFFINFO', lazy='dynamic')  
    M_RECORD_PAIDHOLIDAYs = db.relationship('RecordPaidHoliday', backref='M_STAFFINFO', lazy='dynamic')
    D_COUNT_ATTENDANCEs = db.relationship('CountAttendance', backref='M_STAFFINFO', lazy='dynamic')
    D_TIME_ATTENDANCEs = db.relationship('TimeAttendance', backref='M_STAFFINFO', lazy='dynamic')
    D_COUNTER_FOR_TABLEs = db.relationship('CounterForTable', backref='M_STAFFINFO', lazy='dynamic')
    M_SYSTEMINFOs = db.relationship('SystemInfo', backref='M_STAFFINFO', lazy='dynamic')    
    
    def __init__(self, STAFFID):
        self.STAFFID = STAFFID

class StaffLogin(UserMixin, db.Model):
    __tablename__ = "M_LOGGININFO"
    id = db.Column(db.Integer, primary_key=True)
    STAFFID = db.Column(db.Integer, db.ForeignKey('M_STAFFINFO.STAFFID'), unique=True, index=True, nullable=False)
    PASSWORD_HASH = db.Column(db.String(128), index=True, nullable=True)
    ADMIN = db.Column(db.Boolean(), index=True, nullable=True)
    shinseis = db.relationship('Shinsei', backref='M_LOGGININFO', lazy='dynamic')

    def __init__(self, STAFFID, PASSWORD, ADMIN):
        self.STAFFID = STAFFID
        self.PASSWORD_HASH = generate_password_hash(PASSWORD)
        self.ADMIN = ADMIN

    def check_password(self, PASSWORD):
        return check_password_hash(self.PASSWORD_HASH, PASSWORD)

    def is_admin(self):
        return self.ADMIN

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.STAFFID}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return StaffLogin.query.filter_by(STAFFID=user_id)
    
class Applied(db.Model):
    __tablename__ = "M_ATTENDANCE"
    id = db.Column(db.Integer, primary_key=True)
    STAFFID = db.Column(db.Integer, db.ForeignKey('M_LOGGININFO.STAFFID'), index=True)
    WORKDAY = db.Column(db.String(32), index=True, nullable=True)
    HOLIDAY = db.Column(db.String(32), index=True, nullable=True)
    STARTTIME = db.Column(db.String(32), index=True, nullable=True) # 出勤時間
    ENDTIME = db.Column(db.String(32), index=True, nullable=True) # 退勤時間
    MILEAGE = db.Column(db.String(32), index=True, nullable=True) # 走行距離
    ONCALL = db.Column(db.String(32), index=True, nullable=True) # オンコール当番
    ONCALL_COUNT = db.Column(db.String(32), index=True, nullable=True) # オンコール回数
    ENGEL_COUNT = db.Column(db.String(32), index=True, nullable=True) # エンゼルケア
    NOTIFICATION = db.Column(db.String(32), index=True, nullable=True) # 届出（午前）
    NOTIFICATION2 = db.Column(db.String(32), index=True, nullable=True) # 届出（午後） 
    OVERTIME = db.Column(db.String(32), index=True, nullable=True) # 残業時間申請
    REMARK = db.Column(db.String(100), index=True, nullable=True) # 備考

    def __init__(self, STAFFID, WORKDAY, HOLIDAY, STARTTIME, ENDTIME, MILEAGE,
                 ONCALL, ONCALL_COUNT, ENGEL_COUNT, NOTIFICATION, NOTIFICATION2, OVERTIME,  REMARK):
        self.STAFFID = STAFFID
        self.WORKDAY = WORKDAY
        self.HOLIDAY = HOLIDAY
        self.STARTTIME = STARTTIME
        self.ENDTIME = ENDTIME
        self.MILEAGE = MILEAGE
        self.ONCALL = ONCALL
        self.ONCALL_COUNT = ONCALL_COUNT
        self.ENGEL_COUNT = ENGEL_COUNT
        self.NOTIFICATION = NOTIFICATION
        self.NOTIFICATION2 = NOTIFICATION2
        self.OVERTIME = OVERTIME
        self.REMARK = REMARK

