import tkinter as tk
from tkinter import *
from tkinter import Tk,filedialog
from PIL import Image,ImageTk
import os
import cv2
from skimage.feature import local_binary_pattern
import numpy as np
import hashlib
import dlib

import mysql.connector as s
mc=s.connect(host="localhost",user="root",passwd='',database="SAS")
if mc.is_connected()==False:
    print("connection unsuccessful")
cr=mc.cursor()

global image1



def login():
    a=Toplevel(root)
    a.title("Admin Login")
    a.geometry("450x220")
    a.configure(bg='black')
    
    IDlab=Label(a,text="Enter ID: ",bg='black',fg='white',font=("Arial", 12)).place(x=30,y=30)
    Id=Entry(a,width=30)
    Id.place(x=150,y=30)
    PASSlab=Label(a,text="Enter Passwd: ",bg='black',fg='white',font=("Arial", 12)).place(x=30,y=80)
    Pass=Entry(a,width=30)
    Pass.place(x=150,y=80)
    
    def instopp():
        if Id.get()=="" and Pass.get()=="":
            a.destroy()
            interface2()
        else:
            P=Label(a,text="Worng ID/Passcode").pack()
    logbut=Button(a,text="Login",command=instopp,width=10,bd=10).place(x=100,y=150)
    clo=Button(a,text="close",command=a.destroy,width=10,bd=11).place(x=300,y=150)
    


