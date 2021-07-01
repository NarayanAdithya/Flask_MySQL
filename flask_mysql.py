from app import app, db
from app.models import user,courses

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': user,'Courses':courses}

if __name__=="__main__":
    app.run(debug=True)


#Connect to MySQL local server using mysql+pymysql://username:password@localhost/db_name