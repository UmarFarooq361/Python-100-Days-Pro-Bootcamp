import smtplib
import datetime as dt
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="abcdf@gmail.com",password="Cccdddff")
    connection.sendmail(
        from_addr = "abcdf@gmail.com",
        to_addrs  = "aaaaad@gmail.com",
        msg="Subject:Hello\n\nHi umar from python"
    )

today = dt.datetime.now()
print(today)
hbd = dt.datetime(year=1990, month= 5, day= 23)
print(f"My date of birth is {hbd}")