def interface2():
    
    in2 = tk.Toplevel(root)
    in2.title("Add New ID")
    in2.geometry("900x500")

    canvas = tk.Canvas(in2, width=900, height=500)
    canvas.place(x=0,y=0)
    yuio=r"bg3.png"
    background_image = tk.PhotoImage(file=yuio)
    res_image4=background_image.subsample(1)
    canvas.create_image(0, 0, anchor=tk.NW, image=res_image4)

    
    abc = Label(in2, text="Create New Authentication IDs", font=("Calibri", 14, "bold"), bg='cyan')
    abc.place(x=300,y=50)

    image_path1 = r'index_finger.png'
    image1 = tk.PhotoImage(file=image_path1)

    image_label = tk.Label(in2, image=image1)
    image_label.place(x=150,y=150)

    image_path2 = r'Facegui.png'
    image2 = tk.PhotoImage(file=image_path2)
    res_image2=image2.subsample(5)

    image_label = tk.Label(in2, image=res_image2)
    image_label.place(x=600,y=150)


    def open_file_dialog_fing():
        global file_path_fing
        file_path_fing = filedialog.askopenfilename()
        file_name_fing = os.path.basename(file_path_fing)
        if file_path_fing:
            selected_file_label.config(text="Selected File: " + file_name_fing)
        else:
            selected_file_label.config(text="No file selected")
        return file_path_fing

    select_file_button1 = tk.Button(in2, text="Select File", command=open_file_dialog_fing)
    select_file_button1.place(x=165,y=260)

    selected_file_label = tk.Label(in2, text="-", font=("Arial", 12),bg='black',fg='white')
    selected_file_label.place(x=100,y=290)

    def open_file_dialog_face():
        global file_path_face
        file_path_face = filedialog.askopenfilename()
        file_name_face = os.path.basename(file_path_face)
        if file_path_fing:
            selected_file_labe2.config(text="Selected File: " + file_name_face)
        else:
            selected_file_labe2.config(text="No file selected")
        return file_path_face

    select_file_button2 = tk.Button(in2, text="Select File", command=open_file_dialog_face)
    select_file_button2.place(x=615,y=260)

    selected_file_labe2 = tk.Label(in2, text="-", font=("Arial", 12),bg='black',fg='white')
    selected_file_labe2.place(x=550,y=290)

    def generate_hash():
        global fingerprint_hash
        global face_hashvalue
        global hex_decimal_result
        def finger_hash():
            global unique_finger_hash
            def extract_features(fingerprint_image_path):
                global asd
                fingerprint_img = cv2.imread(fingerprint_image_path, cv2.IMREAD_GRAYSCALE)
                radius = 3
                n_points = 8 * radius
                lbp_image = local_binary_pattern(fingerprint_img, n_points, radius, method='uniform')
                unique_value = np.sum(lbp_image)
                asd= unique_value
                return asd
            def hashing(unique_value):
                def calculate_sha256_hash(input_data):
                    input_string = str(input_data)
                    sha256 = hashlib.sha256()
                    sha256.update(input_string.encode('utf-8'))
                    hash_value = sha256.hexdigest()
                    return hash_value
                input_data = unique_value
                sha256_hash = calculate_sha256_hash(input_data)
                #print("SHA-256 hash of '{}' is: {}".format(input_data, sha256_hash))
                return sha256_hash

            # Example usage
            if __name__ == "__main__":
                root = tk.Tk()
                root.withdraw()
                fingerprint_image_path = file_path_fing
                unique_data_value = extract_features(fingerprint_image_path)
                unique_finger_hash=hashing(asd)
                #print(unique_finger_hash)
            return unique_finger_hash

        def face_hash():
            global unique_face_hash
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

            def normalize_features(features):
                mean = np.mean(features, axis=0)
                std_dev = np.std(features, axis=0)
                epsilon = 1e-10
                std_dev += epsilon
                
                normalized_features = (features - mean) / std_dev
                return normalized_features

            def extract_and_hash_features(image_path):
                img = dlib.load_rgb_image(image_path)
                faces = detector(img)
                features = []
                for face in faces:
                    shape = predictor(img, face)
                    face_features = np.array([[point.x, point.y] for point in shape.parts()])
                    features.append(face_features)
                    normalized_features = normalize_features(np.array(features))
                    if len(normalized_features) == 0:
                        print("Try again")
                    else:
                        hasher = hashlib.sha256()
                        for feature in normalized_features:
                            feature_bytes = feature.tobytes()
                            hasher.update(feature_bytes)
                    a=hasher.hexdigest()
                    return a
            if __name__ == "__main__":
                image_path = file_path_face
                unique_face_hash = extract_and_hash_features(image_path)
                #print("Unique hash value for the facial features:", unique_face_hash)
            return unique_face_hash

        def final_hash():
            global hex_decimal_result
            try:
                decimal_value1 = int(unique_finger_hash, 16)
                binary_value1 = bin(decimal_value1)
                binary_value_fing = '0'+binary_value1[2:]
            except ValueError:
                print("Invalid hexadecimal value. Please enter a valid fing hexadecimal number.")

            try:
                decimal_value2 = int(unique_face_hash, 16)
                binary_value2 = bin(decimal_value2)
                binary_value_face = '0'+binary_value2[2:]
            except ValueError:
                print("Invalid hexadecimal value. Please enter a valid face hexadecimal number.")

            num1 = int(binary_value_fing, 2)
            num2 = int(binary_value_face, 2)
            result = num1 ^ num2
            result_value_binary = bin(result)[2:]

            def binary_to_hexadecimal(result_value_binary):
                decimal_num = int(result_value_binary, 2)
                hex_decimal_result = hex(decimal_num).upper()[2:]
                return hex_decimal_result
            if set(result_value_binary) <= {'0', '1'}:
                hex_decimal_result  = binary_to_hexadecimal(result_value_binary)
                #print(f"The hexadecimal representation of {result_value_binary} is:{hex_decimal_result}")
            else:
                print("Invalid input. Please enter a binary number.")
            return hex_decimal_result

            
        fingerprint_hash= finger_hash()
        face_hashvalue= face_hash()
        
        

        if unique_face_hash == None :
            inx=Tk()
            inx.title("Warning!!!!")
            inx.configure(bg='red')
            inx.geometry("480x50")
            b1=Label(inx,text='Resubmit Facial Feature!!!',bg='red', font=("Arial", 30)).grid(row=3,column=0)
        resulting_hash= final_hash()
        return fingerprint_hash,face_hashvalue,hex_decimal_result


    
    def store_hash():
        sql="INSERT INTO result_hashes values('{}')".format(hex_decimal_result)
        try:
            cr.execute(sql)
            mc.commit()
            lab1=Label(in2,text='ok')
            susfg=Label(in2,text="Hash succesfully Added!!!").place(x=400,y=450)
        except:
            mc.rollback()
        

    genhash=Button(in2,text="Generate Unique Hash",command=generate_hash,fg="black",bg="light blue",width=28,bd=8).place(x=200,y=320)
    storhash=Button(in2,text="Store Hash",command=store_hash,fg="black",bg="light blue",width=28,bd=8).place(x=500,y=320)
    closewin=Button(in2,text="Close",command=in2.destroy,fg="black",bg="light blue",width=28,bd=8).place(x=350,y=400)
    in2.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------
