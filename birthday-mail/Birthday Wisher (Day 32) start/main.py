import smtplib

my_email = "rupakhetikaushal649@gmail.com"
password = "jmwb hqee cass rohn"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # make the connection secure
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr= my_email, to_addrs="rupakhetikaushal2024@gmail.com", msg= "Subject:Hello\n\n This is the content of my email")
