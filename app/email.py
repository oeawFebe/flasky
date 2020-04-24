from threading import Thread

def send_email(to,subject,template,**kwargs):#kwargs will be template context, see line 3,4 below
    msg=Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    thr=Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr    
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)