def authenticate():
    in3 = tk.Toplevel(root)
    in3.title("Authentication Page")
    in3.geometry("600x650")

    canvas = tk.Canvas(in3, width=600, height=650)
    canvas.place(x=0,y=0)
    bsg=r"bg1.png"
    background_image = tk.PhotoImage(file=bsg)
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
    
    abc = Label(in3, text="Authentication", font=("Calibri", 26, "bold"), bg='black',fg='white')
    abc.place(x=200,y=50)

    image_path1 = r'index_finger.png'
    image1 = tk.PhotoImage(file=image_path1)

    image_label = tk.Label(in3, image=image1)
    image_label.place(x=100,y=150)

    image_path2 = r'Facegui.png'
    image2 = tk.PhotoImage(file=image_path2)
    res_image2=image2.subsample(5)

    image_label = tk.Label(in3, image=res_image2)
    image_label.place(x=100,y=400)

    

    def open_file_dialog_fing():
        global file_path_fing1
        file_path_fing1 = filedialog.askopenfilename()
        file_name_fing1= os.path.basename(file_path_fing1)
        if file_path_fing1:
            selected_file_label.config(text="Selected File: " + file_name_fing1)
        else:
            selected_file_label.config(text="No file selected")
        return file_path_fing1

    select_file_button1 = tk.Button(in3, text="Select File", command=open_file_dialog_fing)
    select_file_button1.place(x=115,y=270)

    selected_file_label = tk.Label(in3, text="-", font=("Arial", 12),fg='white',bg='black')
    selected_file_label.place(x=50,y=300)

    def open_file_dialog_face():
        global file_path_face1
        file_path_face1 = filedialog.askopenfilename()
        file_name_face1 = os.path.basename(file_path_face1)
        if file_path_face1:
            selected_file_labe2.config(text="Selected File: " + file_name_face1)
        else:
            selected_file_labe2.config(text="No file selected")
        return file_path_face1

    select_file_button2 = tk.Button(in3, text="Select File", command=open_file_dialog_face)
    select_file_button2.place(x=120,y=520)

    selected_file_labe2 = tk.Label(in3, text="-", font=("Arial", 12),fg='white',bg='black')
    selected_file_labe2.place(x=50,y=550)

    def generate_hash():
        global fingerprint_hash1
        global face_hashvalue1
        global hex_decimal_result1
        def finger_hash():
            global unique_finger_hash1
            def extract_features(fingerprint_image_path1):
                global asdr
                fingerprint_img = cv2.imread(fingerprint_image_path1, cv2.IMREAD_GRAYSCALE)
                radius = 3
                n_points = 8 * radius
                lbp_image = local_binary_pattern(fingerprint_img, n_points, radius, method='uniform')
                unique_value1 = np.sum(lbp_image)
                asdr= unique_value1
                return asdr
            def hashing(unique_value1):
                def calculate_sha256_hash(input_data):
                    input_string = str(input_data)
                    sha256 = hashlib.sha256()
                    sha256.update(input_string.encode('utf-8'))
                    hash_value = sha256.hexdigest()
                    return hash_value
                input_data = unique_value1
                sha256_hash = calculate_sha256_hash(input_data)
                #print("SHA-256 hash of '{}' is: {}".format(input_data, sha256_hash))
                return sha256_hash

            # Example usage
            if __name__ == "__main__":
                root = tk.Tk()
                root.withdraw()
                fingerprint_image_path1 = file_path_fing1
                unique_data_value = extract_features(fingerprint_image_path1)
                unique_finger_hash1=hashing(asdr)
                #print(unique_finger_hash1)
            return unique_finger_hash1

        def face_hash():
            global unique_face_hash1
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

            def normalize_features(features):
                mean = np.mean(features, axis=0)
                std_dev = np.std(features, axis=0)
                epsilon = 1e-10
                std_dev += epsilon
                
                normalized_features = (features - mean) / std_dev
                return normalized_features

            def extract_and_hash_features(image_path):
                img = dlib.load_rgb_image(image_path)
                faces = detector(img)
                features = []
                for face in faces:
                    shape = predictor(img, face)
                    face_features = np.array([[point.x, point.y] for point in shape.parts()])
                    features.append(face_features)
                    normalized_features = normalize_features(np.array(features))
                    if len(normalized_features) == 0:
                        print("Try again")
                    else:
                        hasher = hashlib.sha256()
                        for feature in normalized_features:
                            feature_bytes = feature.tobytes()
                            hasher.update(feature_bytes)
                    a=hasher.hexdigest()
                    return a
            if __name__ == "__main__":
                image_path = file_path_face1
                unique_face_hash1 = extract_and_hash_features(image_path)
                #print("Unique hash value for the facial features:", unique_face_hash1)
            return unique_face_hash1

        def final_hash():
            global hex_decimal_result1
            try:
                decimal_value11 = int(unique_finger_hash1, 16)
                binary_value11 = bin(decimal_value11)
                binary_value_fing1 = '0'+binary_value11[2:]
            except ValueError:
                print("Invalid hexadecimal value. Please enter a valid fing hexadecimal number.")

            try:
                decimal_value22 = int(unique_face_hash1, 16)
                binary_value22 = bin(decimal_value22)
                binary_value_face1 = '0'+binary_value22[2:]
            except ValueError:
                print("Invalid hexadecimal value. Please enter a valid face hexadecimal number.")

            num11 = int(binary_value_fing1, 2)
            num22 = int(binary_value_face1, 2)
            result = num11 ^ num22
            result_value_binary1 = bin(result)[2:]

            def binary_to_hexadecimal(result_value_binary1):
                decimal_num = int(result_value_binary1, 2)
                hex_decimal_result1 = hex(decimal_num).upper()[2:]
                return hex_decimal_result1
            if set(result_value_binary1) <= {'0', '1'}:
                hex_decimal_result1 = binary_to_hexadecimal(result_value_binary1)
                #print(f"The hexadecimal representation of {result_value_binary1} is:{hex_decimal_result1}")
            else:
                print("Invalid input. Please enter a binary number.")
            return hex_decimal_result1

            
        fingerprint_hash1= finger_hash()
        face_hashvalue1= face_hash()
        
        

        if unique_face_hash1 == None :
            inx=Tk()
            inx.title("Warning!!!!")
            inx.configure(bg='red')
            inx.geometry("480x50")
            b1=Label(inx,text='Resubmit Facial Feature!!!',bg='red', font=("Arial", 30)).grid(row=3,column=0)
        resulting_hash1= final_hash()
        return fingerprint_hash1,face_hashvalue1,hex_decimal_result1

    def authenticate_user():
        ade=hex_decimal_result1
        cr.execute("SELECT * FROM result_hashes".format(ade))
        data=cr.fetchall()
        iz=0
        for row in data:
            hashes=row[0]
            if hashes == ade:
                iz+=1
        if iz==1:
            c1=Label(in3,text='Authentication success',bg='light green', font=("Arial",16)).place(x=300,y=550)
        if iz==0:
            c2=Label(in3,text=' Try Again !!!!!!!!!!!!!!!!!!!!',bg='Red', font=("Arial",16)).place(x=300,y=550)
            


    submit1=Button(in3,text="Submit",command=generate_hash,fg="black",bg="yellow",width=14,bd=8,font=("Arial",14)).place(x=350,y=220)
    authent=Button(in3,text="Authenticate User",command=authenticate_user,fg="black",bg="yellow",width=16,bd=8,font=("Arial",14)).place(x=350,y=340)
    closewin=Button(in3,text="Close",command=in3.destroy,fg="black",bg="yellow",width=10,bd=8,font=("Arial",14)).place(x=350,y=460)

    in3.mainloop()
    


#-------------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.title("SAS Main Menu")
root.geometry("800x500")

canvas = tk.Canvas(root, width=800, height=500)
canvas.place(x=0,y=0)
bsge=r"abst.png"
background_image = tk.PhotoImage(file=bsge)
res_image3=background_image.subsample(1)
canvas.create_image(0, 0, anchor=tk.NW, image=res_image3)

projname=Label(root,text="""+---------------------------------------------------------------------+
~Secure Authentication Service~
+---------------------------------------------------------------------+""",font=("Calibri",14,"bold"),bg='black',fg='white')
projname.place(x=200,y=5)


a=Button(root,text="Add new IDs",command=login,fg="black",bg="orange",width=22,bd=8,font='bold').place(x=150,y=150)

b=Button(root,text="Authenticate",command=authenticate,fg="black",bg="#FF7F7F",width=22,bd=8,font='bold').place(x=150,y=250)

c=Button(root,text="Exit..",command=root.destroy,fg="black",bg="cyan",width=22,bd=8,font='bold').place(x=150,y=350)

rtyo=Label(root,text="By Sanjay.R.S",font=("Calibri",14,"bold"),bg='black',fg='white')
rtyo.place(x=5,y=465)



root.mainloop()
