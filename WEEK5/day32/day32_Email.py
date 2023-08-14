import smtplib
my_email = "aaminuabdulrahman@gmail.com"
password = "xsxsxsxs"

try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)  #587_is_the_port_number_for_TLS
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abeds7@gmail.com", msg="Subject:This is the practical sample")
    connection.quit()  #_Use_quit()_instead_of_close()
    print("Email sent successfully! ")
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your email you provided and password.")
except smtplib.SMTPException as e:
    print("Error sending email:", e)
except Exception as e:
    print("An unexpected error occurred:", e)