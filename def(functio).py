def bmi(berat, tinggi):

    hasil = int(berat) / float(tinggi **2)

    print("hasil bmi anda adalah", hasil)

    if(hasil < 17.0):
        print("anda sangat kurus")
    elif(hasil >= 17.0 and hasil <= 18.0):
        print("anda cukup kurus")
    elif(hasil >=18.1 and hasil <= 25.0 ):
        print("anda nromal")
    elif(hasil >= 25.1 and hasil <= 27.0 ):
        print("anda cukup gemuk")
    else:
        print("anda obesitas")
           
    
    
