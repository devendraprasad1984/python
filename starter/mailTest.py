import sys, smtplib

message_template="""
To:{}
From:{}
Subject:Test message from first python app

Hello,
I am happy coding python

"""

def main():
    if len(sys.argv<4):
        name=sys.argv[0]
        sys.exit(2)
    server,fromaddr,toaddr=sys.argv[1],sys.argv[2],sys.argv[3:]
    message=message_template.format(','.join(toaddr),fromaddr)
    connection=smtplib.SMTP(server)
    connection.sendmail(fromaddr,toaddr,message)
    connection.quit()

    s='' if len(toaddr)==1 else 's'
    print('message sent to {} recepients {}'.format(len(toaddr),s))

if __name__=='__main__':
    main()

